# Gerekli kütüphaneleri içe aktarıyoruz
import cv2          # OpenCV: Görüntü işleme kütüphanesi
import numpy as np  # NumPy: Sayısal işlemler ve matrisler için kullanılır
import mediapipe as mp

# MediaPipe bileşenleri
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# El tespiti için Hands modülü (tek sefer tanımlanmalı)
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)


# Bu fonksiyon, gelen görüntüde yumruk var mı kontrol eder
def detect_fist_with_mediapipe(frame):
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # BGR'den RGB'ye çevir
    results = hands.process(image)  # MediaPipe el analizini yap

    is_fist = False  # Başlangıçta yumruk yok varsay

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Her parmak ucu için uç noktaları avuç içine yakın mı kontrol ediyoruz
            tips_ids = [8, 12, 16, 20]  # İşaret, orta, yüzük ve serçe parmak uçları
            closed_fingers = 0

            for tip_id in tips_ids:
                tip = hand_landmarks.landmark[tip_id]
                base = hand_landmarks.landmark[tip_id - 2]  # Parmağın bir önceki eklemi

                if tip.y > base.y:  # Uç nokta alta doğru bükülmüşse, parmak kapalıdır
                    closed_fingers += 1

            if closed_fingers == 4:  # 4 parmak da kapalıysa yumruk diyebiliriz
                is_fist = True

            # El iskeletini çiziyoruz
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    return frame, is_fist


# Bu fonksiyon bir görüntü (kare/frame) alır ve 3 farklı işlem uygular:
# 1. Grayscale (siyah beyaz)
# 2. Renk tespiti (kırmızı)
# 3. Şekil tespiti (kontur)
def process_frame(frame):
    # 1. Grayscale (siyah beyaz)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Renkli görüntüyü griye çeviriyoruz

    # 2. Renk Tespiti (Kırmızı Renk)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Görüntüyü HSV formatına çeviriyoruz
    # HSV renk uzayında kırmızı rengin alt ve üst sınırlarını tanımlıyoruz
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    # Bu aralıktaki kırmızı bölgeleri maske ile tespit ediyoruz
    red_mask = cv2.inRange(hsv, lower_red, upper_red)
    # Maskeyi kullanarak sadece kırmızı alanları gösteriyoruz
    red_detected = cv2.bitwise_and(frame, frame, mask=red_mask)

    # 3. Şekil Tespiti
    # İlk olarak grayscale görüntü üzerinden kenarları tespit ediyoruz
    edges = cv2.Canny(gray, 50, 150)  # Kenar bulma (Canny algoritması)
    # Bulunan kenarlardan konturları elde ediyoruz
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    shapes = frame.copy()  # Orijinal görüntünün kopyası üzerinde çizim yapacağız

    # Tüm konturlar üzerinde dönüyoruz
    for cnt in contours:
        area = cv2.contourArea(cnt)  # Konturun alanını hesaplıyoruz
        if area > 500:  # Gürültüleri ayıklamak için çok küçük konturları es geçiyoruz
            # Konturu yaklaşık hale getiriyoruz (şeklin köşelerini bulmak için)
            approx = cv2.approxPolyDP(cnt, 0.04 * cv2.arcLength(cnt, True), True)
            # Şekli yeşil çizgiyle işaretliyoruz
            cv2.drawContours(shapes, [approx], 0, (0, 255, 0), 2)

    # === Yumruk Tespiti ve Güvenilir yazısı ===
    shapes, is_fist = detect_fist_with_mediapipe(shapes)
    if is_fist:
        # Yumruk varsa görüntüye yazı ekle
        cv2.putText(shapes, "Güvenilir", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                    1.5, (0, 255, 0), 3, cv2.LINE_AA)

    # 3 ayrı işlem sonucunu geri döndürüyoruz
    return gray, red_detected, shapes


# Kamera modunu başlatan fonksiyon
def camera_mode():
    cap = cv2.VideoCapture(0)  # Bilgisayarın kamerasını açar (0 = varsayılan kamera)

    while True:
        ret, frame = cap.read()  # Kameradan bir kare (frame) alıyoruz
        if not ret:
            break  # Eğer kare alınamadıysa döngüden çık

        # Alınan kareye 3 işlem uyguluyoruz
        gray, red, shapes = process_frame(frame)

        # Her sonucu ayrı pencerelerde gösteriyoruz
        cv2.imshow("Gray", gray)  # Siyah beyaz pencere
        cv2.imshow("Red Detection", red)  # Kırmızı tespiti pencere
        cv2.imshow("Shape Detection", shapes)  # Şekil tespiti pencere

        # Klavyeden 'q' tuşuna basıldığında çıkış yap
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Kamera ve pencereleri kapat
    cap.release()
    cv2.destroyAllWindows()


# Dosyadan görsel seçmek için kullanılan mod
def image_mode(image_path):
    image = cv2.imread(image_path)  # Bilgisayardan görüntüyü okuyoruz
    # Aynı 3 işlem burada da uygulanıyor
    gray, red, shapes = process_frame(image)

    # Sonuçları göstermek için 3 ayrı pencere açıyoruz
    cv2.imshow("Gray", gray)
    cv2.imshow("Red Detection", red)
    cv2.imshow("Shape Detection", shapes)
    cv2.waitKey(0)  # Bir tuşa basılana kadar pencereyi açık tut
    cv2.destroyAllWindows()


# === Programın başlangıç noktası ===

# Kullanıcıdan hangi modda çalışmak istediğini soruyoruz
mode = input("Modu seçin (1: Kamera, 2: Görsel): ")

# Kullanıcı "1" girerse kamera modu çalışır
if mode == "1":
    camera_mode()

# Kullanıcı "2" girerse görsel yolu sorulur ve image_mode çalışır
elif mode == "2":
    path = input("Görsel dosya yolunu girin: ")
    image_mode(path)

# Geçersiz bir değer girilirse uyarı verilir
else:
    print("Geçersiz seçim.")

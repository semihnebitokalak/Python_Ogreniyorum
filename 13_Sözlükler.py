# Bu dersimizde sözlük kavramını ele alacağız.
# Python'da sözlükler, anahtar-değer çiftleri şeklinde veri saklamaya yarayan veri yapılarıdır. 
# Boş bir sözlük oluşturma = bos_sozluk = {}

mevsim = {"kis = 1 ","ilkbahar = 2 ","yaz = 3 ","sonbahar = 4 "}
print(mevsim)
TC = dict([("Semih",1234),("Ali",4567),("Mehmet",7801)])
print(TC)
# Anahtar-değer çiftleriyle sözlük oluşturma
sozluk = {
    "isim": "Ahmet",
    "yas": 25,
    "sehir": "İstanbul"
}
print(sozluk)
# Yeni bir anahtar-değer çifti ekleme
sozluk["meslek"] = "Mühendis"
print(sozluk)
# Mevcut bir anahtarın değerini güncelleme
sozluk["yas"] = 26
print(sozluk)
# Anahtarları kullanarak sözlükteki değerlere erişebilirsin:
isim = sozluk["isim"]
yas = sozluk["yas"]
print(isim)
print(yas)
# genel olarak syntax bu şekilde.
# Şimdi boş sözlük oluşturup içini dolduralım ve yazdırıp gözlemleyelim.
S = {}
S[1] = "bir"
S[2] = "iki"
S[3] = "üç"
print(S)

# Şimdi sözlük fonksiyonlarını inceleyeceğiz.
# get() : anahtarın değerini döndürür.
# Anahtarın değerini döndürür. Anahtar sözlükte yoksa, varsayılan bir değer döndürür.
# Tüm fonksiyonlar için bir tane sözlük oluşturalım ve onu kullanalım.

Days_of_Week = {
    "Pazartesi": 1,
    "Sali": 2,
    "Carsamba": 3,
    "Persembe": 4,
    "Cuma": 5,
    "Cumartesi": 6,
    "Pazar": 7
}
print(Days_of_Week)

Pazartesi = Days_of_Week.get("Pazartesi", "yok")
print(Pazartesi)  # Çıktı: 1
Araba = Days_of_Week.get("Araba","yok")
print(Araba) # çıktı: yok   

# Listelerden de bildiğimiz üzere pop() fonksiyonunu inceleyeceğiz.
# Belirtilen anahtarı sözlükten çıkarır ve değerini döndürür. Anahtar bulunamazsa, KeyError hatası döner.
Sali = Days_of_Week.pop("Sali")
print(Days_of_Week)

# Sözlükteki anahtarları döndüren fonksiyon ise keys() tir.
key_words = (Days_of_Week.keys())
print(key_words)

# Aynı şekilde sadece değerleri de döndürebiliyoruz. value() ile
deger = Days_of_Week.values()
print(deger)

# Sözlükteki anahtar-değer çiftlerini döndürür. items() ile yapılır.
# dict edilmiş şekilde yazar.
anahtar_deger_cift = Days_of_Week.items()
print(anahtar_deger_cift)

# Şimdi ise küme kavramına bakalım.

K = {1,2,"hg","hb","LOL",33} # şeklinde tanımlayabiliriz.
print(K)

K = set("asdf555gh5jklş123pğ5") # şeklinde de tanımlanabilir. K değerini güncelledik.
print(K)
ne_tur = type(K) # K nın türü ne ?
print(ne_tur)

k1 = {1,2,3,4,5}
k2 = {1,3,6,8,9}
# Matematik dersindeki kümeler mantığı ile aynı. Şimdi kesişim birleşim işlemlerine bakalım.
# Birleşim
birlesim = k1 | k2 # k2|k1 şeklinde de yazılabilir.
print(birlesim)
print(len(k1))
print(len(k2))
print(len(birlesim))

# Kesişim
kesisim = k1 & k2
print(kesisim)

# Fark
fark1 = k1 - k2 
fark2 = k2 - k1
# fark yaparken farklı değer görüntülenebilir. Çünkü ilk yazdığımızdan diğerini çıkardığımızda ilk kümede olanlar yazılır.
print(fark1)
print(fark2)

# Şimdi demet(tuple) kavramını göreceğiz.
# listeler ile aynı olsa da birkaç tane farkı var. Hemen bakalım.
# liste oluşturalım.
L = [1,"ata",2,"hb"]
tip1 = type(L)
print(tip1)
T = (1,"ata",2,"hb")
tip1 = type(T)
print(tip1)
# listemizin ilk elemanını değiştirelim.
L[0] = 99
print(L)
# tuple ilk eleman değiştirelim.
# T(0) = 123
# T[0] = 123
# Bu iki değiştirme de kabul edilemez. Tuple değerleri sabittir ve bir kere tanımlama yapılır.
# Sıfırdan tanımlama yapıp değiştirmek lazım.
# Değiştirilemez olmasının nedeni hafızada kapladığı yer. Değiştirilemediği için listelerden daha az yer kaplar.
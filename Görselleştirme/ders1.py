import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
# pandas: Veri analizi ve manipülasyonu için kullanılır.
# matplotlib.pyplot: Grafik ve veri görselleştirme için kullanılır.
# numpy: Sayısal hesaplamalar ve dizi işlemleri için kullanılır.
# os: İşletim sistemiyle etkileşim için kullanılır.


#Örnek veri
# Excel dosyasından veri okuma
df = pd.read_excel('/Users/semihnebitokalak/Desktop/Desktop_2/Pyhton Öğreniyorum/Görselleştirme/teknolojik_urunler_zamanli.xlsx')

# 'Tarih' sütununu datetime formatına çevirme
df['Tarih'] = pd.to_datetime(df['Tarih'])

# 'Tarih' sütununu DataFrame'in indexi yapma (Zaman serisi analizi için gerekli)
df.set_index('Tarih', inplace=True)

# Terminal ekranını temizleme fonksiyonu
def ekran_temizleme():
    if os.name == 'nt':  # Windows işletim sistemi için
        os.system('cls')
    else:  # Linux ve Mac işletim sistemleri için
        os.system('clear')
        
# Yukarıdaki kod kullanıcının daha temiz bir arayüz görmesini sağlar.

#menu fonksiyonu
def menu():
    print("Grafik seçenekleri:")
    print("1. Satışların Zaman içindeki değişimi (Çizgi Grafik)")
    print("2. Aylık Toplam Satışlar (Bar Grafik)")
    print("3. Kategorilere Göre Satış Dağılımı (Pasta Grafik)")
    print("4. Fiyat ve Satış İlişkisi (Scatter Plot)")
    print("5. Fiyat Dağılımı (Histogram)")
    print("6. Aylık Satış Miktarları (Çizgi Grafik)")
    print("7. Fiyat Kategorisine Göre Toplam Satışlar (Bar Grafik)")
    print("0. Çıkış")
    
    return int(input("Seçiminizi yapın: "))


#kullanıcının seçimine göre ilgili işlemleri yapan fonksiyon

# Kullanıcının seçimine bağlı olarak ilgili grafiği çizen fonksiyon
def grafik_secim(secilen):
    if secilen == 1:
        # Zaman içindeki satış değişimini gösteren çizgi grafik
        df['Satış'].plot(title='Satışların Zaman içindeki değişimi', xlabel='Tarih', ylabel='Satış Miktarı')
        plt.show()

    
    elif secilen == 2:
        aylik_satis = df.resample('ME')['Satış'].sum()
        aylik_satis.plot(kind='bar', title='Aylık Toplam Satışlar', xlabel='Ay', ylabel='Toplam Satışı')
        df.resample('ME')
        plt.show()
        # resample() fonksiyonu, zaman serisi verisini belirli bir zaman dilimine göre yeniden düzenlemek için kullanılır.
        # 'ME' (Month End) parametresi, her ayın son gününü alarak veriyi gruplar.
        # Örneğin, Ocak 2025 verilerini 31 Ocak 2025 tarihine, Şubat 2025 verilerini 28 Şubat 2025 tarihine göre gruplar.
        # ['Satış'].sum():
        # "Satış" sütunundaki verileri her ay için toplayarak yeni bir veri serisi oluşturur.
        
    elif secilen == 3:     
        kategori_satis = df.groupby('Kategori')['Satış'].sum()
        kategori_satis.plot(kind='pie', autopct='%1.1f%%', title='Kategorilere Göre Satış Dağılımı')
        plt.ylabel('') 
        plt.show()
    elif secilen == 4:
        df.plot(kind='scatter', x='Fiyat (TL)', y='Satış', title='Fiyat ve Satış İlişkisi')
        z = np.polyfit(df['Fiyat (TL)'], df['Satış'], 1) # Doğrusal Regresyon Eğilim Çizgisi Ekleme
        p = np.poly1d(z) #  bulunan polinomu fonksiyon olarak tanımlar. Kullanabilmemizi sağlar.
        plt.plot(df['Fiyat (TL)'], p(df['Fiyat (TL)']), color='red')
        plt.show()
    elif secilen == 5:
        df['Fiyat (TL)'].plot(kind='hist', bins=10, title='Fiyat Dağılımı')
        plt.xlabel('Fiyat (TL)')
        plt.ylabel('Kategori')
        plt.show()
    elif secilen == 6:
        aylik_satis = df.resample('M')['Satış'].sum()
        aylik_satis.plot(kind='line', title='Aylık Satış Miktarları')
        plt.xlabel('Ay')
        plt.ylabel('Satış Miktarı')
        plt.show()
    elif secilen == 7:
        bins = [0, 2000, 5000, 10000, 20000, 30000]
        labels = ['Düşük', 'Orta', 'Yüksek', 'Çok Yüksek', 'Lüks']
        df['Fiyat Kategorisi'] = pd.cut(df['Fiyat (TL)'], bins=bins, labels=labels)
        df.groupby('Fiyat Kategorisi')['Satış'].sum().plot(kind='bar', title='Fiyat Kategorisine Göre Toplam Satışlar')
        plt.xlabel('Fiyat Kategorisi')
        plt.ylabel('Toplam Satış')
        plt.show()


while True:
    ekran_temizleme()
    secim = menu()
    if secim == 0:
        print('Çıkış Yapılıyor...')
        break
    elif 1 <= secim <= 7:
        grafik_secim(secim)
    else:
        print('Geçersiz bir seçim yaptınız..')
        break
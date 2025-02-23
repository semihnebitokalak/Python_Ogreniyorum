import numpy as np

dizi = np.array([1,2,3,4,5,])
print(dizi)

#Belirli aralıklarla artan np array kodu.
dizi = np.arange(0,10,2)
print(dizi)

dizi = np.linspace(0,17,5)
print(dizi)

boyut = dizi.ndim
veri_turu = dizi.dtype
print("Dizinin Boyutu :",boyut)
print("Dizinin Boyutu :",veri_turu)


# NumPy Kütüphanesinin Başlıca Özellikleri
# Çok Boyutlu Diziler (ndarray): Python’un standart listelerine kıyasla daha verimli, optimize edilmiş dizi yapıları sağlar.
# Hızlı Matematiksel İşlemler: Vektörel işlemler, matris çarpımı, lineer cebir işlemleri, istatistiksel hesaplamalar gibi birçok fonksiyon içerir.
# Birimsel Bellek Kullanımı: Python listelerine kıyasla daha az bellek tüketir ve yüksek performans sunar.
# Kolay Entegrasyon: SciPy, Pandas, Matplotlib gibi popüler bilimsel ve veri analiz kütüphaneleriyle uyumludur.
# Rastgele Sayı Üretimi: Olasılık ve istatistik çalışmalarında kullanılan rastgele sayı üretme fonksiyonlarına sahiptir.

zeros = np.zeros((3,3))  # 3x3 sıfırlardan oluşan matris
ones = np.ones((2,4))    # 2x4 birlerden oluşan matris
print(zeros)
print(ones)


random_numbers = np.random.rand(4)  # 0 ile 1 arasında 4 rastgele sayı
print(random_numbers)

data = np.array([10, 20, 30, 40, 50])
print("Ortalama:", np.mean(data))  # Ortalama hesaplama
print("Standart Sapma:", np.std(data))  # Standart sapma hesaplama

# NumPy, veri analizi, makine öğrenimi, görüntü işleme ve bilimsel hesaplamalar gibi birçok alanda kullanılır. Eğer büyük ölçekli verilerle çalışıyorsan veya matematiksel işlemler yapman gerekiyorsa NumPy oldukça işine yarayacaktır.


# Bu dersimizde fonksiyonları inceleyeceğiz...
# Fonksiyon Nedir?
# Programın belli işlevini(görevini) yerine getiren küçük program parçacıklarıdır.
# Fonksiyonlar, kodu daha modüler ve tekrar kullanılabilir hale getirmek için kullanılır.

# Fonksiyon Tanımlama
# Python'da bir fonksiyon tanımlamak için def anahtar kelimesi kullanılır. İşte basit bir fonksiyonun tanımlanması:
def merhaba_dunya():
    print("Merhaba, Dünya!")
# Bu fonksiyon çağrıldığında "Merhaba, Dünya!" yazdırır.
# Çağırma işlemi ise aşağıdaki şekilde yapılır.
# Tanımladığınız fonksiyonu çağırmak için sadece adını ve parantezleri kullanmanız yeterlidir:
merhaba_dunya()

# Parametreler ve Argümanlar
# Fonksiyon parametrelerini inceleyelim.
# Fonksiyonlar, dışarıdan veri alabilir ve bu verilerle işlemler yapabilir. 
# Parametreler, fonksiyon tanımlanırken belirtilir, argümanlar ise fonksiyon çağrılırken sağlanır.

"""
def selamlama(isim):
    print("Sayin",isim,"restoranimiza hosgeldiniz.")
    
ad = input("İsminizi giriniz..:")
selamlama(ad)
"""
# yukarıdaki kodu sonsuz döngüye alalım...

def selamlama(isim):
    print("Sayın", isim, "restoranımıza hoş geldiniz.")

while True:
    ad = input("İsminizi giriniz..: ")
    if ad == "dur":
        break
    selamlama(ad)
    
# Fonksiyonlar, dışarıdan veri alabilir ve bu verilerle işlemler yapabilir. 
# Parametreler, fonksiyon tanımlanırken belirtilir, argümanlar ise fonksiyon çağrılırken sağlanır.
def topla(a, b):
    return a + b

sonuc = topla(5, 3)
print(sonuc)  # Çıktı: 8

# Fonksiyon parametrelerine varsayılan değerler atanabilir. 
# Bu sayede, fonksiyon çağrıldığında bu parametreler verilmezse varsayılan değerler kullanılır.
def selamla(isim="Dünya"):
    print(f"Merhaba, {isim}!")

selamla()          # Çıktı: Merhaba, Dünya!
selamla("Ahmet")   # Çıktı: Merhaba, Ahmet!

# Dikdörtgenin çevresini ve alanını veren fonksiyonları yazalım ve ana programda değerleri bulalım.

def alan(u,g):
    Alan = u * g
    return Alan
def cevre(u,g):
    Cevre = 2 * (u + g)
    return Cevre

uzunluk = int(input("Lütfen dikdörtgenin uzun kenarini giriniz :"))
genişlik = int(input("Lütfen dikdörtgenin kisa kenarini giriniz :"))
print("Dikdörtgenin alani :",alan(uzunluk,genişlik))
print("Dikdörtgenin cevresi :",cevre(uzunluk,genişlik))

# Şimdi lokal ve global değişkenleri öğreneceğiz.

def topla():
    a=5
    b=3
    return a+b
print("toplam : ",topla())
# print(a) şeklinde a değişkenini yazdırmaya çalışırsak hata alırız çünkü a değişkeni fonksiyon içinde tanımlı.
# Bu yüzden a değeri ekrana verilmez. Fonksiyon içinde yazdırmamız veyahut global olarak tanımlamamız lazım.
a = 4
print(a)
# Şeklinde global olarak değer atadık ve ekrana 4 değerini yazdırdık.
# Şu şekilde de tanımlama yapabiliriz.
def topla():
    global k
    global l
    k = 12
    l = 10
    return k+l
# Şu şekilde tanımlarsak yine hata alırız > global k = 4 
print("toplam : ",topla())
print(k)
print(l)
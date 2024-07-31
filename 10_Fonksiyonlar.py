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

# İçeriği olmayan fonksiyon nedir? Hemen örnekle daha iyi anlayalımmm...
# Alt program(so fonksiyonlar)
def top():
    global t
    global y 
    t = 24
    y = 3
    return t + y
""" 
def cik():
def bol():
def carp():
eğer yukaridaki gibi tanimlayip kodu çaliştirirsak hata aliriz. Bunu engellemek için pass ifadesini kullanıyoruz.
"""
def cik():
    pass
def bol():
    pass
def carp():
    pass
# Ana program
print(top())
print(cik())
print(bol())
print(carp())

#Neden pass Kullanılır?
#Yer Tutucu: Geliştirme sürecinde fonksiyonların yapısını belirlemek için kullanılır.
#Hataları Önlemek: Henüz tamamlanmamış kod parçalarının çalışmasını sağlamak için kullanılır.
#Okunabilirlik: Kodun ileride hangi işlemlerin yapılacağını belirten bir işaret olarak kullanılır.
#Bu sayede, Python'da içeriği olmayan fonksiyonlar tanımlayabilir ve kodunuzu daha esnek ve yönetilebilir hale getirebilirsiniz.

# Şimdi ise fonksiyon kısaltma işlemini öğreneceğiz.
# Python'da fonksiyon kısaltma, genellikle lambda fonksiyonları kullanılarak yapılır. 
# lambda fonksiyonları, tek satırlık küçük ve anonim (ismi olmayan) fonksiyonlar tanımlamak için kullanılır. 
# lambda fonksiyonları, genellikle kısa ve basit işlemler için kullanılır ve daha okunabilir kod yazmayı sağlar.
# hemen örnekle pekiştirelimmm..

# Normal fonksiyon tanımlama
def topla(i, j):
    return i + j

# Lambda fonksiyonu ile aynı işlevi yerine getirme
topla_lambda = lambda i, j: i + j

# Kullanımı
print(topla(3, 4))          # Çıktı: 7
print(topla_lambda(3, 4))   # Çıktı: 7

# Şimdi bir diğer konu olan yinelemeli yani recursive fonksiyonları inceliyeceğiz.
# Bu bahsettiğimiz recursive nedir?
# Özyinelemeli (recursive) fonksiyonlar, kendilerini doğrudan veya dolaylı olarak çağıran fonksiyonlardır. 
# Bu tür fonksiyonlar, bir problemi daha küçük alt problemlere bölerek çözerler ve genellikle belirli bir duruma ulaştığında dururlar.

# üs alma işlemini yapalım.
def üsalma(taban,üs):
    if üs == 0:
        return 1
    else:
        return taban * üsalma(taban,üs-1)
taban = 3
üs = 2
print(üsalma(taban,üs))
# Yukarıdaki kodu süsleyip kullanıcıdan taban ve üs kısımlarını alabiliriz.

# Faktöriyel hesabı yapan recursive program
def faktoriyel(n):
    if n == 0:  # Temel durum
        return 1
    else:
        return n * faktoriyel(n - 1)  # Özyineleme adımı

# Örnek kullanım
print(faktoriyel(5))  # Çıktı: 120

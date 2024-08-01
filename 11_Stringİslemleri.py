# String, programlama dillerinde metin (text) verilerini temsil eden veri tipidir. 
# Python'da stringler, tek tırnak ('...'), çift tırnak ("..."), üç tek tırnak ('''...''') 
# veya üç çift tırnak ("""...""") kullanılarak tanımlanabilir. Stringler değişmezdir (immutable), 
# yani oluşturulduktan sonra değiştirilemezler. Her bir karakterin sırasıyla saklandığı bir karakter dizisi olarak düşünülebilir.
str1 = 'Merhaba'
str2 = "Dünya"
str3 = '''Bu
çok
satirli
bir string.'''
str4 = """Bu da
çok satirli
bir string."""
print(str1)
print(str2)
print(str3)
print(str4)

# Stringler, karakter dizileridir ve her karakterin bir index numarası vardır. Python'da indeksler 0'dan başlar.
# Boşluk ifadesi de bir indis kabul edilir.
str1 = "merhaba dünya"
print(str1[8]) # d değeri döner.
# Sıfırdan başlayıp indisleri teker teker çağırabildiğimiz gibi - indis ile son karakterden başlayarak yazabiliriz.
print(str1[-1]) # a değerini döndürür.
# python dilinde şu atamayı yapamıyoruz. str1[2] = 'k'. Normalde 2. indiste r harfi bulunuyor bu değeri değiştirmeyi ileride göreceğiz.

# Şimdi ise string ile ilgili işlemlere bakalım.
# string değerler nasıl birleştirilir.
# Stringleri birleştirmenin en basit yolu + operatörünü kullanmaktır.

str1 = "Merhaba"
str2 = "Dünya!"
birlesmis_string = str1 + " " + str2 # " " işaretini boşluk karakterini koymak için yazdık."
print(birlesmis_string)
print(str1 + str2)

# string değerler nasıl birden fazla tekrar eder.
# Bir stringi belirli bir sayıda tekrarlamak için * operatörü kullanılabilir.
str1 = "Python "
tekrarlanan_str = str1 * 3
print(tekrarlanan_str)  # Output: Python Python Python 

# String Parçalama (Slicing)
# Stringlerin belirli bir kısmını almak için dilimleme kullanılabilir.
str1 = "Merhaba Dünya"
parca = str1[8:]  # 8. indexten başlayıp sonuna kadar alır
print(parca)  # Output: Dünya
tersten_yaz = str1[::-1] # burada ise kodu tersten yazdırma işlemini yapıyoruz.
print(tersten_yaz)
# Şimdi string ifadedeki bir elemanı değiştireceğiz.
S = "PYTHON"
S2 = S[:3] + 'K' + S[4:]
print(S2)

#  String Değiştirme (Replace)
# Bir string içindeki belirli bir kısmı başka bir string ile değiştirmek için replace() metodu kullanılır.
str1 = "MErhaba Dünya"
degistirilmis_string = str1.replace("MErhaba","Selamlarrrr")
print(degistirilmis_string)

# Şimdi string ifadenin uzunluğunu bulalım.
# Bir stringin uzunluğunu bulmak için len() fonksiyonu kullanılır.
str1 = "Merhaba Dünya"
uzunluk = len(str1)
print(uzunluk)  # Output: 13
# Cümlenin içinden seçilen harfin kaç adet olduğunu count fonksiyonu ile buluyoruz.
harf_adet = str1.count('a')
print(harf_adet)

# string ifadeyi silme.
str1 = "python"
uzunluk = len(str1)
print(str1[:uzunluk + 1])

# String Bölme (Split)
# Bir stringi belirli bir ayırıcıya göre bölmek için split() metodu kullanılır.
# string i listeye dönüştürme.
cumle = 'okulu_cok_seviyorum'
cumle.split('_')
print(cumle)
sayilar = "1,2,3,4,5,6"
sayilar_dizi = sayilar.split(',')
print(sayilar_dizi)

# String karşılaştırma
# Python'da string karşılaştırması yapmak için birkaç farklı yöntem kullanabilirsiniz. İşte bazı yaygın yöntemler:
# Eşitlik Karşılaştırması (== ve !=):
# == operatörü iki string'in eşit olup olmadığını kontrol eder.
# != operatörü iki string'in eşit olmadığını kontrol eder

str1 = "hello"
str2 = "world"
str3 = "hello"

print(str1 == str2)  # False
print(str1 == str3)  # True
print(str1 != str2)  # True

# Büyük/Küçük Karşılaştırması (<, >, <=, >=):
# Bu operatörler, string'leri alfabetik sıraya göre karşılaştırır.
str1 = "apple"
str2 = "banana"

print(str1 < str2)   # True (alfabetik olarak "apple" önce gelir)
print(str1 > str2)   # False

# Kısa bi uygulama yapalım.

sifre = 1234
kullanici_adi = "Semih"
K_giris = input("Kullanici adinizi giriniz > ")
if K_giris == kullanici_adi:
    K_sifre = int(input("Sifrenizi giriniz > "))
    if K_sifre == sifre:
        print("Hosgeldinizzzzz.")
    else:
        print("Sifre hataliii")
else:
    print("Kullanici adi hataliii")

# String bir ifadeyi tersten yazdıralım.

def ters_cevir(string):
    return ''.join(reversed(string))
# .joindenönceki parantezin içine ne koyarsak her harfin arasına onu yazacaktır.

# Örnek kullanım
orijinal = "Merhaba Dünya"
ters = ters_cevir(orijinal)

print(ters)

# Şimdi verilen string yazıda büyük yazılanlar ile küçük yazılanları değiştirelim.
# Buna swapcase() Yöntemi diyoruz.
def buyuk_kucuk_degistir(string):
    return string.swapcase()

# Örnek kullanım
orijinal = "Merhaba Dünya"
degistirilmis = buyuk_kucuk_degistir(orijinal)

print(degistirilmis)

# Büyük olanları küçültelim.
# lower() Yöntemi:
def buyukleri_kucult(string):
    return string.lower()

# Örnek kullanım
orijinal = "Merhaba Dünya"
degistirilmis = buyukleri_kucult(orijinal)

print(degistirilmis)

# Küçük olanları büyültelim.
# upper() Yöntemi:
def kucukleri_buyult(string):
    return string.upper()

# Örnek kullanım
orijinal = "Merhaba Dünya"
degistirilmis = kucukleri_buyult(orijinal)

print(degistirilmis)

# Şimdi string içerisinde string arayacağız.

text = "Merhaba dünya"
search_string = "dünya"

if search_string in text:
    print(f"'{search_string}' metin içerisinde bulundu.")
else:
    print(f"'{search_string}' metin içerisinde bulunamadi.")
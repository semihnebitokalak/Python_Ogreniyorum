# Bu dersimizde döngüleri detaylı bir şekilde inceleyeceğiz.
# Döngülerde liste kavramını da göreceğimiz için liste kavramına hafif bir giriş yapacağız.
"""
Python'da listeler, sirali ve değiştirilebilir veri yapilaridir. 
Listeler, çeşitli veri tiplerini saklayabilir ve indekslenmiş bir yapiya sahiptirler. Listeler köşeli parantezler [] ile tanimlanir.
"""
# Bir liste tanımlayalım
meyveler = ["Elma", "Muz", "Çilek"]

# Listeyi ekrana yazdıralım
print(meyveler)

# Bir integer liste tanımlayalım
sayilar = [1, 2, 3, 4, 5]

# Liste elemanlarını yazdıralım
print("Birinci eleman:", sayilar[0])  # 1
print("Üçüncü eleman:", sayilar[2])  # 3
print("Son eleman:", sayilar[-1])    # 5
# len fonksiyonu dizinin uzunluğunu bulmamızı sağlar.
# Dizilerde index numarası sıfırdan başladığı için son elemana dizi uzunluğu - 1 yaparak ulaşabiliriz.
uzunluk = len(sayilar)
print("Son eleman:", sayilar[uzunluk-1])    # 5
# in / not in operatörleri neyi sağlar ona bakalım.
# in / not in operatörleri dizideki elemanın varlığını sorgular ve true veya false değeri döndürür.
print("Elma"in meyveler)
print(1 in sayilar)
isimler = ["Ali","Mehmet","Semih","Nebi","Yusuf"]
isimler2 = ["Hamza","Ahmet","Enes"]
isim = input("Isminizi giriniz...")
if isim == "Ali":
    masaNo = 1
if isim == "Mehmet":
    masaNo = 2
if isim == "Semih":
    masaNo = 3
if isim == "Enes":
    masaNo = 4
if isim == "Hamza":
    masaNo = 5
if isim == "Yusuf":
    masaNo = 6
if isim == "Nebi":
    masaNo = 7
if isim in isimler:
    print(masaNo,"Numarali Masada Isminiz listede bulunmaktadir.")
elif isim in isimler2:
    print("Rezervasyonunuz yarin için alinmistir")
elif isim not in isimler and isim not in isimler2:
    print("Isminiz listede bulunmamaktadir.")
# Ayrıca kısa bir bilgi olarak şunu söylemeliyim...
# Python dili büyük küçük harflere duyarsızdır yani verilen değişkenleri ve isimleri çağırırken karşılaştırma yaparken
# yazım kurallarına dikkat etmeliyiz.

# Bir liste tanımlayalım
renkler = ["Kirmizi", "Yeşil", "Mavi"]

# Liste içinde bir öğe olup olmadığını kontrol edelim
print("Kirmizi" in renkler)  # True
print("Sari" in renkler)     # False

# Bir liste tanımlayalım
sayilar1 = [1, 2, 3, 4, 5]

# Liste içinde birden fazla öğe olup olmadığını kontrol edelim
print(3 in sayilar1)  # True
print(7 in sayilar1)  # False


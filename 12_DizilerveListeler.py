# Dizi(array): Aynı türden elemanların oluşturduğu sıralı objelerdir.
# sayiDizisi = 1    17  8   9   10
# karakterDizisi = T    S   F   W gibi örnek verilebilir.
# Python'da temel veri yapıları olarak diziler bulunmaz
# ancak benzer işlevselliği sağlamak için array modülü veya NumPy gibi kütüphaneler kullanılabilir.
# Listeler (Lists)
# Listeler, Python'da en yaygın kullanılan veri yapılarından biridir. 
# Farklı veri türlerini içerebilirler ve değiştirilebilirler (mutable), yani oluşturulduktan sonra içerikleri değiştirilebilir.

liste = ["Ali", 21,'B']
isim_liste = ["Semih","Nebi","Emir","Melih","Cumhur","Mesut"]
char_liste = ['+', '-', '/', '%', '*']
sayi_liste = [1,2,3,4,5,6,7,8,9]
bos_liste = []
kar_liste = [12,'+',"Semih","Ra"]
print(liste)
print(isim_liste)
print(char_liste)
print(sayi_liste)
print(bos_liste)
print(kar_liste)

# Liste Elemanlarına Erişim
# Listelerdeki elemanlara indeksleri kullanarak erişilir:

liste = [1, 2, 3, "a", "b", "c"]

# İlk elemana erişim
print(liste[0])  # Çıktı: 1

# Son elemana erişim
print(liste[-1])  # Çıktı: c

# Bir aralıktaki elemanlara erişim
print(liste[1:4])  # Çıktı: [2, 3, 'a']

# Listedeki elemanın kaçıncı indexte olduğunu nasıl bulacağız.
# list.index(element, start, end)
# element: Bulunacak öğe.
# start (isteğe bağlı): Aramaya başlanacak indeks. Varsayılan olarak 0.
# end (isteğe bağlı): Aramanın sona ereceği indeks. Varsayılan olarak listenin sonu.

liste = [10,20,30,40,50]
# 30 sayısının index ini bulalım.
index = liste.index(30)
print(index)

# Liste dilimleme nedir nasıl yapılır ona bakalım. Dilimleme Söz Dizimi
# list[start:stop:step]
# start: Dilimlemenin başlayacağı indeks (dahil).
# stop: Dilimlemenin biteceği indeks (hariç).
# step: Dilimleme işlemi sırasında atlanacak adım sayısı (isteğe bağlı, varsayılan olarak 1).

liste = [0,1,2,3,4,5,6,7,8,9]
# 2. indeksten başlayıp 5. indekse kadar olan elemanlar
print(liste[2:5])
# şu şekilde de yapabiliriz.
dilim = liste[4:8]
print(dilim)
# Önceki derslerimizde zaten bunu göstermiştik tekrar etmiş olduk.

# Listeye Eleman Ekleme
liste = [0,1,2,3,4,5]

# append metodu : Bu metod, listeye tek bir eleman ekler. Eleman, listenin sonuna eklenir.
liste.append(10)
print(liste)  # Çıktı: [1, 2, 3, 4, 5, 10]

# extend() Metodu : Bu metod, bir listeyi başka bir listeyle genişletir. 
# Başka bir liste veya iterable (iterasyon yapılabilir) nesne alır ve her bir elemanı mevcut listenin sonuna ekler.
liste.extend([7,8,9])
print(liste)
# insert() Metodu : Bu metod, belirli bir indekse tek bir eleman ekler. İki argüman alır: indeks ve eklemek istediğiniz eleman.
liste1 = [1,2,3,4,5]
liste1.insert(2, 10.3)
print(liste1)

# Pekiştirmek için hemen örnek yapalım.
# Bu örneğimizde kullanıcıdan 5 tane int sayı alıp listeye atadıktan sonra ekrana yazdıralım
# önce boş bir liste oluşturalım.
Bos_List = []
for i in range(0,5):
    sayi = int(input("Lütfen 5 adet integer sayi giriniz >"))
    Bos_List.append(sayi)
    
for i in range(0,5):
    print("Bos listedeki indis numarasi [",i,"]","ve degeri > ",Bos_List[i])
    
# Şimdi liste uzunluğu bulma ve girilen elemanın kaç kere tekrar ettiğini ekrana yazdıralım.

liste2 = [5,8,7,6,9,10,"Semih","/","Nebi",44,33,6]
uzunluk = len(liste2)
print(uzunluk)
# Aşağıdaki kodda listede var olan elemanın kaç kere tekrar ettiğini bulacağız.
istenilen_eleman = liste2.count(6)
print(istenilen_eleman)

# Listedeki max ve min değerleri bulalım.
L = [45,24,76,88,99,124,678,456,321]
en_buyuk = max(L)
print(en_buyuk)
en_kucuk = min(L)
print(en_kucuk)

# String bir ifadeyi listeye dönüştürme.
str1 = "BTKAKADEMİ"
L = []
L = list(str1)
print(L)
sayac = L.count("A")
print(sayac)

# Listede eleman arama
my_list = [1, 2, 3, 4, 5]
element = 3

if element in my_list:
    print(f"{element} listede bulunuyor.")
else:
    print(f"{element} listede bulunmuyor.")

# sort() metodu elemanları küçükten büyüğe sıralar.
my_list = [5, 2, 9, 1, 5, 6]
my_list.sort()
print("Siralanmiş liste:", my_list)

# enumerate fonksiyonu nedir nasıl kullanılır?
# enumerate() Kullanımı
# enumerate() fonksiyonu iki parametre alabilir:

# iterable: Üzerinde gezilecek olan iteratör.
# start: İsteğe bağlı, saymaya başlanacak başlangıç değeri (varsayılan olarak 0'dır).
gun = ["pazartesi","sali","carsamba","persembe","cuma","cumartesi","pazar"]
# enumerate genelde for ile beraber kullanılır.
for i, deger in enumerate(gun):
    print(str(i+1) + ".gün", deger)

    
my_list = ['elma', 'armut', 'çilek']
for index, value in enumerate(my_list):
    print(index, value)
# Çıktı:
# 0 elma
# 1 armut
# 2 çilek

my_list = ['elma', 'armut', 'çilek']

for index, value in enumerate(my_list, start=1):
    print(index, value)

# Yığın Oluşturma ve Kullanımı
# Python listelerini kullanarak yığın oluşturabiliriz.
stack = []
# Yığına Eleman Ekleme (Push) append() ile ekliyoruz.

stack.append(4)
stack.append(17)
stack.append(99)
stack.append(33)
stack.append(7)
print(stack)
    
# Yığından Eleman Çıkarma (Pop)
# pop() metodu kullanılarak yığından eleman çıkarılır.
stack.pop()
print("Yiğindan bir eleman çikardiktan sonra:", stack)
# stack den eleman silerken son eklediğimiz elemandan yani en üstte kalan elemandan itibaren silmeye başlar.
# pop ile istenilen indisteki değeri de silebiliz. stack.pop(2) gibi.



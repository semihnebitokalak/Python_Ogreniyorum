# Bu dersimizde range fonksiyonunu anlamaya çalışalım.
for i in range(0,6):
    print(i)
# range fonksiyonunun genel kullanım şekli budur.
# ekrana çıkan çıktı 0'dan 6'ya kadar olarak karşımıza çıkar.

# 0'dan 5'e kadar (5 hariç) olan sayıları üretir
for i in range(5):
    print(i)

# 2'den 7'ye kadar (7 hariç) olan sayıları üretir
for i in range(2, 7):
    print(i)
# Eğer 2 şer veyahut 3 er yazmak istersek şöyle kullanıyoruz.
# 1'den 10'a kadar olan sayıları 2'şer 2'şer üretir (10 hariç)
for i in range(1, 10, 2):
    print(i)

# 5'ten 0'a kadar olan sayıları geriye doğru üretir
for i in range(5, -1, -1):
    print(i)

# Aşağıdaki şekilde de yazabiliriz fakat range bizim işimizi çok daha kolaylaştırıyor.
for a in[0,1,2,3,4,5]:
    print(a)
    
# Peki ya range i listeleyebilir miyiz diye sorarsanız eğer evet listeye dönüştürebiliriz.
# Range nesnesini listeye dönüştürelim
liste = list(range(5))
print(liste)

# 5 kere "Merhaba!" yazdırma
for _ in range(5):
    print("Merhaba!")


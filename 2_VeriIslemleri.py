# Bu dersimizde kullanıcıdan veri alma ve yazma işlemlerini göreceğiz.
# Elimizde bir A değişkeni var ve bunu çeşitli şekilde ekrana yazıcaz.

A = 5
print('A.:',A )
print("A = {0}".format(A))
print(f"A = {A}")
print('A = '+str(A))

# Kullanıcıdan veri alma
isim = input("Adinizi girin: ")
yas = int(input("Yaşinizi girin: "))

# Ekrana yazdırma
print(f"Merhaba, {isim}. Yaşiniz {yas}.")
# print("Merhaba, {}. Yaşınız {}.".format(isim, yas)) bu şekilde de yazabiliriz.

# Kullanıcıdan iki sayıyı alma
sayi1 = float(input("Birinci sayiyi girin: "))
sayi2 = float(input("İkinci sayiyi girin: "))

# Sayıların toplamını hesaplama ve ekrana yazdırma
toplam = sayi1 + sayi2
print("Toplam: {:.2f}".format(toplam))  # .2f ile 2 ondalık basamak gösterilir
print(f"Toplam: {toplam:.2f}")



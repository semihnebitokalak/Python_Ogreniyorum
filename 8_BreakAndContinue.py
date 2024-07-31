# Bu dersimizde break ve continue kavramlarını inceleyeceğiz...
# Önceki dersimizde while döngüsünü öğrenmiştik.
# Şimdi sonsuz döngü oluşturacağız.
# Bir sonsuz döngü, koşul her zaman doğru olduğu için (örneğin, while True:) durmaksızın çalışır.
# Bu tür döngülerde "break" ifadesi ile döngüyü sonlandırmak önemlidir.
# Önceki dersimizde yaptığımız örneğimizi tekrar yapalım.
# break Komutu
# break komutu, döngüyü tamamen sonlandırmak için kullanılır. 
# break komutu çalıştırıldığında, döngü anında durdurulur ve döngüden sonraki kod çalıştırılmaya devam edilir.
print("Programdan cikmak icin 0 a basiniz...")
while True:
    d = int(input("Lütfen bir sayi giriniz..."))
    print("Girilen sayinin karesi : ",d*d)
    if d == 0:
        break # döngüden çık anlamına gelir.
    
# 1'den 10'a kadar olan sayılar içinde 5'i bulunca döngüyü sonlandırır
for i in range(1, 11):
    if i == 5:
        break
    print(i)
print("Döngü sonlandi")

# continue Komutu
# continue komutu, döngünün o anki iterasyonunu atlayarak bir sonraki iterasyona geçmek için kullanılır.
# continue komutu çalıştırıldığında, döngü içindeki kalan kodlar atlanır ve döngünün bir sonraki iterasyonu başlar.
# 0 dan 100 e kadar 7 nin katları hariç diğer sayıları ekrana yazdıran programı yazınız.

for i in range(100):
    if i % 7 == 0:
        continue
    print(i)
z = 0
while z < 100:
    z += 1
    if z % 7 == 0:
        continue
    print(z)

# break ve continue Kullanımının Dikkat Edilmesi Gereken Noktaları
# break komutu döngüyü tamamen sonlandırırken, continue komutu yalnızca o anki iterasyonu atlar.
# break komutu döngüden tamamen çıkarken, continue komutu döngünün başına geri döner ve bir sonraki iterasyona geçer.
# break ve continue komutlarını doğru kullanmak, döngülerin akışını kontrol etmek için önemlidir ve hatalı kullanımı,
# beklenmeyen sonuçlara yol açabilir.
    

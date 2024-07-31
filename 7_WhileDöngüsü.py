# Bu dersimizde while döngüsüne dair bilgileri öğreneceğiz...
"""
while döngüsü, bir koşul doğru olduğu sürece bir kod bloğunu tekrar tekrar çaliştirmak için kullanilir. 
for döngüsünden farkli olarak, while döngüsü belirli bir sayida değil, belirtilen koşul sağlandiği sürece çalişir.
"""
# Basit Bir while Döngüsü Yapalım
x = 1
while x <= 5:
    print(x)
    x += 1

# Klavyeden 0 girildiği zaman programı bitiren bir kod örneği yazalım...
print("Programi bitirmek icin '0' a basiniz...")
a = 1
while a != 0:
    a = int(input("Lütfen karesini almak istediginiz sayiyi giriniz..:"))
    print("Sayinin karesi : ",a*a)
print("Program kapatilmistir...")

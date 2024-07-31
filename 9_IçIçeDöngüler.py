# Bu dersimizde iç içe döngü nedir onu öğreneceğiz.
# Çarpım tablosu örneği çözeceğiz.
# Bu yapılar, genellikle çok boyutlu veri yapılarını işlemek veya karmaşık tekrar gereksinimlerini karşılamak için kullanılır.
# İç içe döngüler, özellikle matrisler gibi iki boyutlu veri yapılarını işlemek için yaygındır.
# Bir döngü içinde başka bir döngü yer aldığında, iç döngü her dış döngünün her bir iterasyonu için tamamen çalıştırılır.
# Örneğin, bir for döngüsünü başka bir for döngüsünün içinde kullanarak iç içe döngü yapısı oluşturabilirsiniz.

for i in range(3):  # Dış döngü: satırlar
    for j in range(3):  # İç döngü: sütunlar
        print(f"({i}, {j})", end=" ")
    print()  # Her satırın sonunda yeni bir satır ekler

# Çarpım tablosunu yapalım.
for i in range(1,11):
    for j in range(1,11):
        print(i,"*",j,"=",i*j)
    print("\n")
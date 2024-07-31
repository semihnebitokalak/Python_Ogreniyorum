# Bu dersimizde koşul ve karşılaşmaya dair her şeyi öğrenceğiz.
# Karşılaştırma yaparken kullanacağımız yapılara dikkat etmeliyiz. Mesela tek eşittir koyarsak ona değer atarız karşılaştırma yapmayız.
# Basit bir if yapısı oluşturduk.
age = int(input("Yaşinizi girin: "))

if age >= 18:
    print("Reşitsiniz.")
# Şimdi if else if ve else yapılarının olduğu bir örnek yapalım.
agee = int(input("Yaşinizi girin: "))

if agee < 18:
    print("Reşit değilsiniz.")
elif agee == 18:
    print("Tam reşit yaşindasiniz.")
else:
    print("Reşitsiniz.")

# Şimdi de karşılaştırma operatörlerine dair örnek yapalım.
number1 = int(input("Birinci sayiyi girin: "))
number2 = int(input("İkinci sayiyi girin: "))

if number1 > number2:
    print(f"{number1} sayisi {number2} sayisindan büyüktür.")
elif number1 < number2:
    print(f"{number1} sayisi {number2} sayisindan küçüktür.")
else:
    print(f"{number1} sayisi {number2} sayisina eşittir.")

# Şimdi de birden fazla koşullu örnek yapalım ve inceleyelim.
score = int(input("Puaninizi girin: "))

if score >= 90:
    print("Notunuz: A")
elif score >= 80:
    print("Notunuz: B")
elif score >= 70:
    print("Notunuz: C")
elif score >= 60:
    print("Notunuz: D")
else:
    print("Notunuz: F")
    
# Şimdi "or","and" ve "not" ifadelerini örneklerle açıklayacağız.
# and operatörü
ageee = 25
income = 50000

if ageee> 18 and income > 30000:
    print("Hem reşitsiniz hem de geliriniz yüksek.")
else:
    print("Koşullar sağlanmadi.")

# or operatörü
age1 = 17
income = 40000

if age1 > 18 or income > 30000:
    print("En az bir koşul sağlaniyor.")
else:
    print("Hiçbir koşul sağlanmadi.")

# not operatörü
is_student = False

if not is_student:
    print("Öğrenci değilsiniz.")
else:
    print("Öğrencisiniz.")

# karmaşık bir örnek

age2 = 20
income1 = 25000
is_student1 = True

if (age2 > 18 and income1 > 30000) or not is_student1:
    print("Bu koşullar sağlaniyor.")
else:
    print("Koşullar sağlanmiyor.")

# Sayı tahmin etme
a = 25
b = int(input("Sayiyi tahmin et :"))
if a == b:
    print("Dogru bildiniz...")
else:
    print("Yanlis bildiniz...")

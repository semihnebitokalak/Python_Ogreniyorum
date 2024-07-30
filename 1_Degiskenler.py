# Değişken oluşturma ve değer atama
x = 10
y = 20.5
name = "John"
is_student = True

# Değerleri ekrana yazdırma
print(x)           # 10
print(y)           # 20.5
print(name)        # John
print(is_student)  # True

# Değişken İsimlendirme Kuralları
# Python'da değişken isimlendirirken bazı kurallara dikkat etmek gerekir:
# Değişken isimleri harf veya alt çizgi (_) ile başlamalıdır.
# Değişken isimleri harfler, rakamlar ve alt çizgi içerebilir, ancak rakamla başlayamaz.
# Büyük/küçük harf duyarlıdır (case-sensitive).
# Python'un anahtar kelimeleri değişken ismi olarak kullanılamaz.

# Geçerli değişken isimleri
age = 25
first_name = "Alice"
_lastName = "Doe"
number1 = 100

# Geçersiz değişken isimleri
# 1number = 100  (Rakamla başlayamaz)
# first-name = "Alice"  (Tire (-) içeremez)
# class = "Math"  (Anahtar kelime kullanılamaz)

# Değişkenlere değer atama
a = 5
b = a   # b, a'nın değerini alır

# Değerleri değiştirme
a = 10

# Değerleri ekrana yazdırma
print(a)  # 10
print(b)  # 5

# Özet
# Değişkenlere değer atama
x = 42
y = 3.14
greeting = "Merhaba"
is_active = False

# Değişkenlerin birbirine aktarılması
a = x
b = y
message = greeting

# Değerleri güncelleme
x = 100
greeting = "Selam"

# Değerleri ekrana yazdırma
print("x:", x)          # 100
print("a:", a)          # 42
print("y:", y)          # 3.14
print("b:", b)          # 3.14
print("greeting:", greeting)  # Selam
print("message:", message)    # Merhaba
print("is_active:", is_active)  # False

# İşlem önceliği örnek çözüm

result = (2 + 3) * 2 ** 2 / 2 - 1
print(result)  # Çıktı: 9.0

# Atanan verinin tipini bulma

num1 = 10
num2 = -5
print(type(num1))  # Çıktı: <class 'int'>
print(type(num2))  # Çıktı: <class 'int'>

pi = 3.14
gravity = 9.81
print(type(pi))  # Çıktı: <class 'float'>
print(type(gravity))  # Çıktı: <class 'float'>

greeting = "Hello, World!"
name = 'Alice'
print(type(greeting))  # Çıktı: <class 'str'>
print(type(name))  # Çıktı: <class 'str'>

is_sunny = True
is_raining = False
print(type(is_sunny))  # Çıktı: <class 'bool'>
print(type(is_raining))  # Çıktı: <class 'bool'>

# Veri tipleri dönüşümleri nasıl yapılır

# Metinden tam sayıya dönüştürme
number_str = "123"
number_int = int(number_str)
print(number_int)  # Çıktı: 123
print(type(number_int))  # Çıktı: <class 'int'>

# Kayan noktadan tam sayıya dönüştürme
number_float = 123.45
number_int = int(number_float)
print(number_int)  # Çıktı: 123
print(type(number_int))  # Çıktı: <class 'int'>

# Metinden kayan nokta sayıya dönüştürme
number_str = "123.45"
number_float = float(number_str)
print(number_float)  # Çıktı: 123.45
print(type(number_float))  # Çıktı: <class 'float'>

# Tam sayıdan kayan nokta sayıya dönüştürme
number_int = 123
number_float = float(number_int)
print(number_float)  # Çıktı: 123.0
print(type(number_float))  # Çıktı: <class 'float'>

# Tam sayıdan metne dönüştürme
number_int = 123
number_str = str(number_int)
print(number_str)  # Çıktı: "123"
print(type(number_str))  # Çıktı: <class 'str'>

# Kayan noktadan metne dönüştürme
number_float = 123.45
number_str = str(number_float)
print(number_str)  # Çıktı: "123.45"
print(type(number_str))  # Çıktı: <class 'str'>

# Tam sayıdan boolean'a dönüştürme
number_int = 0
boolean_value = bool(number_int)
print(boolean_value)  # Çıktı: False
print(type(boolean_value))  # Çıktı: <class 'bool'>

number_int = 1
boolean_value = bool(number_int)
print(boolean_value)  # Çıktı: True
print(type(boolean_value))  # Çıktı: <class 'bool'>

# Metinden boolean'a dönüştürme
text = ""
boolean_value = bool(text)
print(boolean_value)  # Çıktı: False
print(type(boolean_value))  # Çıktı: <class 'bool'>

text = "Hello"
boolean_value = bool(text)
print(boolean_value)  # Çıktı: True
print(type(boolean_value))  # Çıktı: <class 'bool'>

# Veri tipi dönüşümleri, özellikle kullanıcı girdilerini doğru veri tipine dönüştürmek için kullanışlıdır.
# Dönüştürmeye çalıştığınız veri tipinin uygun olup olmadığını kontrol edin. Örneğin, bir metni 
# tam sayıya dönüştürmeye çalışırken metin yalnızca rakamlardan oluşmalıdır; aksi halde hata alırsınız.

# Hatalı dönüşüm, "abc" tam sayıya dönüştürülemez
text = "abc"
try:
    number = int(text)
except ValueError as e:
    print(f"Dönüşüm hatasi: {e}")  # Çıktı: Dönüşüm hatası: invalid literal for int() with base 10: 'abc'

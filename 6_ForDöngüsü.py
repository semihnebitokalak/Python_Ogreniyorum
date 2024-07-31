# Bu dersimizde for yapısını ve range ile beraber kullanımını inceleyeceğiz.
# 1 den 30 a kadar olan tek sayıları ekrana birkaç şekilde yazalım...

for i in range(1,30,2):
    print(i)
    
for i in range(1,30):
    if i % 2 == 0:
        continue
    else:
        print(i)
    
for i in range(10, 0, -2):  # 10'dan 2'şer 2'şer geriye doğru
    print(i)

for i in range(1, 6):  # 1'den 5'e kadar olan sayılar range içine giriyor.
    print(i * 2) # değerler 2 ile çarpılıp ekrana yazdırılıyor.

for i in range(3):
    for j in range(3):
        print(f"({i},{j})", end = " ") # end ne işe yarıyor?
        # end yazılacak ifadelerin arasına konulacak ifadeyi simgeler.
        
# end' in kullanımına örnekler verelim
print("Merhaba")
print("Dünya")
"""
Çikti;
Merhaba
Dünya
"""

print("Merhaba", end=" ")
print("Dünya")
"""
Çikti;
Merhaba Dünya
"""

print("1", end=", ")
print("2", end=", ")
print("3")
"""
Çikti;
1, 2, 3
"""

for i in range(5):
    print(i, end=" ")
"""
Çikti;
0 1 2 3 4 
"""

        
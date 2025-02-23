import numpy as np
# Kitap fiyatları
kitap_fiyatlari = np.array([25, 45, 20, 35, 50, 40, 30])

# Satılan kitap adetleri
satis_adetleri = np.array([100, 150, 200, 120, 130, 80, 110])

# Kitap kategorileri
kategoriler = np.array(["Roman", "Bilim", "Çocuk", "Tarih", "Roman", "Bilim", "Çocuk"])

toplam_gelir = kitap_fiyatlari* satis_adetleri
print("Toplam Gelir : " , kategoriler , '\n' , toplam_gelir  )

ortalama_fiyat = np.mean(kitap_fiyatlari)
max_fiyat = np.max(kitap_fiyatlari)
min_fiyat = np.min(kitap_fiyatlari)

print("Ortalama Fiyat: " , ortalama_fiyat , 'TL' )
print("Max Fiyat: " , max_fiyat, 'TL'  )
print("Min Fiyat: " , min_fiyat , 'TL' )


romanlar = kitap_fiyatlari[kategoriler == "Roman"]
print('Roman fiyatları :', romanlar)
roman_satislari = satis_adetleri[kategoriler == "Roman"]
print('Roman Satis :', roman_satislari)
roman_toplam_satis = np.sum(romanlar * roman_satislari)
print('Roman Satis :', roman_toplam_satis ,'TL')


veri = np.array([kitap_fiyatlari, satis_adetleri])
veri_reshaped = np.reshape(veri,(2,7))


print(veri_reshaped)


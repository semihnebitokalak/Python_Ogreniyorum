import pandas as pd

# excel dosyasını oku
df = pd.read_excel('/Users/semihnebitokalak/Desktop/Desktop_2/Pyhton Öğreniyorum/Pandas/teknolojik_urunler.xlsx')

# ilk bir kaç satırı oku
# print(df.head())

# ortalama_fiyat = df['Fiyat (TL)'].mean()
# print(f"Ortalama Fiyat : {ortalama_fiyat} TL")

#en cok gelir getiren ürünü sırala

kategori_bazlı_satis = df.groupby('Kategori')['Satış'].sum()
print(f"{kategori_bazlı_satis}")

#En cok gelir getiren ürünü bulma
max_gelir = df.loc[df['Toplam Fiyat (TL)'].idxmax()]
print(f"En çok gelir getiren ürün : {max_gelir}")

#belli bir fiyat üstünü cek

# fiyat_ust_urunler = df[df['Fiyat (TL)'] > 4000]
# print('Fiyatı 4000 TL nin üzerinde olan ürünler :')
# print(fiyat_ust_urunler)

# fiyat_ust_urunler.to_excel('fiyatı_4000_üstü_olanlar.xlsx', index=False)


# ürün_adi = df['Ürün Adı'] 

# print(ürün_adi)
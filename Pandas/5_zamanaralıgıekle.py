import pandas as pd
import numpy as  np
#excel dosyasını oku
df = pd.read_excel('/Users/semihnebitokalak/Desktop/Desktop_2/Pyhton Öğreniyorum/Pandas/teknolojik_urunler.xlsx')
#rastegele tarih damgaları oluşturma 
df['Tarih'] = pd.to_datetime(np.random.choice(pd.date_range('2024-01-01','2024-12-31'), size=len(df)))
#gör

print(df[['Ürün Adı','Tarih']])



df.to_excel('/Users/semihnebitokalak/Desktop/Desktop_2/Pyhton Öğreniyorum/Pandas/teknolojik_urunler.xlsx', index=False)
print('Veri Dosyaya Aktarıldı')


import pandas as pd
import numpy as np

# Excel dosyasını oku
df = pd.read_excel('/Users/semihnebitokalak/Desktop/Desktop_2/Pyhton Öğreniyorum/Pandas/teknolojik_urunler.xlsx')

df['Tarih'] = pd.to_datetime(df['Tarih'])
print(df.head())



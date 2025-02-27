import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#veriyi hazırlama

data = {
    'Ev_Buyuklugu':[120, 250, 175, 300, 220],
    'Fiyat':[2400000, 5000000, 3500000, 6000000, 4400000]
}


df = pd.DataFrame(data) # veriyi df çevirme

X = df[['Ev_Buyuklugu']] #girdi burada iki köşeli parantez koymamızın sebebi girdiye göre sonuçlar üreteceğimiz için girdinin neye bağlı olduğunu belirtmek için kullandık. Yani X girdi olacak ve bu girdi ev büyüklüğüne bağlı olacak.
y = df['Fiyat'] # cıktı

X_train, X_test, y_train, y_test = train_test_split(X,y , test_size=0.2, random_state=42)

#modeli oluştur

model = LinearRegression()
model.fit(X_train,  y_train)

# y_pred = model.predict(X_test)
#hata ne kadar küçükse tahmin o kadar iyidir.
# mse = mean_squared_error(y_test , y_pred)
# rmse = np.sqrt(mse)
# print(f"Ortalama Kare Hatası (MSE){rmse}")

ev_buyuklugu = float(input("Lütfen evin büyüklüğünü (m²) girin :"))
ev_buyuklugu_df = pd.DataFrame([[ev_buyuklugu]], columns=['Ev_Buyuklugu'])

tahmini_fiyat = model.predict(ev_buyuklugu_df)

print(f"Bu evin tahmini fiyatı : {tahmini_fiyat[0]:.2f} TL")


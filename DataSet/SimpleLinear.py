# Import libraries
import pandas as pd              # Veri işleme için pandas kütüphanesini import eder
import numpy as np               # Sayısal işlemler için numpy kütüphanesini import eder
import matplotlib.pyplot as plt   # Grafik çizmek için matplotlib'in pyplot modülünü import eder
import seaborn as sns            # Estetik grafikler için seaborn kütüphanesini import eder
from sklearn.model_selection import train_test_split  # Veriyi eğitim ve test setlerine ayırmak için train_test_split fonksiyonunu import eder
from sklearn.linear_model import LinearRegression     # Lineer regresyon modelini import eder

# Veri Setini Yükleme
df_sal = pd.read_csv('/Users/semihnebitokalak/Desktop/Desktop/Pyhton Öğreniyorum/DataSet/Salary_Data.csv')  # CSV dosyasını pandas ile okur
df_sal.head()  # Veri setinin ilk 5 satırını gösterir (veri hakkında ilk izlenimi almanızı sağlar)

# Veriyi Tanıma
df_sal.describe()  # Veri setinin sayısal özetini (ortalama, std, min, max) verir

# Maaş Dağılımını Görselleştirme
plt.title('Salary Distribution Plot')  # Grafik başlığını belirler
sns.distplot(df_sal['Salary'])  # Maaş dağılımını histogram ile çizer
plt.show()  # Grafiği gösterir

# Maaş ve Deneyim Arasındaki İlişkiyi Görselleştirme
plt.scatter(df_sal['YearsExperience'], df_sal['Salary'], color = 'lightcoral')  # Deneyim yılı ve maaş arasındaki ilişkiyi scatter plot ile çizer
plt.title('Salary vs Experience')  # Grafik başlığını belirler
plt.xlabel('Years of Experience')  # X ekseni etiketi
plt.ylabel('Salary')  # Y ekseni etiketi
plt.box(False)  # Grafik kutu çizgilerini kaldırır
plt.show()  # Grafiği gösterir

# Bağımsız (X) ve Bağımlı (y) Değişkenleri Ayırma
X = df_sal.iloc[:, :1]  # Bağımsız değişken (Deneyim Yılı)
y = df_sal.iloc[:, 1:]  # Bağımlı değişken (Maaş)

# Eğitim ve Test Setlerine Veriyi Ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)  # Veriyi eğitim (%80) ve test (%20) setlerine ayırır

# Lineer Regresyon Modelini Oluşturma
regressor = LinearRegression()  # Lineer regresyon modelini başlatır
regressor.fit(X_train, y_train)  # Modeli eğitim seti üzerinde eğitir

# Eğitim ve Test Seti Üzerinden Tahmin Yapma
y_pred_test = regressor.predict(X_test)  # Test seti için tahmin yapar
y_pred_train = regressor.predict(X_train)  # Eğitim seti için tahmin yapar

# Eğitim Seti Üzerindeki Tahminlerin Görselleştirilmesi
plt.scatter(X_train, y_train, color = 'lightcoral')  # Eğitim setinin gerçek verisini scatter plot ile çizer
plt.plot(X_train, y_pred_train, color = 'firebrick')  # Eğitim seti üzerindeki tahmin edilen maaşları çizgi ile gösterir
plt.title('Salary vs Experience (Training Set)')  # Grafik başlığını belirler
plt.xlabel('Years of Experience')  # X ekseni etiketi
plt.ylabel('Salary')  # Y ekseni etiketi
plt.legend(['X_train/Pred(y_test)', 'X_train/y_train'], title = 'Sal/Exp', loc='best', facecolor='white')  # Grafik üzerine açıklama ekler
plt.box(False)  # Grafik kutu çizgilerini kaldırır
plt.show()  # Grafiği gösterir

# Test Seti Üzerindeki Tahminlerin Görselleştirilmesi
plt.scatter(X_test, y_test, color = 'lightcoral')  # Test setinin gerçek verisini scatter plot ile çizer
plt.plot(X_train, y_pred_train, color = 'firebrick')  # Eğitim setindeki regresyon doğrusu ile tahmin edilen maaşları çizer
plt.title('Salary vs Experience (Test Set)')  # Grafik başlığını belirler
plt.xlabel('Years of Experience')  # X ekseni etiketi
plt.ylabel('Salary')  # Y ekseni etiketi
plt.legend(['X_train/Pred(y_test)', 'X_train/y_train'], title = 'Sal/Exp', loc='best', facecolor='white')  # Grafik üzerine açıklama ekler
plt.box(False)  # Grafik kutu çizgilerini kaldırır
plt.show()  # Grafiği gösterir

# Regresyon Modelinin Katsayıları ve Kesiti
print(f'Coefficient: {regressor.coef_}')  # Modelin katsayısını yazdırır (deneyim yılı başına maaş artışı)
print(f'Intercept: {regressor.intercept_}')  # Modelin kesitini yazdırır (deneyim sıfırken maaş)

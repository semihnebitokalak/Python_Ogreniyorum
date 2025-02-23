import numpy as np 

dizi1 = np.array([1,2,3,5,14])
dizi2 = np.array([3,4,12,5])

# toplam = dizi1 + dizi2
# cikarma = dizi1 - dizi2
# carpma = dizi1 * dizi2
# bölme = dizi1 / dizi2
# print("Toplam",toplam)
# print("Fark",cikarma)
# print("Çarp",carpma)
# print("Bölüm",bölme)

# TOPLAMA FONKSİYONU
toplam = np.sum(dizi1)
carpim = np.prod(dizi1)
kareal = np.sqrt(dizi1)
# ARİTMATİK ORTALAMA ALMA
ortalama = np.mean(dizi1)
# MEDYAN
medyanal = np.median(dizi1)
# STANDART SAPMA
standartsapma = np.std(dizi1)
print(standartsapma)
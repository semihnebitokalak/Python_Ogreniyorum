import numpy as np

dizi = np.array([1,2,3,4,56])
# min = np.min(dizi)
# maks = np.max(dizi)
# print("---------------------------------------------------")
# print("Dizi içerisinde en düşük değere sahip veri :" , min)
# print("---------------------------------------------------")
# print("Dizi içerisinde en yüksek değere sahip veri :" , maks)
# print("---------------------------------------------------")

toplam = np.sum(dizi)
kume_toplam = np.cumsum(dizi)
# Verimizi bir önceki değer ile toplayıp günceller.
print(kume_toplam)
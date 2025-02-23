import numpy as np

dizi = np.array([10,20,30,40,50,68,98,74,25,11,33])
# boolean_mask = dizi > 50
# print(boolean_mask)

#boolean maskeyi kullanarak dizideki elemanları seçme
# secilmis = dizi[boolean_mask]
# print("50'den büyük olan elemanlar : " , secilmis )
#coklu eleme
boolean_mask = (dizi > 30) & (dizi <70) & (dizi >10)
print("30 ile 70 arasındaki elemanlar :", dizi[boolean_mask])
import numpy as np

dizi1 = np.array([1, 2, 3])
dizi2 = np.array([4, 5, 6])

birlesik_dizi = np.concatenate((dizi1,dizi2))

print("Diziler birleştirildi :", birlesik_dizi)

# iki boyutlu dizi birleştirme
dizi1 = np.array([[1,2,3],[4,5,6]])
dizi2 = np.array([[7,8,9],[10,11,12]])
# Üç boyutlu için vstack kullanılır.
birlesik_dizi = np.vstack((dizi1,dizi2))
# İki boyutlu için hstack kullanılır.
birlesik_dizi1 = np.hstack((dizi1,dizi2))
print(birlesik_dizi)
print(birlesik_dizi1)
# dizi = np.array([1, 2, 3, 4, 5, 6])
# bd = np.split(dizi,3)
# dizi = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# bd = np.vsplit(dizi,2)
# bd1 = np.hsplit(dizi,2)

# print(bd)
# print(bd1)

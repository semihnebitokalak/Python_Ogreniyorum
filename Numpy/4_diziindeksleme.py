import numpy as np

dizi = np.array([10,20,30,40,50])

# eleman = dizi[2]

# print(eleman)

matris = np.array([[1,2,3],[4,5,6],[7,8,9]])
# eleman = matris[-2,-3]
# matrislerde indis numarası 0 dan başlar buna dikkat etmeliyiz.
eleman = matris[1,1]
print(eleman) # Çıktı 5 verir.

alt_matris = matris[0:3,1:3]

print(alt_matris)


dilim = dizi[0:3]
print("Dilim :", dilim)







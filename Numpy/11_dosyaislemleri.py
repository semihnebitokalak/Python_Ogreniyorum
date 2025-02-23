import numpy as np

data = np.loadtxt('/Users/semihnebitokalak/Desktop/Desktop_2/Pyhton Öğreniyorum/Numpy/data.txt', delimiter=' ')
print(data)
row_sums = np.sum(data , axis=1)
print("Her satırın toplamı :", row_sums)

np.savetxt('/Users/semihnebitokalak/Desktop/Desktop_2/Pyhton Öğreniyorum/Numpy/output_with_sums.txt', row_sums , fmt='%d')

output_data = np.column_stack((data, row_sums))

np.savetxt('/Users/semihnebitokalak/Desktop/Desktop_2/Pyhton Öğreniyorum/Numpy/output_with_sums.txt', output_data, fmt='%d' , delimiter=' ')
print('Kayıt işlemi tamamlandı !')

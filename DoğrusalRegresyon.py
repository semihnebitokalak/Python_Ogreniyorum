import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)

    # mean of x and y vector
    m_x = np.mean(x)
    m_y = np.mean(y)

    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x

    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x

    # Return the coefficients
    return (b_0, b_1)

import numpy as np

import matplotlib.pyplot as plt

def plot_regression_line(x, y, b):
    # Gerçek verileri scatter plot olarak çiz
    plt.scatter(x, y, color="m", marker="o", s=30)

    # Predicted response vector (tahmin edilen y değerleri)
    y_pred = b[0] + b[1]*x

    # Regresyon doğrusunu çiz
    plt.plot(x, y_pred, color="g")

    # Eksen etiketlerini yerleştir
    plt.xlabel('x')
    plt.ylabel('y')

    # Grafiği göster
    plt.show()


# Örnek veriler
x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])

# Regresyon katsayılarını hesaplayalım (b_0, b_1)
b = np.polyfit(x, y, 1)  # b[0] = b_0, b[1] = b_1

# Regresyon doğrusu çiz
plot_regression_line(x, y, b)


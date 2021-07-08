import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('dataset_2017.csv', delimiter=',')

X = data['periode'].values
Y = data['kesiapan'].values

mean_x = np.mean(X.copy())
mean_y = np.mean(Y.copy())

n = len(X)

num = 0
den = 0

for i in range(n):
    num += (X[i] - mean_x) * (Y[i] - mean_y)
    den += (X[i] - mean_x) ** 2
    
b1 = float(num) / float(den)
b0 = mean_y - (b1 * mean_x)

print('Mean Periode ='+ str(mean_x))
print('Mean Kesiapan ='+ str(mean_y))
print(b0, b1)

max_x = np.max(X) + 10
min_x = np.min(X) - 10

x = np.linspace(min_x, max_x, 100)
y = b0 + b1 * x

plt.plot(x, y, label='Linear Regression')
plt.scatter(X, Y, label='Scatter Plot')

plt.xlabel('Periode')
plt.ylabel('Kesiapan')

plt.legend()
plt.show()

y = b0 + b1 * 16
print(y)

ss_t = 0
ss_r = 0

for i in range(n):
    y_pred = b0 + b1 * X[i]
    ss_t += (Y[i] - mean_y) ** 2
    ss_r += (Y[i] - y_pred) ** 2
    
r2 = 1 - (ss_r/ss_t)
print(r2)

# rmse = 0
# for i in range(n):
#     y_pred = b0 + b1 * X[i]
#     rmse += (Y[i] - y_pred) **2
# rmse = np.sqrt(rmse/n)
# print(rmse)

mape = 0
for i in range(n):
    y_pred = b0 + b1 * X[i]
mape = np.mean(np.abs((Y[i] - y_pred)/Y[i]))*100
print(mape)

akurasi = 100 - mape
print(akurasi)
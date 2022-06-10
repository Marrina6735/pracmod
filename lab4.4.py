# Задание 4
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure(figsize=(12,12))
ax = fig.add_subplot()
vals = [42, 2, 3, 7, 45]
labels = ['None','Towards Data Science','Tthe Reality Project','Note','Eng']
ax.pie(vals,labels=labels, autopct='%.1f%%',startangle=90)
plt.legend(loc='upper right')
ax.grid()
ax.set_title(r'Круговая диаграмма')
plt.show()

# 2)
np.random.seed(1968081)
b = 60
k = 25
x = b + k * np.random.randn(447)
num_bins = 60
fig, ax = plt.subplots()
n, bins, patches = ax.hist(x, num_bins, density=True)
y = ((1 / (np.sqrt(2 * np.pi) * k)) *
np.exp(-0.5 * (1 / k * (bins - b))**2))
ax.plot(bins, y, )
ax.set_title(r'Гистограмма')
fig.tight_layout()
plt.show()
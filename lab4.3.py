# Задание 3
import matplotlib.pyplot as plt
import numpy as np
z = np.linspace(-10, -0.5, 51)
x = np.linspace(0.5, 10, 51)
l_1 = (z ** 1 + 2 ** 1) / (z ** 1) # при p = 2, n = 1
l_2 = (z ** 1 + 4 ** 1) / (z ** 1) # при p = 4, n = 1
l_3 = (z ** 2 + 2 ** 2) / (z ** 2) # при p = 2, n = 2
h_1 = (x ** 1 + 2 ** 1) / (x ** 1) # при p = 2, n = 1
h_2 = (x ** 1 + 4 ** 1) / (x ** 1) # при p = 4, n = 1
h_3 = (x ** 2 + 2 ** 2) / (x ** 2) # при p = 2, n = 2
fig, ax = plt.subplots()
ax.plot(z, l_1, color='blue', linestyle=':',label='F(x) при p = 2, n = 1')
ax.plot(z, l_2, color='red', label='F(x) при p = 4, n = 1')
ax.plot(z, l_3, color='green', linestyle='--', label='F(x) при p = 2, n = 2')
ax.plot(x, h_1)
ax.plot(x, h_2)
ax.plot(x, h_3)
plt.grid()
plt.title(r'График функции $f(x) = (x^n + p^n)/(x^n)$, при различных значениях n и p')
plt.legend(loc='lower right')
plt.ylabel('f(x)', fontsize=20)
plt.xlabel('x', fontsize=20)
plt.show()


# Задание 2
# 1)
# 1/1*2 + 1/2*3 + 1/3*4 + ... + 1/n*(n+1) +...= 1 - 1/2 + 1/2 - 1/3 + 1/3 - 1/4 + 1/4 ... + 1/n + 1/(n+1) + ... = 1 + 1/(n+1)
n = int(input()) # номер частичной суммы
print("Частичная сумма при заданном значении n равна ", 1 + 1/(n+1))

# 2)
import math
from math import sqrt
print("Введите точность (эпсилон) ")
e = float(input()) # Точность
s = 0 # сумма
i = 1
a = sqrt(i + 1) / (i * math.exp(i))
while True:
    a = (sqrt(i + 1)) / (i * math.exp(i))
    s += a
    i += 1
    if abs(a) < e:
        i -= 1
        break

print(s)




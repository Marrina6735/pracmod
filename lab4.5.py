# Задание 5
# 1)
'''a = []
n = int(input("квадратная матрица порядка = "))
for i in range (n):
    b = []
    for i in range (n):
        b.append(int(input()))
    a.append(b)
for i in a:
    print(i)
for j in range(n - 1):
    for i in range(n - 1):
        if a[i][j] != a[j][i] and i != j:
            print("Матрица не симметрична")
            break'''

# 2)
a = []
n = int(input()) # строк
m = int(input()) # столбцов
for i in range (n):
    b = []
    for j in range (m):
        b.append(int(input()))
    a.append(b)
for i in a:
    print(i)
max = 0 # максимум
for i in range (n):
    for j in range (m):
        if a[i][j] > max:
            max = a[i][j]
            num_i = i
            num_j = j
a[0], a[num_i] = a[num_i], a[0]
for i in range (n):
        a[i][0], a[i][num_j] = a[i][num_j], a[i][0]
print()
for i in a:
    print(i)


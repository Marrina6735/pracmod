# Задание 6
# 1)
import math
def gipotenuza(kat1, kat2):
    a = kat1 ** 2 + kat2 ** 2
    b = math.sqrt(a)
    return b
print("Катеты первого треуголника 3 и 4")
print("Катеты второго треуголника 9 и 12")
if gipotenuza(3, 4) < gipotenuza(9, 12):
    print("Первая гипотенуза больше")
else:
    print("Вторая гипотенуза больше")
# 2)
s = input("Введите строку ")
s = sorted(s)
print(s)








'''# Контрольные вопросы
S = "s,pa,in"
print(S[2:4])
print(S[2]+S[3])'''
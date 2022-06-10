# Индивидуальное задание 4
# 1)
print("Введите два числа, причем а < b")
a = int(input())
b = int(input())
sum = 0
for i in range(a, b + 1):
    sum += i**2
print(sum)
# 2)
print("Введите первое число последовательности, причем оно обязано быть четным")
n = int(input())
sum = 0
while n % 2 == 0:
    sum += n
    n = int(input())
print(sum)
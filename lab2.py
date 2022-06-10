
# Задание 1
while True:
    print("Введите число ")
    n = int(input())
    if n < 0 or n > 10:
        print("Число неверное, введите число больше 0, но меньше 10 ") ## вводим число повторно
    else:
        break
print(n**2)


# Задание 2
# Медицинская анкета
name = input("Введите Ваше имя ")
surname = input("Введите Вашу фамилию ")
print("Введите Ваш возраст ")
age = int(input())
print("Введите Ваш вес ")
weight = int(input())
if age < 30 and (weight > 50 and weight < 120):
    print("Пациент в хорошем состоянии")
elif age > 30 and (weight < 50 or weight > 120):
    print("Пациенту требуется заняться собой")
elif age > 40 and (weight < 50 or weight > 120):
    print("Пациенту требуется врачебный осмотр")
else:
    print("Пациенту требуются сдать дополнительные анализы для результата")

# Индивидуальное задание (вариант 3)
print("Введите сумму покупки")
sum = int(input())
print ("Сумма покупки с учетом скидки ")
if sum > 1000:
    sum = sum * 0.95
    print(sum)
elif sum > 500:
    sum = sum * 0.97
    print(sum)
else:
    print(sum)

# Индивидуальное задание 4
# 1)
print("Введите два числа, причем а<b")
a = int(input())
b = int(input())
sum = 0
for i in range (a, b + 1):
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

# Контрольные вопросы
a = int(input())
b = int(input())
if a < b:
    print ("a меньше b")
elif a > b:
    print("b меньше a")
else:
    print("a равно b")













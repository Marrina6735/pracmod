
#Задание 1
type_1 = int(1) #целое число
type_2 = float(2.35) #число с плавающей точкой
type_3 = complex(3.5+2j) #комплексное число
type_4 = list('123') #список
type_6 = str(123) #строка
type_7 = 1 #по умолчанию программа считает это строкой

print(type_1, ' ', type_3)
print(type_4)

number_1 = int(input())
number_2 = input()
a = number_1
b = number_2
print(a, ' ', b)

#Задание 2
print("Введите время в секундах ")
seconds = int(input()) #вводим время в секундах
minutes = 0
hours = 0
while seconds / 60 > 1:
    minutes += 1
    seconds -= 60
while minutes / 60 > 1:
    hours += 1
    minutes -= 60
print(hours, ':', minutes, ':', seconds)

#Задание 3
print("Введите число")
n = int(input()) #введем число
print(n*123) #поскольку n + n * 11 + n * 111 = n * 123

#Задание 4
print("Введите целое положительное число")
a = int(input()) #Создадим целое положительное число
max_a = 0
while a > 0:
    b = a % 10
    if b > max_a:
        max_a = b
    a = a // 10
print(max_a)

#Альтернатива без цикла
#а = str(a)
#print(max(b))

#Задание 5
print("Введите значения выручки и издержки")
gain = int(input()) #выручка
charge = int(input()) #издержка
profit = gain - charge #значение прибыль
if profit > 0:
    print("Компания работает с прибылью")
    r = profit / gain #рентабельность выручки
    print("Введите численность сотрудников компании")
    N = int(input())
    income = profit / N
    print ("Прибыль компании в расчете на одного сотрудника состовляет ", income)
else:
    if profit < 0:
        print("Компания работает в убыток")
    else: print("Компания работает ни с прибылью, ни в убыток")

#Задание 6
print("Введите х километров")
x = float(input())
print("Введите у километров")
y = float(input())
day = 1 #количество дней
while x <= y:
    x = x * 1.1 #увеличивается на 10%
    day += 1
print(day)





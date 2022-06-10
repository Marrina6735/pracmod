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
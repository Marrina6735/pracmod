# Задание 1
while True:
    print("Введите число ")
    n = int(input())
    if n < 0 or n > 10:
        print("Число неверное, введите число больше 0, но меньше 10 ") # вводим число повторно
    else:
        break
print(n**2)
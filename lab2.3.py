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
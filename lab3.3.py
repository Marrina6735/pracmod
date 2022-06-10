# Задание 3
list_1 = [2, 0, 12, 5, 12, 8, 2, 12]
for i in list_1:
    if list_1.count(i) >= 2:
        while i in list_1:
            list_1.remove(i)

print(list_1)

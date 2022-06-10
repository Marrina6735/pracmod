# Задание 4
list_1 = input()
print('Количество удаленных точек составляет ',len(list_1)-len(list_1.replace('.','')))
print(list_1.replace('.','')) # удалить все точки
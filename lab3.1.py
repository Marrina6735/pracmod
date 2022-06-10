# Задание 1
my_list1 = [1, 0, 6, 9, 2, 1, 7, 0, 4, 4]
my_list2 = [1, 2, 9, 4]
for i in my_list2:
    while i in my_list1:
        my_list1.remove(i)
print(my_list1)

# Задание 1
# music_serialize.py
import json
import pickle
my_favourite_group = { # my_favourite_group - словарь, содержащий строки и списки
    'name': 'Г.М.О.',
    'tracks': ['Последний звонок', 'Шапито'],
    'Albums': [{'name': 'Делать панк-рок','year': 2022},
               {'name': 'Шапито','year': 2014}]}

with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(my_favourite_group, f)
print("С помощью json сериализовать данный словарь в json: ")
print(json.dumps(my_favourite_group))

with open('group.pickle', 'wb') as f:
    pickle.dump(my_favourite_group, f)
print("С помощью pickle сериализовать данный словарь в pickle: ")
print(pickle.dumps(my_favourite_group))
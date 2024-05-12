# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

MAXIMUM_WEIGHT = 500

things = {'Палатка': 110,
    'Спальник': 110,
    'Ботинки': 70,
    'Пенка': 40,
    'Пуховик': 150,
    'Термобелье': 30,
    'Дождевик': 30,
    'Кружка': 10,
    'Ложка': 7,
    'Кастрю': 50,
    'Другое': 100
}

weight_things = 0
things_lst = list(things.items())
things_lst.sort(key = lambda x: x[1])

for thing in things_lst:
    if thing[1] + weight_things <= MAXIMUM_WEIGHT:
        weight_things += thing[1]
    else:
        things.pop(thing[0])
print(things)

weight_things = 0
selected_things = {thing: (weight_things + thing[1] if thing[1] + weight_things <= MAXIMUM_WEIGHT else things.pop(thing[0])) for thing in list(things.items()) }

print(things)
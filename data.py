# этот файл использовала для генерации случайных данных
# в самом образе он не играет
from random import randint, choice
random_names = ['Rick', 'Morty', 'Summer', 'Jerry', 'Beth', 'Stanley', 'Maximus', 'Annabel']
random_surnames = ['Smith', 'Pines', 'Kennedy', 'Oswald']
random_cities = ['Washington', 'Oslo', 'Helsinki', 'Moscow', 'Paris']
records = []
for i in range(20):
    name = choice(random_names)
    surname = choice(random_surnames)
    age = randint(18, 50)
    city = choice(random_cities)
    record = (name, surname, city, age)
    records.append(record)

print(records)

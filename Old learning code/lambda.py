#List of tuples, we can sort it with sort(), using lambda function pointing on the second member of each tuple
users = [('Иван', 25), ('Анна', 19), ('Олег', 30)]
users.sort(key=lambda user: user[1]) 

print(type(users[0]))
print(users)

users.sort()

words = ['код', 'питон', 'дом', 'функция', 'лямбда', 'я']
upper_words = []
for x in words:
    if len(x) >3:
        upper_words.append(x.upper())
print (upper_words)

second_upper_words = [x.upper() for x in words if len(x)>3]
print (second_upper_words)

items = [
    {'name': 'Чехол для телефона', 'price': 500},
    {'name': 'Наушники', 'price': 2500},
    {'name': 'Зарядный кабель', 'price': 800},
    {'name': 'Клавиатура', 'price': 4300}
]
temp_items = []
for x in items:
    if x['price'] >1000:
        temp_items.append(x)
print (temp_items)
second_temp_items = []
second_temp_items = [x for x in items if x['price']>1000]
print (second_temp_items)
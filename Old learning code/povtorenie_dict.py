
#___________________Создание словаря ____________________________________________-
my_dict = {'color': 'black', 'material': 'fiber', 'qty':25000, 'price $': 5.3, 'time to deliver': 1.5} #usual creating dict
print (my_dict)
print (type(my_dict))

new_dict = {} #Пустой словарь
print(new_dict)
print(type(new_dict))

galsan_dict = dict(name="galsan", age='38') #creating objec dict by function dict

print(galsan_dict)
print(type(galsan_dict))

bulochka_list = [("Name","Bulochka"), ("age", "35")] #creating dict from list of tuples, it could be come as a result of zip() function
bulochka_dict = dict(bulochka_list)
print(bulochka_dict)
print(str(type(bulochka_dict)) + " bulochka_dict")

second_dict = dict((['love', 100], ['skill', 25])) #Cловарь из функции dict() tuple of lists
second_dict["key1"] = 25000 #Adding new pair
print (second_dict)

raw_list = ["apple", "watermellon", "orange"]
raw_list2 = [100, 255, 500]
third_dict = dict(zip(raw_list, raw_list2)) #ловарь из функции dict() с объектом ZIP
print (third_dict)



#______________________Свойства и методы словаря__________________________
forth_dict = third_dict.copy()
fifth_dict = forth_dict #creating dict like this doesn't create a new dict, bu copy a link for this dict
print(id(third_dict))
print(id(forth_dict))
print(id(fifth_dict))

raw_list3 = ['table', 'stool', 'knife', 'fry pan']
sixth_dict = dict.fromkeys(raw_list3, 'available') #creating dict from one list and filling with the same values
print (sixth_dict)

sevent_list = {a: a+a for a in range (1,4)}
print (sevent_list)


print(bulochka_dict['age']) #gets value of this key, if there is no such key - ERROR
print(bulochka_dict.get('address', "No such key")) #gets value of this key, returns 2nd paramater if nothing was found, used to avoid errors

print (my_dict.keys())
print (my_dict.values())
print (my_dict.items())

print (type(my_dict.keys()))
for parameter_one_for_key, parameter_two_for_value in my_dict.items():
    print (parameter_one_for_key,parameter_two_for_value )

[print(a,b) for a,b in my_dict.items() ] #List Comprehension - Использование генератора списков

print('***' * 15)
print(my_dict)

#Распаковка словаря 

def func_for_smth (color, material, qty = 0, *args, **kwargs):
    print (f" we have product wih {color} color, made with {material}, and its quantity is {qty}")


func_for_smth(**my_dict)
my_set = {55,45,777, 5656, 8845}

my_set.add(4545)

print (my_set)

second_set = {55,4545, 4572, 9956, 6445}

print (my_set & second_set)

my_list = my_set | second_set
print (list(my_list))
my_set.update(second_set)
print (my_set)
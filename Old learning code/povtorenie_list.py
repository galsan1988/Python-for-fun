#list

my_list = [1,2,3,4]
second_list = list() #only one arg
second_list.append(25) #only 1 arg

for iterator in range(1,3,1):
    second_list.append(5*iterator) 

second_list.extend([it*10 for it in range (1,3,1)])
print (second_list)

third_list = second_list+my_list #operator + in this case is the same as .__add__()

forth_list = second_list.copy() #complete copy of obj 2nd list
fifth_list = second_list #copy of the link for 2nd list
sixth_list = second_list #copy of the link for 2nd list
print (my_list)
print (second_list, f'\n ID is {id(second_list)} \n \n' )
print (id(forth_list)) #created using copy() its unique object separated from original
print (id(second_list)) #is a copied object
print (id(fifth_list), "fifth list ID") #is a copy of address
print (id(sixth_list)) #is a copy of address

fifth_list = [2,5,8] #Since we already have this obj, but this is not muting already existing object
#it is creating an object
print (fifth_list)
print (id(fifth_list), "fifth list ID")

sixth_list.append(999) #changing 6th list and also changing 2nd list, because they refer to one object
print (second_list,"second_list, it's been changed by its link") #because 6th list was changed this one is also changed
print (sixth_list, "sixth list that was changed")

print('*****'*15)
print(second_list.count(25)) #counting this arguement inside of the list
print(len(third_list)) #showing how many objects in this list
print(second_list.index(25)) #showing index of this object if it is in the list, error if not
popped_item =second_list.pop(second_list.index(25)) #find the first object with value 25 and erase it by its index, and save the erased item into the new object called popped_item
print (second_list) #the result was saved into the list
print (popped_item) #we can see the popped item
second_list.sort() #soring list from small number to high
second_list.reverse() #reversing the list
print (second_list)
second_list.insert(0, 66) #adding an item inside of the list by its index 
print (second_list)
second_list.remove(5) #removing the first found item, error if the item is not in the list
print (second_list)
second_list.extend(third_list) #extend by the items of the list
second_list.append(third_list) #adding a list as an item into the list


print ("___"*20)
print ("\n", second_list)
print (second_list.__class__) #type() magic method
# print (second_list.__doc__) #description

seventh_list = third_list + [5*item for item in fifth_list] #cycle for in one lane using list comprehension
print (seventh_list)

print (" \n \n")
second_list = [2,2,2]
print(my_list)
print(second_list)
print (my_list.append(second_list)) #my list was changed even here - returned object is None
print (my_list, "my list added second list in the end, but it was an object")
print (my_list.pop(-1), "changed with pop() and deleted item is")
print (my_list + second_list, "the same action with second list")


print ('___'*15, "\n \n")


print(seventh_list, "seventh list")
filtered_list = list(filter(lambda num: num %2 ==0, seventh_list))
print(filtered_list, "filtered seventh")
try:
    variable1, var2,*var3 = filtered_list #UNPACKING
except ValueError as e:
    print (e)
# var4, *var5_list = filtered_list #Unpacking with a variable that has multiple variables
# print (variable1) 

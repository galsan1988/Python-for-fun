
#CUTTING using list fucntions
bin_number = bin(3+10).replace('0b', '') # Create Bin number as a STR and Replace 0b with '' 
bin_number2 = bin(25+35)[2:] #Create Bin number as a STR and Cut everything before index 2

print(bin_number2)
print(bin_number)
#TUPLE, LIST or SET
e = tuple(bin_number2)  #STR change into another type TUPLE, LIST or SET 
e = list(bin_number2)
c = set(bin_number)

#find()
index_of_num = bin_number.find('01') #returns the first index of 101 if found, else returns -1
print (index_of_num)

#count()
print (bin_number2.count('1')) #returns qty of '1' in the str
string_one = "My name is Galsan"

#split()
list_of_strings = string_one.split(' ') #splitting by ' ' and returning the list of str objects
print (list_of_strings)

#join()
back_to_string = ','.join(list_of_strings)  #joining the list of str objects using ',' returning one STR object
print (back_to_string)

#strip()
back_to_string.strip(' ') #delete ' ' from both begin and ending of the STR

#replace()
back_to_string =  back_to_string.replace(',',' ')
print(back_to_string)
back_to_string = back_to_string.replace(' ', '')

# + 
string_one = string_one + '!' #simple adding 
print(string_one)

#isalnum() isdigit() isalpha()
print(string_one.isalnum()) #checking if the STR is only alphabet and digits FALSE
print(back_to_string.isalnum()) #checking if the STR is only alphabet and digits, NO SPACES or other symbols - TRUE

#iterable
for it in back_to_string: #STR is iterable object
    print (it)
print(back_to_string[0])

#immutable
# back_to_string[0] = 'S' #ERROR !!! #THIS WON"T WORK BECAUSE STR IS IMMUTABLE OBJ

#frormat()
template_format = " User ID: {user_id} has entered the game at {timer}, he/she has spawned in {territory}"
dict_to_paste ={ "user_id": 54545, 'timer': '00:45', 'territory': "old city"}
print (template_format.format(**dict_to_paste)) #The superior usage of format() function
#This file is to learn about int class properties


num_a = 25.1  #creating float 
int_a = int(num_a) # making int from float by deleteing everything after the float


int_b = 11
int_c = int_b
int_d = 11
print(id(int_b))
print(id(int_c))
print(id(int_d)) 
#all three share the same ID because integers are immutable 
#python points creates different objects poiting at the same integer 
print ("____" * 15, '\n', '\n')


int_b += 20 # int_b = int_b + 20
print (int_c) 
#modidying int_b creates new object, int_c is still pointing at the same integer
#this proves they are all independent objects, not bound to each other

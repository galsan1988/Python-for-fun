#Блок с обработкой ошибок и поимкой ошибки

# try:
#     a= 10/ "asd"  #Если здесь попадет 0 или строка - то ошибка будет поймана в двух секциях ниже
#     print (a)
# except ZeroDivisionError as e:
#     print (e)
# except TypeError as e:
#     print (e)
# else:
#     print ("no error occured")
# finally:
#     print ('continue...')



#Минимальная обработка ошибки
# try:
#     a = 10 / 0
# except Exception as e:
#     print (e)




# #Блок где мы создаем собственную ошибку с помощью Raise
# def devide_num (a,b):
#     if b == 0:
#         raise TypeError("ERROR cannot devide by 0 ")
#     if type(b) == str:
#         raise TypeError ("ERROR cannot use STR-class for division ") 
#     return a/b


# try:
#     print(devide_num(10,3))
# except TypeError as e:
#     print (e)
# print ('continue...')




def image_info (img):
    if 'image_id' not in img or 'image_title' not in img:
        raise TypeError ('ERROR invalid image ID or image title ')
    
    return f"Image {'image_title'} has id {'image_id'}"

my_dict = {'image_id': 1, 'image_size': 'cats'}


print (my_dict)

try:
    image_info(my_dict)
except Exception as e:
    print (e)



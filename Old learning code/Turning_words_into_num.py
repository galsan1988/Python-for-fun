
def Turn_into_num(message):
    num_str_list = message.replace('-', ' ').split()
    print (num_str_list)
    simple_num = {
        'one': 1,'two': 2,'three': 3,'four': 4,'five': 5,'six':6,'seven':7,'eight':8,'nine':9,
        'ten':10,'eleven':11,'twelve':12,"thirteen":13,'fourteen':14,'fifteen':15,
        'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19,
    }
    double_num = {
        'twenty':20,'thirty':30,'forty':40,'fifty':50,
        'sixty':60,'seventy':70,'eighty':80,'ninety':90
    }
    multyplier100 = {'hundred':100}
    multyplier1000 = {'thousand':1000, 'million':1000000}

    temp_num = 0
    temp2_num = 0
    thousands = []
    millions = []
    for it in num_str_list:
        if it in simple_num:
            temp_num += simple_num[it]
        if it in multyplier100:
            temp_num = temp_num*100
        if it in double_num:
            temp_num += double_num[it]
        if it in multyplier1000:
            temp2_num = temp2_num + (temp_num * multyplier1000[it])
            temp_num = 0
    return temp_num + temp2_num

a= 'one million six hundred eighty three thousand four hundred sixty five'
b = 'one million and four thousand sixty eight'
print(Turn_into_num(a))
print (Turn_into_num(b))

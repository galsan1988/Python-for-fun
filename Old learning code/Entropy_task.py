import math

# message = " Some kind of random text, maybe uploaded from web-site or text file, it doesn't count spaces as a unique symbol "
message = '            '

def entropy(message):
    temp_message = [symb for symb in message if symb!=' ']
    unique_symb = set(temp_message)
    length = len(temp_message)
    total = 0
    for each_s in unique_symb:
        p_i = temp_message.count(each_s)/length
        total += p_i * math.log2(p_i)
    return -total


print(entropy(message))
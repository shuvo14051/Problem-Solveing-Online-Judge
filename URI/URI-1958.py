number = float(input())
scientific_notation = "{:e}".format(number)
str_num = str(scientific_notation)
print(str_num)

result_pos = '+'
result_neg = ''

if number >= 0:
    for i in str_num:
        if i == 'e':
            result_pos += i.upper()
        else:
            result_pos += i
    
    print(result_pos)

elif number < 0:
    for i in str_num:
        if i == 'e':
            result_neg += i.upper()
        else:
            result_neg += i

    print(result_neg)

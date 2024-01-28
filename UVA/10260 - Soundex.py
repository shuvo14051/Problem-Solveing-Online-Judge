while True:
    result = ""
    try:
        word = input()
        for i in word:
            if i in 'BFPV':
                result += '1'
            elif i in 'CGJKQSXZ':
                result += '2'
            elif i in 'DT':
                result += '3'
            elif i in 'L':
                result += '4'
            elif i in 'MN':
                result += '5'
            elif i in 'R':
                result += '6'
        print(result)     
    except EOFError:
        break
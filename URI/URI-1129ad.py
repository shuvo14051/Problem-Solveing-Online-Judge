test = int(input())

for i in range(test):
    
    li = list(map(int, input().split()))
    options = {index: value for index, value in enumerate(li) if value <= 127}

    possible_answers = list(options.values())

    # if len(possible_answers) == 1:
    #     answer = possible_
    print(possible_answers)

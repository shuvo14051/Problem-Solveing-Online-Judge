test = int(input())
vowels = 'aeiou'
def max_consonant(name):
    count = 0
    li = []
    for i in name.lower():
        if i not in vowels:
            count += 1
        else:
            li.append(count)
            count = 0
    li.append(count)
    return li

        

for _ in range(test):
    # li = []
    name = input()
    result = max_consonant(name)
    if max(result)>=3:
        print("{} nao eh facil".format(name))
    else:
        print("{} eh facil".format(name))
    
    
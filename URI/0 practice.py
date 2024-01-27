def max_consonant(name):
    count = 0
    li = []
    vowels = "aeiou"
    for i in name.lower():
        if i not in vowels:
            count += 1
        else:
            li.append(count)
            count = 0
    # Add this line to account for the last consonant sequence
    li.append(count)
    return li

print(max_consonant("bbbeddddipppppppp"))

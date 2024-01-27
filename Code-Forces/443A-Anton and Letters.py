line = input()

if line == "{}":
    print(0)
else:
    spilled = line.split(",")
    spilled[0] = spilled[0].replace('{','')
    spilled[-1] = spilled[-1].replace('}','')

    remove_space = [element.strip() for element in spilled]
    
    # print(remove_space)
    unique = set(remove_space)
    # print(unique)
    print(len(unique))

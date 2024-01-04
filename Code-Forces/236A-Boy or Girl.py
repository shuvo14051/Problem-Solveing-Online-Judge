username = input()
li = [char for char in username]
unique = set(li)
length = len(unique)

if length % 2 != 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
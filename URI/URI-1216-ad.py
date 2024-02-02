dis = 0
cont = 0
total = 0.0

while True:
    try:
        name = input()
        
        if not name:
            break
        dis = int(input())
        total += dis
        cont += 1

    except EOFError:
        break

print("{:.1f}".format(total / cont))
  
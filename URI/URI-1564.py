
while True:
    try:
        line = input()
        if not line:
            break  
        n = int(line)
        if n == 0:
            print("vai ter copa!")
        else:
            print("vai ter duas!")
    
    except EOFError:
        break
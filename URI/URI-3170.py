# while True:
balls = int(input())
branches = int(input())

balls_needed = (branches//2) - balls

if balls_needed > 0: 
    print("Faltam {} bolinha(s)".format(balls_needed))

else:
    print("Amelia tem todas bolinhas!")


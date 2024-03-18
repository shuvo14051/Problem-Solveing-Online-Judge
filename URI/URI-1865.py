# 5% wrong answer
# while True:
#     try:
#         a = input().lower()
#         if a.startswith('thor'):
#             print('Y')
#         else:
#             print('N')

#     except EOFError:
#         break

# I don't know why

for i in range(int(input(""))):
    print("Y" if input("").split()[0].lower() == "thor" else "N")
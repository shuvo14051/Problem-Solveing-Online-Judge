name = input().lower()
guest = input().lower()

puzzeled = input().lower()

sorted_name = ''.join(sorted(name))
sorted_guest = ''.join(sorted(guest))
real = sorted_name+sorted_guest
sorted_real = ''.join(sorted(real))
sorted_puzzeled = ''.join(sorted(puzzeled))

if  sorted_real == sorted_puzzeled:
    print("YES")
else:
    print("NO")


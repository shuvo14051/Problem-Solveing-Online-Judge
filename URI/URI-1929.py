def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def can_form_triangle(lengths):
    if is_triangle(lengths[0], lengths[1], lengths[2]) or \
       is_triangle(lengths[0], lengths[1], lengths[3]) or \
       is_triangle(lengths[0], lengths[2], lengths[3]) or \
       is_triangle(lengths[1], lengths[2], lengths[3]):
        return True
    else:
        return False
    
li = list(map(int, input().split()))
res = can_form_triangle(li)

if res:
    print("S")
else:
    print("N")
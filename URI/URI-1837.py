a, b = map(int,input().split())

def euclidean_division(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    
    q = a // b  # Integer division to get the quotient
    r = a % b   # Modulus operation to get the remainder
    
    return q, r

print(euclidean_division(a,b))
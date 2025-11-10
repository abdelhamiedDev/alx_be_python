def gcd(a, b):
    a , b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

def gcd_recursive(a, b):
    a , b = abs(a), abs(b)
    if b == 0:
        return a
    return gcd_recursive(b, a % b)
print(gcd(72, 11))
print(gcd_recursive(72, 11))
def gcd(a, b):
    while b != 0:
        temp = a
        a = b
        b = temp % b
    return a


print(gcd(18, 30))
print(gcd(30, 18))
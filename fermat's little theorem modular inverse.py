def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)
   
   
def invFermat(a, b):
    if gcd(a,b) != 1:
        print("No modular inverse")
        return False
    c = a**(b-2)
    print(c%b)
    return True
   
invFermat(3,7)
invFermat(5,9)
invFermat(6,11)
invFermat(11,13)
invFermat(12,21)

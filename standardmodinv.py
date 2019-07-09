def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)
   
   

def invMod(a, b):
    if gcd(a,b) != 1:
        print("No modular inverse")
        return False
    d = 0
    while True:
        if d*a%b == 1:
            print(d)
            return True
        d = d+1
    return False
   
invMod(2,7)
invMod(4,10)
invMod(5,11)
invMod(7,13)
invMod(11,15)

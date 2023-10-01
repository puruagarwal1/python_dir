# This program computes greatest common divisor or gcd of two natural numbers using Euclid's algorithm.
def gcd(m,n):
    if m<=0 or n <=0:
        raise ValueError("Given numbers {}, {} are not natural numbers.".format(m,n))
    g=max(m,n)
    s=min(m,n)
    if g%s ==0:
        return s
    while (g%s):
        r=g%s
        g=s
        s=r
    return s
m=int(input("Enter a natural number m:"))
n=int(input("Enter a natural number n:")) 
print("GCD(m,n) = {}".format(gcd(m,n)))

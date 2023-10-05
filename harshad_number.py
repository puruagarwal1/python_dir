'''
HARSHAD NUMBER:

A number is said to be the Harshad number if it is divisible by the sum of its digit.
'''

n=input("ENTER THE NATURAL NO: ")
sum=0
for x in n :
    sum+=int(x)
if int(n) % sum == 0 :
    print("NO is HARSHAD NUMBER.")
else :
    print("NO is not a HARSHAD NUMBER.")
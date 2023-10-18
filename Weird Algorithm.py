# Weird Algorithm problem link and solution from CSES
#https://cses.fi/problemset/task/1068/

n=int(input())
l=[n]
while(n!=1):
    if(n%2==0):
        n=int(n/2)
        l.append(n)
    else:
        n=n*3+1
        l.append(n)
print(*l)       

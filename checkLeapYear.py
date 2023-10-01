year = int(input("Enter an year :"))
if(year%4==0):
    if(year%100 == 0):
        if((year/100)%4 !=0):
            print(year," is not a leap year.")
        else:
            print(year," is a leap year.")
    else:
            print(year," is a leap year.")
else:
    print(year," is a leap year.")
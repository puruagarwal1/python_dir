# # one parent one child
# class employee:                      #base class (single inheritance)
#     company="google"
#     def getdetails(self):
#         print("this is an employee")

# class programmer(employee):                 #derived class
#     language="python"
#     def showdetails(self):
#         print(f"the language is {self.language}")

#     def getdetails(self):
#         print("this is an programmer")

# e=employee()
# e.getdetails()
# print(e.company)
# p=programmer()
# p.getdetails()
# p.showdetails()
# print(p.company)

# # 2 parents one child(multiple inheritance)
# class employee:
#     company="microsoft"
#     level=1
#     def upgradelevel(self):
#         self.level=self.level + 1
#     print("he is a freelancer")
# class freelancer:
#     company="google"
#     ecode=120

# class programmer(employee,freelancer):
#     name="palak"
# p=programmer()
# p.upgradelevel()
# print(p.company)
# print(p.level)

# 1 parent 1 subparent 1 children (multilevel inheritance)

class person:
    company="indigo"
    def __init__(self):
        super().__init__()
        print("initializing a person")
    def takeBreath(self):
        print("i am breathing....")

class employee(person):
    company="visa"
    def __init__(self):
        super().__init__()
        print("initializing a employee")
    def takeBreath(self):
        print("i am employee and still breathing...")
    def getsalary(self):
        print(f"my salary is {self.salary}")
    
class programmer(employee):
    company="microsoft"
    def __init__(self):
        print("initializing a programmer")
        super().__init__()
    def takeBreath(self):
        super().takeBreath()
        print("i am a programmer and breathing++")
    def getsalary(self):
        print(f"my salary is {self.salary}")

p=programmer()
pe=person()
e=employee()
e.salary=34000
p.salary=56000
pe.takeBreath()
p.getsalary()
p.takeBreath()
e.takeBreath()
print(pe.company)

class employee:
    name="harry"
    company="google"
    salary="23000"
    @classmethod
    def changesalary(cls,sal):
        cls.salary=sal
e=employee()
print(e.salary)
e.changesalary(32000)
print(e.salary)

class employee:
    salary =9000
    salarybonus =500
    @property                   #getter
    def totalsalary(self):
        return self.salary + self.salarybonus
    @totalsalary.setter           #setter
    def totalsalary(self,value):
        self.salarybonus= value- self.salary
e=employee()
print(e.totalsalary)
e.totalsalary=23300
print(e.salary)
print(e.salarybonus)

# operaator overloading
class number:
    def __init__(self,num1):
        self.num1=num1
    def __add__(self,num2):
        print("lets add ")
        return self.num1+ num2.num1
        # return 300
    def __mul__(self,num2):
        print("lets multiply")
        return self.num1 * num2.num1
    def __floordiv__(self,num2):
        print("lets multiply")
        return self.num1 // num2.num1
    def __truediv__(self,num2):
        print("lets multiply")
        return self.num1 / num2.num1
    def __str__(self):
        return f'decimal number={self.num1}'
    def __len__(self):
        return 9
n1=number(90)
n2=number(10)
sum=n1+n2
print(sum)
multiply=n1*n2
print(multiply)
div=n1//n2
print(div)     #int
truediv=n1/n2
print(truediv)    #float
n=number(1020)
print(n)
print(len(n))

# hybrid inheritances:

class baseclass:
    pass
class derivedclass1(baseclass):
    pass
class derivedclass2(baseclass):
    pass
class derivedclass3(derivedclass1,derivedclass2):
    pass

# hierichalclass inheritances:
class baseclass:
    pass
class d1(baseclass):
    pass
class d2(baseclass):
    pass
class d3(d1):
    pass
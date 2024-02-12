# inbuilt functions
y = max(32, 56, 78, 49, 80)
print(y)

x = min(14, 37, 3, 83, 9)
print(x)

z = pow(2, 3)
print(z)


# user defined function
def details():
    print("Michelle")


details()  # calling a function


# parameters and arguments

def students(name, course, age):
    print(name, course, age)


students("Ashley", "MIT", 17)
students("Michelle", "MIT", 20)


def Employees(fullname, Idno, salary, position, age):
    print(fullname, Idno, salary, position, age)


Employees("job", 3464, 1200000, "chairperson", 45)
Employees("Elizabeth", 3478, 100000, "secretary", 34)
Employees("Mark", 3489, 900000, "manager", 43)
Employees("Jessica", 3429, 800000, "head employee", 50)
Employees("Dylan", 3479, 700000, "member", 29)

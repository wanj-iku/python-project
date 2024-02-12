# exception = error

try:
    print(x)
except:
    print("NameError occurred")
finally:
    print("Success")

num1 = 20
num2 = 0
try:
    print(num1 / num2)
except:
    print("ZeroDivisionError occurred")


# User-defined function
def multiply(x, y):
    return x * y


print(multiply(5, 7))

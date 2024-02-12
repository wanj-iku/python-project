# A simple calculator
v = float(input("Enter first number:"))
t = float(input("Enter second number:"))
operator = input("Enter Operator:")
if operator == "+":
    print("result is:",v+t)
elif operator == "-":
    print("result is:",v-t)
elif operator == "*":
    print("result is:",v*t)
elif operator == "/":
    print("result is:",v/t)
else:
    print("Invalid Operator")
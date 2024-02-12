temperature = 32

if temperature > 37:
    print("it is hot")
else:
    print("it is cold")

# A program that prints out the largest number among 3 numbers
num1 = 20
num2 = 70
num3 = 40
if num1 > num2 and num1 > num3:
    print(num1, "is the largest number")
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest number")
else:
    print(num3, "is the largest number")

# a program that checks whether a number is even or odd
number = 71
if number % 2 == 0:
    print("number is even")
else:
    print("number is odd")

# A program that checks whether a number is prime or not


n = int(input("Enter a number: "))
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print(n, "is not a  prime number")
            break
    else:
        print(n, "is a prime number ")
else:
    print("is not a prime number")

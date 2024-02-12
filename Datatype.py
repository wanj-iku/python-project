#  datatype
number = 60  # int
num = 34.78  # float
greeting = "hellow there"  # str
isPythonInteresting = True  # bool

# A variable with multiple values
languages = ["python", "PHP", "java"]  # list
fruits = ("apple", "banana", "oranges")  # tuple
countries = {"kenya", "Ghana", "China"}  # set
# Dictionary
Details = {
    "firstname": "Ashley",
    "course": "MIT",
    "age": 18,
    "nationality": "kenyan"

}
print(Details["firstname"])
print(Details["nationality"])
print(number)
print(num)
print(greeting)
print(isPythonInteresting)
print(countries)
print(languages)
# Determining the data type of a variable
print(type(Details))
print(type(countries))
print(type(greeting))

# Typecasting converting one data type to another
print(float(number))
print(int(num))

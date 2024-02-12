courses = ["MIT", "Cybersecurity", "Datascience"]

print(courses)
# Accessing an element in an array
print(courses[1])

# looping through an array
for course in courses:
    print(course)

# Adding a element to an array
courses.append("Android development")
print(courses)

# deleting an element in an array
courses.remove("Datascience")
print(courses)

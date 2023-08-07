Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

# Print the value of the shoe size
shoe_size = Shoes["size"]
print("Shoe Size:", shoe_size)


# Change the value "Nick" to "Adidas"
Shoes["brand"] = "Adidas"
print("Updated Shoes:", Shoes)

# Add a new key/value pair to the dictionary
Shoes["type"] = "sneakers"
print("Updated Shoes:", Shoes)

# Get a list of all the keys in the dictionary
keys = list(Shoes.keys())
print("Keys List:", keys)

# get a list of all values in dictionary
values = list(Shoes.values())
print(values)

# Check if the key "size" exists in the dictionary
if "size" in Shoes:
    print("Key 'size' exists in the dictionary.")
else:
    print("Key 'size' does not exist in the dictionary.")
    
#Looping
for keys ,values in Shoes.items():
    print (keys,':',values)

# Remove the key "color" from the dictionary
Shoes.pop("color")
print("Updated Shoes:", Shoes)

# Empty the dictionary
Shoes.clear()
print("Updated Shoes:", Shoes)

#copt dictionary
# Create a dictionary
original_dict = {
    "name": "BAZZIWE",
    "age": 21,
    "course": 'BSSE',
    "COUNTRY": 'Uganda'
}

# Make a copy of the dictionary
copied_dict = dict(original_dict)
print("Original Dictionary:", original_dict)
print("Copied Dictionary:", copied_dict)

#NESTED BICTIONARIES
# Define a nested dictionary
student = {
    "name": "BAZZIWE MARVIS",
    "age": 21,
    "contact": {
        "phone": "+256-760-130-194",
        "email": "Bazz@example.com"
    },
    "courses": {
        "mobile programming": 80,
        "php": 80,
        "python":90
    }
}

# Access nested dictionary values
student_name = student["name"]
student_age = student["age"]
contact_phone = student["contact"]["phone"]
contact_email = student["contact"]["email"]
math_grade = student["courses"]["mobile programming"]
science_grade = student["courses"]["php"]
history_grade = student["courses"]["python"]

# Print the values
print("Student Name:", student_name)
print("Student Age:", student_age)
print("Contact Phone:", contact_phone)
print("Contact Email:", contact_email)
print("Mobile programming Grade:", math_grade)
print("php Grade:", science_grade)
print("python Grade:", history_grade)


#set constructor
favorite = set(["Coffee", "Sprite", "yorgut smoothie"])

print("Favorite Beverages:", favorite)
#add beverages
favorite.update(['tea', 'juice'])
print(favorite)
#check if microwave is present
mySet = {"oven", "kettle", "microwave", "refrigerator"}

if "microwave" in mySet:
    print("Microwave is present in the set.")
else:
    print("Microwave is not present in the set.")
#REMOVE KETTLE
mySet.remove('kettle')
print("updates:",mySet)
#looping
for x in mySet:
    print(x)
#list and set
mySet = {"apple", "banana", "orange", "grape"}
myList = ["cherry", "melon"]

# Adding elements from the list to the set
mySet.update(myList)

print("Updated Set:", mySet)

#2 sets with names and age
ages = {15, 20, 25}
first_names = {"Bazz", "Marvis", "skay"}

# Join the two sets
new_set = ages.union(first_names)

print("Joined Set:", new_set)

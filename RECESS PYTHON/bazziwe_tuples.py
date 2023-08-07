#indexing tuples:Tuples are zero-indexed
print("BAZZIWE MARVIS 21/U/0423")
my_phone = ('iphone','samsung','sony')
print(my_phone[0])  
print(my_phone[1])  
print(my_phone[2]) 
#unpacking tuples
my_phone = ('iphone','samsung','sony')
phone1,phone2,phone3 = my_phone
print(phone1)
print(phone2)
print(phone3)
#Negative Indexing to access elements from the end of the tuple.
#-1 represents the last element
my_phone = ('iphone','samsung','sony')
print(my_phone[-1])  # Output: 'cherry'
print(my_phone[-2])  # Output: 'banana'
print(my_phone[-3])  # Output: 'apple

#Slicing allows you to specify a range of indices to retrieve a sublist of elements.
my_phone = ('iphone','samsung','sony','haweii','redmi')
print(my_phone[1:4])
print(my_phone[3:6])


#adding items in tuples
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
new_tuple = tuple(tuple1) + tuple(tuple2)

print(new_tuple)  

tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
new_tuple = tuple(tuple1) + tuple(tuple2)

print(new_tuple)  
my_phone = ('iphone','samsung','sony')
myphone =('iphone 14pro max')
#tuple(my_phone)+= tuple(myphone)
newstock = myphone + my_phone
print(newstock)
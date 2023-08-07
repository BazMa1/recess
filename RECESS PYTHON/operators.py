#examples of conditional operators
if (12>10):
    print("12 is greater")
    
    #less than
    a =3
    b= 5
    if ( a < b):
        #print(" b is greater")
        print (a<b)
    #equal to
        print(a==b)
    #greater than
        print(a>b)
    #not equal to
        print(a!=b)
        
        #LOGICAL OPERATORS
        
x= True
y= True
 #LOGICAL AND
print(x and y ) # Returns True if both x and y are True, False otherwise
    
#LOGICAL OR 
print( x or y) # Returns True if either x or y (or both) is True, False otherwise
#LOGICAL NOT
print(not x ) # Returns the opposite Boolean value of x

#ASSIGNMENT OPERATORS
#COMPOUND
#+=   -=    *=      /=       %=        **=
a =40
g =2
c= 401
a +=50
print(a)
#EXPONENTS
g**=4
print(g)

#MODULUS
c%=2.5
print(c)

#MEMBERSHIP ASSIGNMENT OPERATORS
# Testing membership in a string
s = "Hello, Bazziwe!"
print('o' in s)  # True
print('z' in s)  # True
print('p'in s) #false

# Testing membership in a list
my_list = [1, 2, 3, 4, 5]
print(2 in my_list)  # True
print(67 not in my_list)  # True
print(11 in my_list) # False

# Testing membership in a dictionary (checks keys)
my_dict = {'a': 6, 'b': 5, 'c': 4}
print('a' in my_dict)  # True
print('e' not in my_dict) # True
print( 'd'in my_dict)

#IDENTITY OPERATORS
#is operator checks for object identity while == compares values
# Comparing identity of integers
a = 5
b = 5
c = 6
print(a is b)  # True
print(a is c)  # False

# Comparing identity of lists
W= [1, 2, 3]
Z= W
Y= [1, 2, 3]
print(W is Z)  # True
print(W is Y)  # False

# Comparing identity of custom objects
class MyClass:
    pass

obj1 = MyClass()
obj2 = MyClass()
obj3 = obj1

#print(obj1 is obj2)# False
print(obj1 is not obj2)
print(obj1 is obj3)  # True

#bitwise operations



    

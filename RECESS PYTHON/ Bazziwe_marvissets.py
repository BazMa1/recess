#sets are unchangeable but one can add new items or remove items
#Duplicates in sets
phone ={'Samsung', 'redmi' , "iphone"}
print(phone)
#compare the outpot of set phone and phone2
phone2= {'samsung','redmi','iphone','iphone'}
print(phone2)
#finding length of a set
set3={'a','b','c','d','e','A'}
print(len(set3)) 
A =len({'samsung','redmi','iphone','iphone'})
print(A)

#add items together in sets
#add Tecno
phone4= {'samsung','redmi','iphone','iphone'}
phone4.add('Tecno')
print(phone4)

#add sets together
#using union operator 
phone5= set3 | phone4
print(phone5)
#using union operator 
name1={'bazziwe'}
name2 ={'Marvis'}
fullname = name1.union(name2)
print(fullname)

#datatypes
#NUMBERS
myset1={ 1, 2,3.14}
print(myset1)
#STRINGS
myset2= { 'cash','iphone13 promax','health and prosperity','life'}
print(myset2)
#BOOLEANS
myset={ True,False}

#TUPLES
myset3= { ('bazz',100),('Marvis',98)}
print(myset3)
#FROZENSETS
myset4={frozenset({50,40}),frozenset({46,40})}
print(myset4)

#ACCESSING ITEMS IN SETS
#USING FOR
myset2= { 'cash','iphone13 promax','health and prosperity','life'}
for x in myset2:
    print(x)
#USING IF
set3={'a','b','c','d','e','A'}
if 'a' in set3:
    print('a is present')
else:
    print("a is not")












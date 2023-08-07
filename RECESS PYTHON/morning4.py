#demonstrating regex
import re
text ='Hello, iam Bazz the billionaire with $100B'
#match first word
match = re.search(r"^\w*", text)
if match:
    print("match:",match.group())
    
#FIND NUMBER
matches = re.findall(r"\d+",text)
print('matches:',matches)

#VALIDATE_EMAIL
import re
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern,email):
        return True
    else:
        return False
email1 ='bazziwemarvis@gmail.com' 
print(validate_email(email1))
    
print('=============GENERATORS==============')
#GENERATORS AND ITERATORS
#Generating factorial
def factorial(n):
    if n==0:
        return 1
    else:
        return n* factorial(n-1)
  #factorial for numbers in range 1 to 10  
for i in range(1, 10):
        print(factorial(i))
print('============================================')
def factorial_generator(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result

# Example usage
for i in factorial_generator(10):
    print(i)
#print('==========squares================')


    
print('===========================ITERATORS=================')
def squares(n):
    for i in range(1,10):
        yield i **2
        
for i in squares(10):
    print(i)
        
print('==================decorators========================')     
#decorators are a way to modify the behavior of a function or class without changing its source code
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")
        return result
    return wrapper

@measure_time
def my_function():
    # Your function logic here
    time.sleep(2)

my_function()

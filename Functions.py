# SYNTAX FOR WITHOUT ARGUMENTS
def name():
    print("welcome to the functions in python ")
name()
# FUNCTION WITH ARGUMENTS
def fullname(input): # Here the input is one of the arguments in that fullname function
    print(f"hello {input} welcome to the class ")
fullname("saran") # This is the way to pass the input trough the arguments 

# FUNCTION WITH TWO ARGUMENTS
def add(a,b): # Here we pass the two arguments in that function 
    print(a+b)
add(2345,876) # This is the way to pass the input trough the arguments 

# RETURN STATEMENT IN FUNCTION
def sub(e,r):
    return e-r # Here return is used for to assign to anoter variable , methods or functions
result=sub(456,123) # In this line we paas the return value to the result variable 
print(result)   

# FUNCTION CALL FROM ANOTHER FILE (HERE FILE NAME IS CALL.py)
from call import add # This line used to call file where the function wrote
result=add(4325542,8879689) # Without return function can"t abblr to do
print(result)

# *args IN THE FUNCTION USE CASE 
def mul(*args): #Here * args accept to assign multi arguments in that function
    # mull(1,2,3,4)
    total=1
    for n in args:
        # so args have the value(1,2,3,4)
        # for n in args(1,2,3,4):
        total*=n # without third arguments we increment the value and to that same variable 
        # 1*=1
        # 1*=2
        # 2*=3
        # 6*=4
    return total # Here return is used to give or return the value of total to another value,variable or function 
print(mul(1,2,3,4,5))   

'''def sub(*args):
    total1=0
    for i in args:
        total1-=i
    return total1
print(sub(1,2,3,4,5,6,7,8,9))'''

# **kargs STATEMENT IN FUCTION USE CASE
def profile(**kwargs): 
    ''' here we use **kwargs to implement te key, value pair in the function. it also have the multi value handelling '''
    print("Your profile")
    for key,value in kwargs.items():
        print(f"{key}: {value}")
profile(name="saran",age=22,location="salem",phno=9344513738)
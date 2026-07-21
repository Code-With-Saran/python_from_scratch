a=input("enter your first name :")
b=input("enter your last name ")
c=a+b
print("your full name is ____", c)

# The real time production input type 
import sys
# fir check if the arguments are statisfied or not
if len(sys.argv)==2:
    print("usage: email.generator.py want two arguments like first name and last name")
    sys.exit()
# The above code will be exit here
# Here the arg== 2, it exit and run the code or else its run print statements



full_name=sys.argv[1]
last_name=sys.argv[2]    # second input argument
email=full_name.lower().replace(" ","_")+last_name+"@mass_company.com"
print("your profile")
print("Your name is",full_name,last_name)
print("your company Email is",email)
import sys
# fir check if the arguments are statisfied or not
if len(sys.argv)==2:
    print("usage: email.generator.py want two arguments like first name and last name")
    sys.exit()
# The above code will be exit here
# Here the arg== 2, it exit and run the code or else its run print statements



full_name="".join(sys.argv[1:])   # here we use : for one and more one arguments are take it as input in the run time
print(full_name)

# "".join(sys.argv[1:]) to use join the separated input as single string

email=full_name.lower().replace(" " , ",")+"@masscompany.com"
print("your profile")
print("Your name is",full_name)
print("your company Email is",email)
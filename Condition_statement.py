# FOR IF AND ELSE CONDITION
'''import sys
input=(sys.argv[1])
age=int(input)'''
age=25
if age>=18:
    print("u are eligiblr to vote")
else:
    print("u cant to vote")

# FOR IF, ELIF AND ELSE CONDITION
'''import sys
input=(sys.argv[1])
mark=int(input)'''
mark=70
if mark>=90:
    print("u are in grade A")
elif mark>=70:
    print("u are in grade b")
elif mark>=50:
    print("u are in grade c")
else:
    print("u are fail. keep try to pass") 

# FOR NESTED IF AND ELSE CONDITION  
'''import sys
input=(sys.argv[1])
input1=(sys.argv[2])
lisence=input1
age=int(input) '''
age=30
lisence="yes"
if age>=18:
    if lisence=="yes":
        print("u can drive")
    else:
        print("u need to apply for lisence")
else:
    print("u are too young")       

# AND IN IF & ELSE CONDITION  
mark=60
attendance=76
if mark>=50 and attendance>=70: # in this line we use "and " as nested if condition 
    print("yes u are eligible to write exam ")
else:
    print("you are not")           

# OR IN IF & ELSE CONDITION
'''import sys
input=sys.argv[1]
input1=sys.argv[2]
recharge_amount=int(input) # here we have to change the input type because defaut data types is string
data_qunatity=int(input1)'''

recharge_amount=400
data_qunatity=2
if recharge_amount>=350 or data_qunatity>=2:
    recharge_amount-=recharge_amount*0.2
    print(f"u are eligible for use discount 20% is {recharge_amount}rupees and {data_qunatity}")
else:
    print(f"u have to purchase more than or eaual to 350")    

#MERGED OF 'OR' & 'AND' IN IF CONDITITON
purchased_amu=1000
day="monday"
golden_membership="no"
if (purchased_amu>=1500 and day in ["saturday","sunday"]) or golden_membership=="yes":
#if purchased_amu>=1500 and day=="saturday"and"sunday" or golden_membership=="yes":
    print(f"u have 50% discount on ur purchase {purchased_amu}")
    purchased_amu-=purchased_amu*0.5
    print(f"after 50% dicound ur amo will be {purchased_amu}")
else:
    print("u have to purchase more than 1500")    



      
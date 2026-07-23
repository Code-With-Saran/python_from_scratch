customer_name="sAraN G"
print(customer_name.lower())# to covert to lower case
print(customer_name.upper())# to covert to upper case 
print(customer_name.capitalize())# to covert first letter to capitalize in that word

mobile="9344513738"
masked=mobile[:2]+"******"+mobile[-2:]
print(masked)

# FORMATTED STRING USE CASE
movie_name="KatraTHu TaMIL"
director_name="RAm SP"
formatted=f"{movie_name.title()} - {director_name.title()}" """to formatted as tittle case here
 the words first letter should converted into upper case"""
print(formatted)

# REPLACE STRING USE CASE 
location="salem"
fixedlocation=location.replace("salem","Bangalore")
print(fixedlocation)

#SPLIT STRING USE CASE
message_alert="your otp is 287645. Keep it safe"
otp=message_alert.split(".")[0].split("is")[1].strip() # split is use to split with keyword like . or any thing
# strip is used to remove the space in that and 0 and 1 are cose the index for that
print(otp)

#SEARCH STRING USE CASE
Cuopen_message="Your coupen ID id MASS123456. To use this for discount"
if "MASS123456" in Cuopen_message:
    print("your are eligible for discount")

#INDEX POSITION STRING USE CASE
message="hi welcome to the new town , where do u want go"
print("your index position is:",message.find("town"))

#TO FIND THE INITIAL OF NAME
name="saran gopinath priya"
initial=".".join([word[0].upper()for word in name.split()]) 
''' here word of 0 is not saran as 0 gopinath as 1 and priya as 2 , when it in loop the saran, gopinagth, priya as word
and the 0 for thier first index value of that words so the result will be in S G P'''
print(initial)

#TO REMOVE THE UNWANTED SPACE IN INPUT
spaced_input="  saran  "
clean=spaced_input.strip() # strip function is used to remove the unwanted space in the inputs
print(clean)

# TO COUNT THE NO.OF.WORD IN THE STRING
sentence="hi all welcome to the graet evening to explore the fun street game around u"
count=len(sentence.split())
print(count)


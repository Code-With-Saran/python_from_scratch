recieved_amo=(int(input("Recieved Amount :")))
print("U purchased : ",recieved_amo)
gst=recieved_amo*0.18
total=recieved_amo+gst
print(f"Your total amount after gst : {total}")
if recieved_amo>=1200:
    discount=total*0.10
    total-=discount
    print(f"After 10% discount : {total} ")
else:
    print(f"Your purchased cost is not applicable for discount, if want discount u must purchse 1200 or above")   
print("Thank u for purchasing our shop!!!!!!!") 
    
#logical operations 
print("Welcome to show ticket booking platform") 
user=(int(input("Enter the age : ")))
student=(input("are u student: "))
if user>=65 or student=="yes":
    print(f"your 50% offer is applicable for u")
else:
    print(f"u are not eligible to 50% discount")   
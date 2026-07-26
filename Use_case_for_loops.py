# CREATION OF COUNTDOWN TIMER USING WHILE LOOP
count=10
while count>=0:
    print(f"COUNTDOWN : {count}")
    count-=1 
    """Here we decrement the value without assign third variable or another, it assign same variable in that line"""
print("Time's up")    

# CREATE CART TO ADD ITEMS IN IT USGING WHILE LOOP
items=[]
while True: # True is used for infinite loop
    item=input("add your item in the cart if finiesh to type done : ")
    if item.lower()=="done": # Here the condition for the while loop
        break
    items.append(item)
print("Item in the cart :",items)

# FOR LOOP
'''When the limits reach it end from loop'''
name=['saran','sachin','priya','gopinath','santhos','bala'] 
for upper in name:
    print(upper.upper())

# WHILE LOOP 
'''When the condition is satiesfied it end from its loop'''
correct_pin='12345'
entered_pin=''
while entered_pin!=correct_pin:
    entered_pin=input('enter the correct pin : ')
print('acces granted ')    

# BREAK FUNCTION IN FOR LOOP 
'''When we want to braek the loop or stop the lopp we use beak function in it'''
for i in range(10):
    if i==6:
        break
    print(i)
id=[1,2,4,5,6,7,3,8,9,]
for u in id:
    if u==3:
        break
    print(u)

# CONTINUE FUNCTION IN FOR LOOP
'''It will skip the condition and continue the process in thta loop'''
print("CONTINUE FUNCTION ")
num=[1,-8,2,-9,3,4,5,6,7]    
for no in num:
    if no<0: # here when 'no' is lees than zero it skip the condition and continue the process
        continue
    print(no)

# PASS CONDITION IN LOOP
num=[1,-8,2,-9,3,4,5,6,7]    
for no in num:
    pass # Here pass will work as to pass the function in it for future implementation logics


    

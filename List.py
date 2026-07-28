# LIST IN PYTHON
song=["tamil","english","hindi","malayalam","tegulu","marati","kanadam","urudu","bengali"]
auhtor=["saran","saran","saran","saran","saran","saran","saran","saran","saran","saran",]
food=["idly","dosa","biriyani","rice"]
city=["salem","coimbatore","bengalore"]
print("song",song)
print("food",food)
print("city",city)

#LIST METHODS
# APPEND IN LIST 
food.append("dhalrice") # here appen is to add the value in from last only
print("after append",food)

#INSERT IN LIST
food.insert(2,"curdrice") # To insert the value based on the index 
print("after insert",food)

#REMOVE METHOD IN LIST
food.remove("dosa")# To reove the particular value in that list we use remove method in it
print("after reome",food)

#POP METHOD IN LIST
food.pop()# To remove the value from last in the list
print("after pop",food)

#REVERSE METHOD IN LIST
food.reverse()# To reverse the list 
print("after reverse",food)

#TO FIND INDEX VALUE IN THE LIST
print("index value",food.count("biriyani")) # to find the index value in the list we use the count()

#LIST SLICING
print(food[0:2]) # Here it shows the index value from 0 to 1 only it will exclude the 2 index position 
print(city[:]) # create the shallow copy of that entire list
print(song[:9]) # gets everything from the list upto index 8

# LIST SLICING USING STEP ARGUMENTS
#print(song[::2]) # Selects every second element (even indices: 0, 2, 4...).
#print(song[1::2]) #Selects every second element starting from index 1 (odd indices: 1, 3, 5...).
#print(song[::3]) #Selects every third element.

#LIST SLICING USING NEGATIVE INDEXING 
#print(song[-3:]) #Gets the last three items.
#print(song[:-2]) #Gets everything except the last two items.
#print(song[::-1]) #A famous Python trick to reverse the entire list.
print(song[-1:])

#LIST ITERATION USE CASE
for foods in food:
    print("your selected menu is",foods)

#ADD THE VALUE IN THE LIST 
for s in song:
    print(s+" by saran")

# TO ADD THE LISTS     
for a in auhtor:
    for s in song:
        print(s+a)

# CHECK THE VALUE PRESENT IN THE LIST
if "tamil" in song:
    print("it present in the song")

# TO CHANGE THE VALUE IN THE LIST USING INDEX VALUE
print(food)
food[3]="chickenrice"
print("after update", food)

# LIST SUPPORT ALL TYPE OF DATA TYPE
data=["saran",23,45.89]
for y in data:
    print(y)

# TO FIND THER INDEX VALUE OF THE LIST
for idex,value in enumerate(song): 
    # this function is spilt the index and value and stored in assigned value here 'idex' and 'value'
    print(f"index {idex} : {value}")




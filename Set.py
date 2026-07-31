# SET
'''it is unordered, it doesn't have index value
it removes the duplicate value 
'''
city=["salem","chennai",'salem','chennai','banglore']
after_remove_duplicate_value=set(city)
print(after_remove_duplicate_value)

# TO FIND THE UNION
town1={'salem','chennai','coimbatore','erode'}
town2={'salem','mettur','namakkal','erode','ooty'}
print(town1.union(town2))

# TO FIND INTERSECTION
town1={'salem','chennai','coimbatore','erode'}
town2={'salem','mettur','namakkal','erode','ooty'}
print(town1.intersection(town2))

# TO FIND DIFFERENCE
town1={'salem','chennai','coimbatore','erode'}
town2={'salem','mettur','namakkal','erode','ooty'}
print(town1.difference(town2)) #here we find the difference in town1 only
print(town2.difference(town1)) #here we find the difference in town2 only

# TO ADD THE VALUE IN SET
town1.add("dharmapuri") 
#we only add the valuein that, we cant access the index value in it because set doesn't have index
print(town1)

# TO REMOVE THE VALUE IN SET
town1.remove("erode")
print(town1)

# IF WE WANT TO REMOVE AND ADD THE VALUE IN IT
town1.remove("coimbatore")
town1.add("kodaikanal")
print(town1)

# TO SAFE REMOVE THE VALUE IF IT PRESENT IT DO OR OTHERWISE IT LEAVE IT
town1.discard('erode') 
'''here the discard function is used to remove the value form set with safly. 
if that value is present it will reove the value or other wise it shold leave it'''
print(town1)

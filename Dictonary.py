order={"order id":"12345",
"item":"dosa",
"cost":150,
"pay mtd":"upi",
"from":"market",
"delivered":"salem pothys"}

# LOOK UP IN DICTONARY
print(order["delivered"])

# GET METHOD IN DICTONARY
print(order.get("from")) 
# here we access the key safly if it present in that list it execute or it shows none not shows error
print(order.get("upi"))

# TO GET KEYS IN THE DICTONARY
print(order.keys()) 

# TO GET VALUES IN DICTONARY
print(order.values())

# ITERATION IN DICTONARY
for key,value in order.items():
    print(key,':',value)

# TO UPDATE THE KEY AND VALUE IN DICTONARY
order.update({"status":"delivered"})
print(order)

# TO POP THE DICTONARY
'''print(".................................")
order.pop("pay mtd")
print(order)'''

# UPSET IN DICTONARY
order.update({"status":"processing"}) 
#here the key is alredy present in dictonary so it should upset the value to that key(status)
print(order)

# TO CHECK DUPIICATE AND UPDATE ITSELF AS LATEST VALUE IN DICTONARY
order1={"order id":"12345",
"item":"dosa",
"cost":150,
"pay mtd":"upi",
"from":"market",
"delivered":"salem pothys",
"order id":"123457890"}
'''here the order id is comes twice first it will take orde id as 12345 after,
 when it comes second order id it accept latest order id in it'''
for key,value in order1.items():
    print(key,':',value)

# MULTIPELVALUES IN ONE KEY
order2={"order id":"12345",
"item":"dosa",
"cost":150,
"pay mtd":"upi",
"from":"market",
"delivered":["salem","railway station","omulor"],# here we have multi value based on one key
"order id":"123457890"}
for key,value in order2.items():
    print(key,":",value)

# TO ACCESS THE MULTI VALUE IN A KEY
print(order2["delivered"][2]) # here this line shpold access the values in key(delivered)

# TO ITERATE KEY CONTAINS MORE VALUE
for location in order2["delivered"]:
    print(location) # here it execute the values in delivered key loaction

# TO HANDELLING MULTIPLE DICTONARY THROUGH LIST
travel_history=[{"travel id":"12345","from":"salem","drop":"chennai","cost":"2500"},
{"travel id":"12346","from":"chennai","drop":"salem","cost":"3500"},
{"travel id":"12347","from":"bangalore","drop":"hosur","cost":"4500"},
{"travel id":"12348","from":"madurai","drop":"tenkasi","cost":"500"}]    

for travel in travel_history:
    print(travel["travel id"]) # here we access the travel ids in travel_history

# TO HANDELLING MULTIPLE DICTONARY THROUGH DICTONARY
travel_history={"12345":{"travel id":"12345","from":"salem","drop":"chennai","cost":"2500"},
"12346":{"travel id":"12346","from":"chennai","drop":"salem","cost":"3500"},
"12347":{"travel id":"12347","from":"bangalore","drop":"hosur","cost":"4500"},
"12348":{"travel id":"12348","from":"madurai","drop":"tenkasi","cost":"500"}}
print(travel_history["12345"]["cost"]) # here we call the two keys to execute this

# TO HANDELLING ITERATION IN MULTIPLE DICTONARY THROUGH DICTONARY
for id,value in travel_history.items(): 
    # items is segregate the keys and values seperately here keys are 12345,12346,12347,12348 and values
    print("your travel id:", id)
    print("Start from:", value["from"],"--->","your destination:", value["drop"],"/ your cost:", value["cost"])
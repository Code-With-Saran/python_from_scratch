# TUPLE IN PYTHON 
'''Its like list apart from its immutable'''
travel_summary=("rapido","salem","airport",45.00,"completed")
print(travel_summary)

# TO FIND THE INDEX VALUE IN THE TUPLE
print(travel_summary[1])

# USE CASE OF FOR LOOP IN THE TUPLE
for a in travel_summary:
    print(a)

# TO find the length of tuple
print("length of tuple:" ,len(travel_summary))

# TO FIND THE COUNT OF TUPLE
print("count of thta value:" ,travel_summary.count("salem")) 
# here count function is count the value salem in the tuplehow many times it present the list

# TO FIND THE INDEX OF THE TUPLE
print("index value:", travel_summary.index("completed")) #here index function is to find the index position of that value
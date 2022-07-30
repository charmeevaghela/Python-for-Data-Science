# in python there is not any json data type but we work with dictionaries as json 
# json module is there for treating it as json 

# creating a nested dictionary phone book 

book = {}
book["charmee"]={
    "name": "charmee",
    "phone" : 90909090,
    "list" : ["hi", "kpop",1]
}
book["shivani"]={
    "name" : "shivani",
    "phone" : 9494949
}

import json 
jsonstr = json.dumps(book,indent=4)  # indent is used to format the json string , dumps converts the python object to json 
# print(jsonstr)
with open("pyfile.txt","w") as file:
    file.write(jsonstr)
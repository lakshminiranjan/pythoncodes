#dicitionary = A changeable,unordered collection of unique key : value paires
#they are fast because they use hashing,allow us to access a value quickly

capitals = {"Andhra-Pradesh":"Amaravathi",
"Telangana":"Hyderabad",
"Tamil-Nadu":"Chennai"}

capitals.update({"Karnataka":"Banglore"})#adds a new key,value pair
capitals.update({"Andhra-Pradesh":"Kadapa"})
capitals.pop("Karnataka")#removes the given key,value pair in the dict
capitals.clear()#clears everything of a dict

# print(capitals["Andhra-Pradesh"])
print(capitals.get("Assam"))#safer way to print the value which is mapped to the given key
# print(capitals.keys())#prints only the keys
# print(capitals.values())--prints only the values

# print(capitals.items())--prints the entire dict

for key,value in capitals.items():
    print(key,value)
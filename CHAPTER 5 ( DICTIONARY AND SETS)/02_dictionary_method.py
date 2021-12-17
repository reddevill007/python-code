myDictionary = {
    "Fast": "in a quick manner",  # duplicate keys can not be used
    "Happy": "Snappy",
    "marks": [1, 2, 5],
    "anotherdict": {'saurabh': 'player'}
}

# dictionary methods

print(myDictionary.keys()) # prints the keys of the dictionary

print(myDictionary.values()) # prints the values of the dictionary

print(myDictionary.items()) # prints all the key value pair of the dictionary in the form of tuples

# updating the dictionary items

updatedictionary={
    "harry":"friends",
    "harman":"friends", 
    "Happy": "Singer", #changes happy snappy to happy singer
    "sukh":"friends"
} #another dictionary which you want to add or update in main dictionary
myDictionary.update(updatedictionary) # updates the mydictionary with all key value pair from updatedictionary
print(myDictionary)

print(myDictionary.get("Happy")) #prints value associated with key happy2
print(myDictionary["Happy"]) #prints value associated with key happy2

# difference between .get and simple calling
# print(myDictionary.get("Happy2")) #returns none as happy2 is not present in the dictionary
# print(myDictionary["Happy2"]) #throws error as happy2 is not present in the dictionary




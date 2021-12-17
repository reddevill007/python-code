myDictionary = {
    "Fast": "in a quick manner", #duplicate keys can not be used
    "Happy": "Snappy",
    "marks" : [1,2,5],
    "anotherdict":{'saurabh': 'player'}
}
print(myDictionary['anotherdict']['saurabh'])

# print(myDictionary['Fast'])
# print(myDictionary["Happy"])

myDictionary['marks']=[45,76] # --> dictionary is mutasble ie its value can be changed
print(myDictionary["marks"])
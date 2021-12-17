# creating empty set
b=set()

# adding values to an empty set
b.add(1)
b.add(2)
b.add(3)
b.add(4) #adding same value repeaditily doesnt work
b.add(5)
#we can not add as it is unhashable and not even dictionary
print(b)

print(len(b)) #prints the length of the set

b.remove(5) #remove 5 from the set if elent is not  present throws key error
print(b)

print(b.pop()) #remove any arbitrary element and returns the element remove

print(b.clear()) # make the set as empty set

#using union and intersection
d={67,78,90,1,2,3,4}
e={1,2,3,4,5,6,7}
print(e.union(d))
print(e.intersection(d))

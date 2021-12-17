
f=open('sample.txt') 

# reads first line
data = f.readline()
print(data)

# reads second line
data = f.readline()
print(data)

# reads third line
data = f.readline()
print(data)

# reads fourth line and so on.....
data = f.readline()
print(data)
f.close
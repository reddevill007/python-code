f=open('poems.txt')
t=f.read()
if 'twinkle' in t:
    print("yes")
else:
    print("no")
f.close()
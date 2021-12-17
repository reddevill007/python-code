a = int(input("Enter the number whoes multiplication yable you want: "))
print("The required multiplication table of ", a, "is:")
i=1
while i<=10:
    # print(a," X ",i,"=",a*i)
    # print(str(a)+" X "+str(i)+"="+str(a*i))
    print(f"{a} X {i} = {a*i}")
    i=i+1

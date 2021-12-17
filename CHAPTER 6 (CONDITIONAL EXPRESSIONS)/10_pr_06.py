a=int(input("Enter your marks: "))

if a>90 and a<100:
    print("Your grade is 'Ex'")

elif a>80 and a<90:
    print("Your grade is 'A'")
    
elif a>70 and a<80:
    print("Your grade is 'B'")

elif a>60 and a<70:
    print("Your grade is 'C'")

elif a>50 and a<60:
    print("Your grade is 'D'")

elif a<50:
    print("Your grade is 'F'")

else:
    print("Invalid mrks entry")


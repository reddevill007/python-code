a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))

# if a==b and b==c and c==d and d==a:
#     print("All four numbes are equal")

# elif a>=b and a>=c and a>= d:
#     print("First number is greatest")
    
# elif b>=c and b>=c and b>= d:
#     print("second number is greatest")
        
# elif c>=b and c>=a and c>= d:
#     print("third number is greatest")
    
# elif d>=b and d>=c and d>= a:
#     print("Fourth number is greatest")

if a>d:
    f1=a
else:
    f1=d

if b>c:
    f2=b
else:
    f2=c

if f1>f2:
    print(str(f1) + " is greatest")
else:
    print(str(f2) + " is greatest")
    


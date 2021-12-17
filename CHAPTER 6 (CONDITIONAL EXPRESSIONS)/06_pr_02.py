sub1 = int(input("Enter  marks of sub1: "))
sub2 = int(input("Enter  marks of sub2: "))
sub3 = int(input("Enter  marks of sub3: "))

if sub1<33 or sub2<33 or sub3<33:
    print("You are failed")
elif (sub1+sub2+sub3)/3 <40:
    print("You are failed as your total percentage is less than 40")
else:
    print("Congratulations!!  you pass")

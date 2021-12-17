# n = 4
# product=1
# for i in range(n):
#     product = product*(i+1)
# print(product)

def factorial_recusive(n):
    if n==1 or n==0:
        return 1
    return n*factorial_recusive(n-1)
print("\t\t\t***********************************************\t\t\t")
print("\t\t\t\t\t\t\t\t\tFACTORIAL CALCULATOR\t\t\t\t")
print("\t\t\t***********************************************\t\t\t")
a=int(input("Enter the number whose factorial you want:"))
f=factorial_recusive(a)
print("\t\t\t***********************************************\t\t\t")
print("the factorial of ",a, " is ",f)
print("\t\t\t***********************************************\t\t\t")

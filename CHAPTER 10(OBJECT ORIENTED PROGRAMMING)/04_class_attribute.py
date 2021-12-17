class Employee:
    company="Google"
    salary=100
# class attribute is changed for all objects
saurabh=Employee()
shivam=Employee()
print(saurabh.company)
print(shivam.company)
Employee.company="YouTube"
print(saurabh.company)
print(shivam.company)

# instance attribute
saurabh.salary=300
shivam.salary=400
print(saurabh.salary)
print(shivam.salary)

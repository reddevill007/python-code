class Employee:
    company="Google"

    def showDetails(self):
        print("This is an emoloyee")

class Programmer(Employee):
    # child class can overwrite attributes of parent class
    language = "Python"
    company = "YouTube"
    def getLang(self):
        print(f"The language is {self.language}")

    def showDetails(self):
        print("This is a programer")

e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)

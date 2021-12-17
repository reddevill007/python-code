class Employee:
    company = "visa"
    eCode = 120
class Freelancer:
    company = "Fiverr"
    level = 0
    def upgradeLevel(self):
        self.level = self.level + 1
class Programmer(Employee, Freelancer):
    name = "Saurabh"

p = Programmer()
print(p.level)
p.upgradeLevel()
print(p.level)
print(p.company) #copany will be visa as we called Employee class first
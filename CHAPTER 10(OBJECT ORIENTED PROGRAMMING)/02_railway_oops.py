class RailwayForm:
    fromType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train name is {self.train}")

saurabhApplication = RailwayForm()
saurabhApplication.name="Saurabh"
saurabhApplication.train="Garib Rath"
saurabhApplication.printData()
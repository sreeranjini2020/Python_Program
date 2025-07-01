class Employee:
    def __init__(self, name, id , department):
        self.name = name
        self.id = id
        self.department = department
    
    def show_details(self):
        print(f"The empolyee name is {self.name}, whose id is {self.id} and from {self.department} department ")

empolyee1 = Employee("Riya", "SN1003", "Enginnering")
empolyee1.show_details()
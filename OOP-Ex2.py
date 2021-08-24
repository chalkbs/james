# Example 2
class Person:
    # attributes
    name = ""
    address = ""
    # methods
    def __init__(self, name, address):
        self.name = name
        self.address = address
    def setName(self, name):
        self.name = name
    def getName(self):
        return (self.name)
    def setAddress(self, address):
        self.address = address
    def getAddress(self):
        return (self.address)

#now create some people
p1 = Person("James", "Somewhere in Leeds")
p2 = Person("Bernard", "Somewhere in Southend")

p3 = Person("Abigail", "Somewhere in London")

#now interact with the objects using the class methods
print (p1.getName())
print (p2.getAddress())
p1.setAddress("Somewhere in Shoeburyness")
print (p1.getAddress())


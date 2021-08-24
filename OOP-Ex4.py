# Example 4
class Person:
    # attributes
    __name = ""      #use a double underscore for private attribute
    __address = ""   #use a double underscore for private attribute
    # methods
    def __init__(self, giveName, givenAddress):
        self.__name = giveName
        self.__address = givenAddress
    def outputName(self):
        return (self.__name)
    def outputAddress(self):
        return (self.__address)
    def setName(self, newName):
        self.__name = newName
    def setAddress(self, newAddress):
        self.__address = newAddress

class Employee(Person):
    __ni_number = ""
    def __init__(self, givenName, givenAddress, ni_number):
       Person.__init__(self, givenName, givenAddress)
       self.__ni_number = ni_number
    def outputNiNumber(self):
        return (self.__ni_number)
    def setNiNumber(self, niNumber):
        self.__ni_number = niNumber

p4 = Employee("Jane", "Cheltenham", "A45765765")
print (p4.outputName())
print(p4.outputNiNumber())
p4.setAddress("Gloucester")
print (p4.outputAddress())

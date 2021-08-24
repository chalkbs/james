# Example 3
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

p3 = Person("Abigail", "Somewhere in London")
print(p3.__name)    # 'Person' object has no attribute '__name'

print(p3.outputName())  # Abigail

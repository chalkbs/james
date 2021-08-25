# Example 2
class Person:
    # attributes
    name = ""
    address = ""

    # methods
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address


# now create some people
p1 = Person("James", "Somewhere in Leeds")
p2 = Person("Bernard", "Somewhere in Southend")

p3 = Person("Abigail", "Somewhere in London")

# now interact with the objects using the class methods
print(p1.get_name())
print(p2.get_address())
p1.set_address("Somewhere in Shoeburyness")
print(p1.get_address())

# Example 4
class Person:
    # attributes
    __name = ""  # use a double underscore for private attribute
    __address = ""  # use a double underscore for private attribute

    # methods
    def __init__(self, given_name, given_address):
        self.__name = given_name
        self.__address = given_address

    def output_name(self):
        return self.__name

    def output_address(self):
        return self.__address

    def set_name(self, new_name):
        self.__name = new_name

    def set_address(self, new_address):
        self.__address = new_address


class Employee(Person):
    __ni_number = ""

    def __init__(self, given_name, given_address, ni_number):
        Person.__init__(self, given_name, given_address)
        self.__ni_number = ni_number

    def output_ni_number(self):
        return self.__ni_number

    def set_ni_number(self, niNumber):
        self.__ni_number = niNumber


p4 = Employee("Jane", "Cheltenham", "A45765765")
print(p4.output_name())
print(p4.output_ni_number())
p4.set_address("Gloucester")
print(p4.output_address())

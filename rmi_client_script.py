import Pyro4

# Creating a person class
class Person(object):
    def __init__(self, name):
        self.name = name

    def visit(self, warehouse):
        print(f"Hello, {name}.")
        self.deposit(warehouse)
        self.retrieve(warehouse)
        print("Thank you, come again!")

    def deposit(self, warehouse):
        print("The warehouse contains:", warehouse.getData())
        item = input("Enter a car you want to sell: ").strip()
        if item:
            warehouse.storeData(self.name, item)

    def retrieve(self, warehouse):
        print("The warehouse contains:", warehouse.getData())
        item = input("Enter a car you want to buy: ").strip()
        if item:
            warehouse.takeData(self.name, item)



# client script
# URI of the remote Object
uri = "PYRONAME:my_warehouse"

# Proxy connects to Remote object and executes RPC
warehouse = Pyro4.Proxy(uri)

name = input("Enter Your Name: ")
person1 = Person(name)
person1.visit(warehouse) 

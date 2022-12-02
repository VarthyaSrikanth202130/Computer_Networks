import Pyro4

# Creating a warehouset of cars available;
# Decorator to mark a method or class to be exposed for remote calls;
@Pyro4.expose
class Warehouse :
    def __init__(self) -> None:
        self.data = ["FORD" , "MERCEDIES" , "MAHENDRA_THAR" , "BUGATTI" , "LAMBORGINI" , "TATA_NANO"]
        
    def getData(self):
        return self.data
    
    def storeData(self,name,item):
        self.data.append(item)
        print(f"\"{item}\" is sold by {name}")
        
    def takeData(self,name,item):
        self.data.remove(item)
        print(f"\"{item}\" is purchased by {name}")




# create a server and listens for the method calls
Pyro4.Daemon.serveSimple(
    { Warehouse : "my_warehouse"},
    ns = True
)


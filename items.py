import csv # imports csv module to read data from csv file

class Item:
    discount = 0.7
    all_items = [] # a class list that holds all the instances of the item class.


    def __init__(self,name: str, price:float, quantity=0): #allows for when a new object of the class is created it gives values for name, price and quantity 
        assert price >= 0, f"Price {price} is not greater than or equal to zero" #price is not a negative number 
        assert quantity >=0, f"Quantity {quantity} is not greater than zero" #quantity is not a negative number 

        self.__name = name # stores the name as a privarte varaible so cannot be accesed from outside the class  
        self.__price = price # stores the prices privately 
        self.quantity = quantity #store the quantity 

        Item.all_items.append(self) #adds the current instance to the all_items list and keeps tracks the objects created 


    @property #allows you to define a method (item.total_price) so you can access it like a regualar variable 
    def total_price(self):
        return self.__price * self.quantity #calcuates total price by multiply price by quantity 

    def apply_discount(self):
        self.__price *= self.discount #this method applies a discount of 30% to the price by multiplying by 0.7
 
    @property
    def name(self):
        return self.__name 

    @name.setter # access the item.name even though its a private variable 
    def name(self, value):
        if len(value) > 10:
            raise ValueError("This name is too long") # the setter checks if the name is longer than 10 charchter and will print the message if so 


    @classmethod #allows creating item instances for the data from the csv files 
    def from_csv(cls):
        with open ('items.csv','r') as file:
            reader = csv.DictReader(file)
            for item in reader:
                cls(
                    name=item['name'],
                    price=float(item['price']),
                    quantity =int(item['quantity']), # converts the price and quantity into appropriate 


              )
                
def __repr__(self):
    return f"{self.__class__.__name__}('{self.name}',{self.price}, {self.quantity})"







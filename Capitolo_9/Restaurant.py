class Restaurant:
    """class to define some stuff about restaurants object"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initializa restaurant name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Show information about restaurant istance"""
        print(f"The restaurant name is {self.restaurant_name} and the type of cuisine is {self.cuisine_type}\n")
    
    def open_restaurant(self):
        """Inform that the restaurant is open"""
        print(f"{self.restaurant_name} is open!")


class IceCreamStand(Restaurant):
    """Represent a specific kind of restaurant"""

    def __init__(self,restaurant_name, cuisine_type):
        """
        Initialize attributes of the parent class
        The initialize attributes specific type of restaurant
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['panna','cioccolato','crema', 'pistacchio','amarena'] 

    def describe_flavors(self):
        """A method to describe the flavours"""
        print("\nAt this moment we have these flavors:")
        for flavor in self.flavors:
            print(f"-- {flavor} --")

            

my_ice_cream = IceCreamStand('19 gradi','Gelateria')
my_ice_cream.describe_restaurant()
my_ice_cream.describe_flavors()

#restaurant = Restaurant('La casetta','Romana')
#restaurant_1 = Restaurant('Bar flory','Romana')
#restaurant_2 =Restaurant('Da Mario','Napoletana')

#restaurant.describe_restaurant()
#restaurant_1.describe_restaurant()
#restaurant_2.describe_restaurant()
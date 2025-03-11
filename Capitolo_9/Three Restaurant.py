class Restaurant:
    """class to define some stuff about restaurants object"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initializa restaurant name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Show information about restaurant istance"""
        print(f"The restaurant name is {self.restaurant_name} and the type of cuisine is {self.cuisine_type}")
    
    def open_restaurant(self):
        """Inform that the restaurant is open"""
        print(f"{self.restaurant_name} is open!")

restaurant = Restaurant('La casetta','Romana')
print(f"The restaurant name is {restaurant.restaurant_name}.")
print(f"The cuisine type is {restaurant.cuisine_type}.")

restaurant.describe_restaurant()
restaurant.open_restaurant()
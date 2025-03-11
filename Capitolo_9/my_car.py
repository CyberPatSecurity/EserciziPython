class Battery:
    """A simple attempt to model the battery size."""

    def __init__(self, battery_size=8):
        """Initialize the battery's attribute"""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print a statement describing battery size."""
        print(f"This car has a {self.battery_size}-Kwh battery.")
    
    def get_range(self):
        """Print a statement about the range this battery provides"""
        range = 0
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge")

    def upgrade_battery(self):
        """Upgrade the battery size to 100Kwh if it is lower than 100."""
        if self.battery_size < 100:
            self.battery_size = 100
            print("Battery upgraded to 100 Kwh.")
        else:
            print("Battery is already at maximum capacity.")


class ElectricCar(Car):
    """Represent aspects of a car specific to electric vehicles.""" 

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class
        Then initialize attributes specific to an electric car
        """
        super().__init__(make, model, year)
        self.battery = Battery()
   
    
my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print("\nUpgrading battery...")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

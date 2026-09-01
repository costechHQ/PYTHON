# Parent class from your previous work
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type="Ice Cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
        
    def display_flavors(self):
        print(f"\n--- Available Flavors at {self.restaurant_name} ---")
        for flavor in self.flavors:
            print(f"- {flavor}")


my_stand = IceCreamStand("Scoops & Dreams")
my_stand.flavors = ["Vanilla", "Dark Chocolate", "Mint Chip", "Mango Sorbet"]

my_stand.describe_restaurant() 
my_stand.display_flavors()       

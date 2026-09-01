class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name}, is open")

    def set_number_served(self, total_served):
        """Set the number of customers served to a specific value."""
        self.number_served = total_served

    def increment_number_served(self, new_served):
        """Add a specific amount of customers to the total served."""
        self.number_served += new_served


restaurant = Restaurant("Sky Light", "Arabian")


print(f"Initial numbers served: {restaurant.number_served}")

restaurant.number_served = 12
print(f"Directly updated numbers served: {restaurant.number_served}")

restaurant.set_number_served(50)
print(f"Set number served via method: {restaurant.number_served}")


restaurant.increment_number_served(35)
print(f"Final incremented numbers served: {restaurant.number_served}")

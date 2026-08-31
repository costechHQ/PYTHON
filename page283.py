class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name}, is open")

restaurant = Restaurant("Sky Light", "Arabian")
print(f"Name Attribute: {restaurant.restaurant_name}")
print(f"Cuisine Attribute: {restaurant.cuisine_type}")
print()

restaurant.describe_restaurant()
restaurant.open_restaurant()

print("\n" + "="*30 + "\n")

#9.2
restaurant1 = Restaurant("De Castle", "Local")
restaurant2 = Restaurant("HSB Hotel", "French")
restaurant3 = Restaurant("Hotel Majestic", "Italian")

restaurant1.describe_restaurant()
print()
restaurant2.describe_restaurant()
print()
restaurant3.describe_restaurant()

print("\n" + "="*30 + "\n")




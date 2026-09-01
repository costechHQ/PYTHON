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



class User:
    """class for user"""
    def __init__(self, first_name, last_name, age, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.occupation = occupation

    def describe_user(self):
        """summary of the user’s information"""

        print("\n--- Users details ----")
        print(f"\nName: {self.first_name} {self.last_name}")
        print(f"Age {self.age}")
        print(f"Occupation: {self.occupation}")

    def greet_user(self):
        """personalized greeting to the user"""
        print(f"\nHello, {self.first_name}, thanks you for logging in today")

user1 = User("Onyedika", "Christopher", 30, "Software Engineer")
user1.describe_user()
user1.greet_user()

user2 = User("Ifeanyi", "Charlse", 28, "Software Engineer")
user2.describe_user()
user2.greet_user()

user3 = User("Loveth", "black", 26, "Software Engineer")
user3.describe_user()
user3.greet_user()

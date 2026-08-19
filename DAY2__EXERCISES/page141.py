#4.10
cubes = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
print(f"1. Generated List: {cubes}\n \n")
print("The first three items in the list are:")
print(f"{cubes[:3]} \n \n")
print("The last three items in the list are:")
print(f"{cubes[-3:]} \n \n")

#4.11
my_pizzas = ["Pepperoni", "Margherita", "BBQ Chiken"]

friend_pizzas = my_pizzas[:]

my_pizzas.append("Spicy Supreme")
friend_pizzas.append("Four cheese")

print("\n My favorite pizzas are:")
for pizza in my_pizzas:
    print(f"- {pizza}")

print("\n My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")
print("\n" + "="*40 + "\n")

#4.12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli']

print("My favorite food are:")
for food in my_foods:
    print(f"I love eating: {food}")

print("\nMy Friend's favorite food are:")
for food in friend_foods:
    print(f"He loves eating: {food}")

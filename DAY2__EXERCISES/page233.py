print("--- 7-8 & 7-9. Deli Order Processing ---")
sandwich_orders = [
    "tuna", "pastrami", "turkey", "pastrami", 
    "roast beef", "pastrami", "italian sub"
]
finished_sandwiches = []

print("Attention Customers: The deli has completely run out of pastrami today!\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(f"Verified remaining orders queue: {sandwich_orders}\n")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0) 
    
    print(f" I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n--- Completed Orders ---")
for sandwich in finished_sandwiches:
    print(f" {sandwich.title()} Sandwich")

print("\n" + "="*40 + "\n")

# 7-10. 

responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    location = input("If you could visit one place in the world, where would you go? ")
    
    responses[name] = location
    
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, place in responses.items():
    print(f"👤 {name.title()} wants to go to {place.title()}.")

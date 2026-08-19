#4.13

buffet_foods = ("Fried rice", "Spaghetti", "Abacha", "Friend chiken", "Steamed rice")

print("This Restaurant offers:")
for food in buffet_foods:
    print(f"-{food}")
print("="*64)

try:
    buffet_foods[0] = "Beans"
except TypeError as error:
    print(f"CRASH PREVENTED! {error}")
print("="*64 + "\n")

buffet_foods = ("Roast Beef", "Smoke fish", "Fried egg", "Indomie")

for food in buffet_foods:
    print(f"-{food}")

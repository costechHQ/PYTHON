def make_shirt(size, message):
    """summerizes a custom printed shirt order."""
    print(f"a {size}-sized shirt will be printed with: '{message}'")

make_shirt("Medium", "Code Everyday")

make_shirt(size="Medium", message="Code Everyday")

print("\n" + "="*60 + "\n")

#8.4 
def make_shirt_default(size="Large", message="I love Python"):
    """Summerizes a shirt order using system fallbacks."""
    print(f"A {size}-sized shirt will be printed with: '{message}'")

make_shirt_default()
make_shirt_default(size="Medium")

make_shirt_default(size="Small", message="Python is Fun")

print("\n" + "="*60 + "\n")

#8.5
def describe_city(city, country="Iceland"):
    print(f"{city.title()} is in {country.title()}.")

describe_city("reykjavik")
describe_city("akureyri")
describe_city("Enugu", country="nigeria")
print("\n" + "="*60 + "\n")




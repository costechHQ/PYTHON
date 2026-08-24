person = {
    'first_name': 'adaeze',
    'last_name': 'eze',
    'age':20,
    'city': 'enugu'
}

print(f"First Name: {person['first_name'].title()}")
print(f"Last Name:  {person['last_name'].title()}")
print(f"Age:        {person['age']}")
print(f"City:       {person['city']}")

print("\n" + "="*40 + "\n")

favorite_numbers = {
    'alice': 7,
    'bob': 42,
    'charlie': 13,
    'david': 3,
    'eva': 99
}

print(f"Alice's favorite number is {favorite_numbers['alice']}.")
print(f"Bob's favorite number is {favorite_numbers['bob']}.")
print(f"Charlie's favorite number is {favorite_numbers['charlie']}.")
print(f"David's favorite number is {favorite_numbers['david']}.")
print(f"Eva's favorite number is {favorite_numbers['eva']}.")

print("\n" + "="*40 + "\n")

favorite_numbers = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    number = int(input("What is your favorite number? "))
    favorite_numbers[name] = number
    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat.lower() == 'no':
        polling_active = False

for name, number in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite number is {number}.")

glossary = {
    'string': 'A series of characters treated as a block of text.',
    'list': 'A collection of items stored in a particular structural order.',
    'loop': 'A block of code that repeats automatically for a set number of times.',
    'boolean': 'A data type that can only hold a value of either True or False.',
    'conditional test': 'An expression that evaluates to determine if a statement is true.'
}

print("\n" + "="*40 + "\n")

word = 'string'
print(f"{word.title()}:\n  {glossary[word]}\n")

word = 'list'
print(f"{word.title()}:\n  {glossary[word]}\n")

word = 'loop'
print(f"{word.title()}:\n  {glossary[word]}\n")

word = 'boolean'
print(f"{word.title()}:\n  {glossary[word]}\n")

word = 'conditional test'
print(f"{word.title()}:\n  {glossary[word]}")
glossary = {
    'string': 'A series of characters treated as a block of text.',
    'list': 'A collection of items stored in a particular structural order.',
    'loop': 'A block of code that repeats automatically for a set number of times.',
    'boolean': 'A data type that can only hold a value of either True or False.',
    'conditional test': 'An expression that evaluates to determine if a statement is true.',
    'dictionary': 'A collection of key-value pairs mapping labels to data.',
    'key': 'The unique identifier label used to find an item in a dictionary.',
    'value': 'The data metric associated with a specific key in a dictionary.',
    'argument': 'A value passed into a function when calling it.',
    'parameter': 'A variable listed inside a function signature definition line.'
}

for term, definition in glossary.items():
    print(f"{term.title()}:\n  {definition}\n")

print("="*40 + "\n")

rivers_map = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}

print("Sentences:\n")
for river, country in rivers_map.items():
    print(f"- The {river.title()} runs through {country.title()}.")

print("\nRivers included in this dictionary:")
for river in rivers_map.keys():
    print(f"- {river.title()}")

print("\nCountries included in this dictionary:")
for country in rivers_map.values():
    print(f"- {country.title()}")

print("\n" + "="*40 + "\n")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

voters_pool = ['sarah', 'matt', 'phil', 'elizabeth', 'jen', 'tim']

for person in voters_pool:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for responding to our developer poll!\n")
    else:
        print(f"Hi, {person.title()}, we noticed you havent't voted yet. pPlease take our poll.\n")

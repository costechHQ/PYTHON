person_1 = {'first': 'sarah', 'last': 'connor', 'age': 29, 'city': 'los angeles'}
person_2 = {'first': 'bruce', 'last': 'wayne', 'age': 34, 'city': 'gotham'}
person_3 = {'first': 'clark', 'last': 'kent', 'age': 32, 'city': 'metropolis'}

people = [person_1, person_2, person_3]

for individual in people:
    full_Name = f"{individual['first']} {individual['last']}".title()
    print(f"Name: {full_Name}")
    print(f"Age:  {individual['age']}")
    print(f"City: {individual['city'].title()}\n")

print("="*40 + "\n")

pet_1 = {'animal': 'dog', 'name': 'buddy', 'owner': 'alice'}
pet_2 = {'animal': 'cat', 'name': 'whiskers', 'owner': 'bob'}
pet_3 = {'animal': 'parrot', 'name': 'echo', 'owner': 'charlie'}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"   Pet Name: {pet['name'].title()}")
    print(f"   Species:  {pet['animal'].title()}")
    print(f"   Owner:    {pet['owner'].title()}\n")

print("="*40 + "\n")

favorite_places = {
    'tony': ['tokyo', 'new york', 'malibu'],
    'selina': ['paris', 'cairo'],
    'arthur': ['atlantis']
}

for person, places in favorite_places.items():
    print(f"{person.title()}'s favorite places are:")
    for place in places:
        print(f"{place.title()}")
    print()

print("="*40 + "\n")

favorite_numbers = {
    'alice': [5, 10],
    'bob': [7, 14],
    'charlie': [13, 7]
}

for name, numbers in favorite_numbers.items():
    num_strings = ", ".join(str(num) for num in numbers)
    print(f"{name.title()}'s lucky choices: {num_strings}")

print("\n" + "="*40 + "\n")

cities = {
    'tokyo': {
        'country': 'japan',
        'population': '14 million',
        'fact': 'It is the most populous metropolitan area in the world.',
        'currency': 'Yen' 
    },
    'reykjavik': {
        'country': 'iceland',
        'population': '130,000',
        'fact': 'It runs entirely on geothermal renewable energy.',
        'currency': 'Krona' 
    },
    'cairo': {
        'country': 'egypt',
        'population': '10 million',
        'fact': 'It is located close to the ancient Giza Pyramid complex.',
        'currency': 'Egyptian Pound' 
    }
}

for city, city_info in cities.items():
    print(f" City: {city.title()}")
    print(f" Country:    {city_info['country'].title()}")
    print(f" Population: {city_info['population']}")
    print(f" Currency:   {city_info['currency']}")
    print(f" Fact:       {city_info['fact']}\n")

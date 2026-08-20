#5.3
alien_color = ['green', 'yellow', 'red']

alien_color = 'green'
if alien_color == 'green':
    print("Version 1 (passess): just earned 5 points.")

alien_color = 'red'
if alien_color == 'green':
    print("This will not print.")
print("="*40 + "\n")

#5.4
alien_color = 'green'
if alien_color == 'green':
    print("You earned 5 points for shooting the alien")
else:
    print("Player just earned 10 points!")

alien_color = 'red'
if alien_color != 'red':
    print("You earned 5 points for shooting the alien")
else:
    print("Player just earned 10 points!")
print("="*40 + "\n")

#5.5
alien_color = 'green'
if alien_color == 'green':
    print("Alien green: You earned 5 points.")
elif alien_color == 'yellow':
    print("Alien yellow: You earned 10 points")
else:
    print("Alien Red: You earned 15 points")

alien_color = 'yellow'
if alien_color == 'green':
    print("Alien green: You earned 5 points.")
elif alien_color == 'yellow':
    print("Alien yellow: You earned 10 points")
else:
    print("Alien Red: You earned 15 points")

alien_color = 'red'
if alien_color == 'green':
    print("Alien green: You earned 5 points.")
elif alien_color == 'yellow':
    print("Alien yellow: You earned 10 points")
else:
    print("Alien Red: You earned 15 points")

print("="*40 + "\n")

#5.6
age = 1

if age < 2:
    print("The person is a baby")
elif age < 4:
    print("The person is a toddler")
elif age < 13:
    print("The person is a kid")
elif age < 20:
    print("The person is a teenager")
elif age < 65:
    print("The person is an adult")
else:
    print("The person is an elder")
print("="*40 + "\n")

#5.7
favorite_fruits = ["Mangoes", "Apple", "Banana", "grapes"]

if 'Apple' in favorite_fruits:
    print("I really like Apple")

if 'Orange' in favorite_fruits:
    print("I really like Orange")

if 'Mangoes' in favorite_fruits:
    print("I really like Mangoes")

if 'Banana' in favorite_fruits:
    print("I really like Banana")

if 'Strewberries' in favorite_fruits:
    print("I really like Stewberries")
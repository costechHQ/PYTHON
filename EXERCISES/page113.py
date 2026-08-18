places = ["Portugal", "China", "USA", "Ghana", "Belgium"]

print("1. Original order:", places)
print("2. Alphabetical order:", sorted(places))
print("3. Original order verified:", places)
print("4. Reverse-alphabetical:", sorted(places, reverse=True))
print("5. Original order verified again:", places)

places.reverse()

print("6. permanently reversed:", places)

places.reverse()
print("7. Flipped back to original", places)

places.sort()
print("8. Permanently sorted:", places)
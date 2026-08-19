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

#Page108.py ln 37 and 38 has 3.9 (Dinner Guests)

#3.10

languages = ["French", "Chinesse", "Arabic", "Hebrew"]

print(f"1. Initial list: {languages}")
print(f"2. My best language is {languages[3]}.")

languages[2] = "Greek"
print(f"3. Updated index 2 name: {languages[2]}")

languages.append("Arabic")
print(f"4. After append: {languages}")

languages.insert(1, "Spanish")
print(f"5. After Insert: {languages}")

del languages[2]
print(f"6. After delete: {languages}")

popped_language = languages.pop()
print(f"7. Popped item: {popped_language}")
print(f"8. List after pop: {languages}")

languages.remove("French")
print(f"9. After removing: {languages}")

print(f"10. Temporarily sorted: {sorted(languages)}")

languages.sort()
print(f"11. Permanently sorted: {languages}")

print(f"12. temporarily reversed: {list(reversed(languages))}")

languages.reverse()
print(f"13. Permanently Reversed: {languages}")
print(f"14. This is the total sum of languages: {len(languages)}")


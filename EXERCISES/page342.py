import os

with open("cat.txt", "w", encoding="utf-8") as f:
    f.write("Luna\nOliver\nMilo\n")
with open("dogs.txt", "w", encoding="utf-8") as f:
    f.write("Rex\nBuddy\nCharlie\n")
with open("gutenberg_sample.txt", "w", encoding="utf-8") as f:
    f.write("The quick brown fox jumps over the lazy dog. then, there were others.")

print("Enter two number to add them together. Enter 'q' at any time to exit.")

while True:
    first_input = input("\nFirst number: ")
    if first_input.lower() == 'q':
        break

    second_input = input("Second number: ")
    if second_input.lower() == 'q':
        break

    try:
        num1 = int(first_input)
        num2 = int(second_input)
    except ValueError:
        print("Friendly Error: Please enter valid numbers, not text string!")
    else:
        result = num1 + num2
        print(f"Result: {num2} + {num2} = {result}")

print("\n" + "="*40 + "\n")

files = ["cat.txt", "dogs.txt", "missing_file.txt"] 

for file_name in files:
    print(f"\nAttempting to read: {file_name}")
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read()
            print(content.strip())
    except FileNotFoundError:
        print(f"Friendly Error: The file '{file_name}' could not be located on this system.")
print("\n" + "="*40 + "\n")

for file_name in files:
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read()
            print(f"Read {file_name} successfully")
    except FileNotFoundError:
        pass
print("\n" + "="*40 + "\n")

try:
    with open("gutenberg_sample.txt", "r", encoding="utf-8") as file:
        raw_text = file.read()

    lowercase_text = raw_text.lower()

    approx_count = lowercase_text.count("the")
    precise_count = lowercase_text.count("the ")

    print(f"Raw analysis sample text: \"{raw_text}")
    print(f"Count of 'the' (includes then/there): {approx_count}")
    print(f"Count of 'the' (with bounding space): {precise_count}")

except FileNotFoundError:
    print("Simple Gutenberg file is missing.")

for f_name in ["cats.txt", "dogs.txt", "gutenberg_sample.txt"]:
    if os.path.exists(f_name):
        os.remove(f_name)
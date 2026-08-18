user_input = input("Enter a word or phrase: ")

cleaned_text = user_input.replace(" ", "").lower()

if cleaned_text == cleaned_text[::-1]:
    print(f"{user_input} is a palindrome!")
else:
    print(f"{user_input} is not a palindrome.")

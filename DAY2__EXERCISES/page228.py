prompt = "\nPlease enter a pizza topping (or type 'quit' to finish): "

while True:
    topping = input(prompt)
    if topping.lower() == 'quit':
        break
    else:
        print(f"Adding {topping} to your pizza!")

# 7-5. Movie Tickets
print("\n--- 7-5. Movie Tickets Simulation ---")

age_prompt = "\nPlease enter your age to check the ticket price (or type 'quit'): "

while True:
    user_input = input(age_prompt)
    
    if user_input.lower() == 'quit':
        break
        
    age = int(user_input)
    
    if age < 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")


print("\n[Strategy A: Direct Condition Evaluation]")
topping = ""
while topping != 'quit':
    topping = input("Enter a topping (type 'quit'): ")
    if topping != 'quit':
        print(f"Adding {topping}!")


print("\n[Strategy B: Using a Flag Variable]")
active_flag = True
while active_flag:
    topping = input("Enter a topping (type 'quit'): ")
    if topping.lower() == 'quit':
        active_flag = False  
    else:
        print(f"Adding {topping}!")


print("\n[Strategy C: Immediate Break Execution]")
while True:
    topping = input("Enter a topping (type 'quit'): ")
    if topping.lower() == 'quit':
        break 
    print(f"Adding {topping}!")

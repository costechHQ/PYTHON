def greet_users(usernames_list):
   
    if usernames_list:
        for username in usernames_list:
            if username.lower() == 'admin':
                print("Hello admin, would you like to see a status report?")
            else:
                print(f"Hello {username}, thank you for logging in again.")
    else:
        print("We need to find some users!")


active_users = ['eric', 'jaden', 'admin', 'sarah', 'alice']
print("Testing active list:")
greet_users(active_users)


empty_users = []
print("\nTesting empty list:")
greet_users(empty_users)

print("\n" + "="*40 + "\n")

#5-10. Checking Usernames 

current_users = ['john', 'sara', 'Alex', 'admin', 'matt']
new_users = ['eric', 'JOHN', 'sara', 'lisa', 'ALEX']


current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user}' is taken. You will need to enter a new username.")
    else:
        print(f"Great! The username '{new_user}' is available.")

print("\n" + "="*40 + "\n")


#5-11. Ordinal Numbers

numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        suffix = "st"
    elif number == 2:
        suffix = "nd"
    elif number == 3:
        suffix = "rd"
    else:
        suffix = "th"
        
    print(f"{number}{suffix}")

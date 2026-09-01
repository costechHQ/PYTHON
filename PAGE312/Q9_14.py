from random import choice

pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
winning_ticket = []
while len(winning_ticket) < 4:
    pulled_item = choice(pool)
    if pulled_item not in winning_ticket:
        winning_ticket.append(pulled_item)

print("--- Lottery Draw Results ---")
print(f"Any ticket matching these 4 numbers or letters wins a prize: {winning_ticket}")

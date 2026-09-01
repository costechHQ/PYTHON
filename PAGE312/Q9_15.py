from random import choice

def get_winning_ticket(pool):
    """Draws 4 unique numbers or letters randomly from a pool."""
    ticket = []
    while len(ticket) < 4:
        pulled_item = choice(pool)
        if pulled_item not in ticket:
            ticket.append(pulled_item)
    return ticket


lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']


my_ticket = [7, 3, 'A', 'E']


attempts = 0
won = False

print("Running simulation... Please wait.")

while not won:
    current_draw = get_winning_ticket(lottery_pool)
    attempts += 1
    
    match_count = 0
    for item in my_ticket:
        if item in current_draw:
            match_count += 1
            
    if match_count == 4:
        won = True

print("\n--- Simulation Complete ---")
print(f"Your ticket: {my_ticket}")
print(f"Final matching draw: {current_draw}")
print(f"It took {attempts:,} attempts to win the lottery!")

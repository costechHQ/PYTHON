#3.4

guests = ["Victoria", "Blessing", "Esther", "Emmanuel", "Michael"]
for guest in guests:
     print(f"Dear {guest}, I will be truly honored to have you join me for a dinner")

#3.5
unable_to_attend = "Esther"
print(f"{unable_to_attend} can't attend the dinner")

guest_index = guests.index(unable_to_attend)
guests[guest_index] = "Adaeze"

print(f"Dear {guest}, I will be truly honored to have you join me for a dinner")

#3.6 
print("A quick update everyone! i found a bigger dinner table, so more space is available. \n")

guests.insert(0, "Precious")

middle_index = len(guests) // 3
guests.insert(middle_index, "Christabel")
guests.append("Glory")

print(f"Dear {guest}, I will be truly honored to have you join me for a dinner")

#3.7
print("Unfortuanately, my table can only accept only two persons")

while len(guests) > 2:
    removed_guest = guests.pop()
print(f" I am sorry, {removed_guest}, but I can't invite you to dinner anymore!")

for guest in guests:
    print(f"Good news, {guest}! you are invited to dinner")

num_guests = len(guests)
print(f"I am inviting exactly {num_guests} to my dinner!") 

del guests[0]
del guests[0]

print(f"Final guest list: {guests}")

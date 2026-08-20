car = 'sabaru'
username = 'ChrisHoly'
age = 30
scores = [85, 92, 78, 99]
banned_users = ['andrew', 'caroline', 'david']

#STRING EQUALITY AND INEQULAITY
print("1. Is car == 'sabaru'? I predict True")
print(car == 'sabaru')

print("\n2. Is car != 'audi'? I predict True (because sabaru is not audi)")
print(car != 'audi')

print("\n3. Is username == 'chrisholy'? I predict False (case-sensitive mismatch)")
print(username == 'chrisholy')

print("\n4. Is username.lower() == 'chrisholy'? I predict True (lowercasing fixes case mismatch)")
print(username.lower() == 'chrisholy')
print("="*40 + "\n")

#NUMBERICAL COMPARISONS

print("\n5. Is age == 30? I predict True.")
print(age == 30)

print("\n6. Is age != 20? I predict False.")
print(age != 30)

#GREATER / LESS THAN 
print("\n7. Is age > 20? I predict True")
print(age > 20)

print("\n8. is age < 18? I predict False")
print(age < 18)

print("\n9. Is age >= 30? I predict True (because age is equal to 30)")
print(age >= 30)

print("\n10. Is age <= 20? I predict False (because age is neither less than or equal to 20)")
print(age <= 20)
print("="*40 + "\n")

#LOGICAL OPERATORS

print("\n11. Is age >= 25 and age < 40? I predict True (both conditions pass)")
print(age >= 25 and age < 40)

print("\n12. Is age <= 10  and age > 29? I predict False")
print(age <= 10 and age > 29)

print("\n13. Is age < 20 or age == 30? i predict True (the right condition passess )")
print(age < 20 or age == 30)

print("\n14. Is age > 100 or age < 25? I predict False")
print(age > 100 or age < 25)
print("="*40 + "\n")

#LIST MEMBERSHIP OPERATORS
print("\n15. Is 92 in scores? I predict True")
print(92 in scores)

print("\n16. is 100 in scores? I predict False")
print(100 in scores)

print("\n17. Is Simon not in banned_users? I predict True")
print(100 not in banned_users)

print("\n18. Is andrew not in banned_users? I predict False")
print("andrew" not in banned_users)
from random import randint

class Die:
    """A class representing a single die."""

    def __init__(self, sides=6):
        """Initialize the number of sides. Default is 6."""
        self.sides = sides

    def roll_die(self):
        """Return a random number between 1 and the number of sides."""
        return randint(1, self.sides)




six_sided_die = Die()
results_6 = []
for _ in range(10):
    results_6.append(six_sided_die.roll_die())
print(f"Rolling a 6-sided die 10 times: {results_6}")

ten_sided_die = Die(sides=10)
results_10 = []
for _ in range(10):
    results_10.append(ten_sided_die.roll_die())
print(f"Rolling a 10-sided die 10 times: {results_10}")


twenty_sided_die = Die(sides=20)
results_20 = []
for _ in range(10):
    results_20.append(twenty_sided_die.roll_die())
print(f"Rolling a 20-sided die 10 times: {results_20}")

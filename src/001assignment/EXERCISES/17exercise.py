inputs = input("Enter three numbers: ").split()
num1 = int(inputs[0])
num2 = int(inputs[1])
num3 = int(inputs[2])

largest = max(num1, num2, num3)
print(f"The largest number is {largest}.")

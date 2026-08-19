# #4.3
# for number in range(1, 21):
#     print(number, end=" ")

# #4.4
# for numbers in range(1, 1000001):
#     print(numbers, end=" ")

#4.5
# numbers = list(range(1,1000001))
# print(f"Minimum Value: {min(numbers)}")
# print(f"Maximum Value: {max(numbers):,}")

# total_sum = sum(numbers)
# print(f"Sum of numbers 1 to 1000000: {total_sum:,}")

#4.6
# odd_numbers = list(range(1, 21, 2))
# for odd in odd_numbers:
#     print(odd, end=" ")

#4.7
# multiples_of_three = list(range(3, 31, 3))
# for multiple in multiples_of_three:
#     print(multiple, end=" ")

#4.8
cube_list = []
for value in range(1, 11):
    cube = value ** 3
    cube_list.append(cube)
    print(f"The cube of {value} is {cube}")

#4.9
cube_comprehension = [value ** 3 for value in range(1,11)]
print(f"Generated List: {cube_comprehension}")

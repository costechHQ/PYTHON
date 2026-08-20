def two_sum(nums, target):
    seen_numbers = {}
    for index, current_num in enumerate(nums):
        complement = target - current_num
        if complement in seen_numbers:
            return [seen_numbers[complement], index]
        seen_numbers[current_num] = index
print("Example 1 Output:", two_sum([2, 7, 11, 15], 9))
print("Example 2 Output:", two_sum([3, 2, 4], 6))
print("Example 3 Output:", two_sum([3, 3], 6))
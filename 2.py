# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element at index i 
# of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?


test_nums = [1, 2, 3, 4, 5]
test_nums2 = [3, 7, 4, 8, 1]
test_nums3 = [3, 2, 1]


def solution_one(nums: list([1,2,3])) -> list:
    print("Beginning list" + f': {nums}')
    for count in range(len(nums)):
        parsed = [x for x_count, x in enumerate(nums) if count != x_count]
        result = parsed[0]

        for each in range(len(parsed) - 1):
            print(f"{result} * {parsed[each + 1]} = {result * parsed[each + 1]}")
            result *= parsed[each + 1]

        print(f"Result: {result}\n")


def solution_two(nums: list([1,2,3])) -> list:
    print(f"Beginning list {nums}")

    



test_one = solution_one(test_nums)
test_two = solution_one(test_nums2)
test_three = solution_one(test_nums3)
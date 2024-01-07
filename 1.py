import time
#This problem was recently asked by Google.

#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

numbers = [3,8,5,7,9,14]

n = 16

def first_solution(nums: list, k: int):
    outcome = False

    for count, num in enumerate(nums):
        curr = nums[count]

        others = [x for countx, x in enumerate(nums) if countx != count]

        for each in others:
            result = each + curr

            if result == k:
                outcome = True
                break
        if outcome:
            break

    if outcome:
        print("Yes there are two numbers that add up to k")
    else:
        print("No there are not two numbers that add up to k")


def second_solution(nums: list, k: int):
    outcome = False

    for count, num in enumerate(nums):
        checkers = [x for x in range(count + 1, len(nums))]

        for each in checkers:
            if nums[each] + num == k:
                outcome = True
                break

        if outcome:
            break

    if outcome:
        print("Yes there are two numbers that add up to k")
    else:
        print("No there are not two numbers that add up to k")

start = time.perf_counter()
first_solution(numbers, n)
end = time.perf_counter()
print(f"Solution one took {end-start:0.6f} seconds")

print(f"\n")

start = time.perf_counter()
second_solution(numbers, n)
end = time.perf_counter()
print(f"Solution two took {end-start:0.6f} seconds")
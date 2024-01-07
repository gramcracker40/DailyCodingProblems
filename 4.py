#Good morning! Here's your coding interview problem for today.

#This problem was asked by Stripe.

# Given an array of integers, find the first missing positive 
# integer in linear time and constant space. In other words, 
# find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.

#For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

test_list = [1, 3, 4, 5, 1, 3, -4, -8, -11]
test_list2 = [1,2,6,3,4,5,6, 7, 8, 9, 5, 7, 9, 13, -10, -100, 100, 145]

def solution_one(numbers: list):
    
    lowest = 1
    for num in numbers:
        if num == lowest:
            lowest += 1
            if lowest in numbers:
                while(lowest not in numbers):
                    lowest+=1
                    

    return lowest

test = solution_one(test_list2)
print(test)

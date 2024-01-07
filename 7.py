#This problem was asked by Airbnb.

#Given a list of integers, write a function that returns the largest sum 
#of non-adjacent numbers. Numbers can be 0 or negative.

#For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. 
# [5, 1, 1, 5] should return 10, since we pick 5 and 5.

#Follow-up: Can you do this in O(N) time and constant space?

a = [2, 4, 6, 2, 5]
b = [5, 1, 1, 5]


def check_non_adjacent(c:list):
    '''
    checks all non adjacent sums 
    '''

    sum = 0
    for count, i in enumerate(c):
        



test = check_non_adjacent(a)
test2 = check_non_adjacent(b)

print(test)
print(test2)
'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers. For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:

  1
 2 3
1 5 1

We define a path in the triangle to start at the top and go down one row at a time to an adjacent value, eventually ending with an entry on the bottom row. For example, 1 -> 3 -> 5. The weight of the path is the sum of the entries.

Write a program that returns the weight of the maximum weight path.
'''

    

tree = [[1], [2, 3], [1, 5, 1]]

rows = len(tree)
max=0

combo = {}
for row in range(rows):      # iterable
    best = 0
    for each in tree[row]:   # each value
        if each > best:
            if best != 0:
                max -= best
            max += each
            best = each
            combo[row] = each
            

for count, val in enumerate(combo.values()):
    if count != len(combo) - 1:
        print(f"{val} -> ", end="")
    else:
        print(f"{val}")
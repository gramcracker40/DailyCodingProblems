'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Slack.

You are given an N by M matrix of 0s and 1s. Starting from the top left corner, how many ways are there to reach the bottom right corner?

You can only move right and down. 0 represents an empty space while 1 represents a wall you cannot walk through.

For example, given the following matrix:

[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]
Return two, as there are only two ways to get to the bottom right:

Right, down, down, right
Down, right, down, right
The top left corner and bottom right corner will always be 0.
'''

maze = [[0, 0, 1],
        [0, 0, 1],
        [1, 0, 0]]


start = (0,0)
paths = {}
for row_num, row in enumerate(maze):
    for index, val in enumerate(maze[row_num]):
        try:
            print(f"Row: {row_num} Col: {index}") 
            print(f"col_num -> {index+1}  length -> {len(maze[row_num])}")
            print(f"row_num -> {row_num}  height -> {len(maze)}")

            right_check = True if (index + 1) < len(maze[row_num]) else False
            bottom_check = True if (row_num + 1) < len(maze) else False

            bottom = maze[row_num + 1][index] if bottom_check else None
            right = maze[row_num][index + 1] if right_check else None

            print(f"Right --> {right}")
            print(f"Bottom --> {bottom}")
            
        except IndexError as err: # no right element
            print("Index error thrown")
            print(str(err))

            pass

        print("\n\n")
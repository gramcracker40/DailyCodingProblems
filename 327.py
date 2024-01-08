# This problem was asked by Salesforce.

# Write a program to merge two binary trees. Each node in the 
# new tree should hold a value equal to the sum of the values of 
# the corresponding nodes of the input trees.

# If only one input tree has a node in a given position, the corresponding node 
# in the new tree should match that input node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mergeTrees(t1, t2):
    # If both trees are empty
    if not t1 and not t2:
        return None
    
    # If one of the trees is empty, return the other tree
    if not t1:
        return t2
    if not t2:
        return t1

    # Merge the values
    t1.val += t2.val

    # Recursively merge the left and right children
    t1.left = mergeTrees(t1.left, t2.left)
    t1.right = mergeTrees(t1.right, t2.right)

    return t1

# Helper function to create a tree from a list
def create_tree(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while i < len(lst):
        current = queue.pop(0)
        if lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i += 1
    return root

# Test Case 1
t1 = create_tree([1, 3, 2, 5, None])
t2 = create_tree([2, 1, 3, None, 4, None, 7])
merged_tree_1 = mergeTrees(t1, t2)

# Test Case 2
t1 = create_tree([1])
t2 = create_tree([1, 2, 7])
merged_tree_2 = mergeTrees(t1, t2)

# Test Case 3
t1 = create_tree([5, 1])
t2 = None
merged_tree_3 = mergeTrees(t1, t2)

# Function to print the tree in pre-order traversal
def print_tree(root):
    if root:
        print(root.val, end=' ')
        print_tree(root.left)
        print_tree(root.right)

# Print the results
print("Test Case 1:")
print_tree(merged_tree_1)
print("\nTest Case 2:")
print_tree(merged_tree_2)
print("\nTest Case 3:")
print_tree(merged_tree_3)

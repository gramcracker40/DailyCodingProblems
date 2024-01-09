from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self, lst):
        if lst:
            self.root = self.build_tree(lst, 0)
        else:
            self.root = None

    def build_tree(self, lst, index):
        if index < len(lst) and lst[index] is not None:
            node = TreeNode(lst[index])
            node.left = self.build_tree(lst, 2 * index + 1)
            node.right = self.build_tree(lst, 2 * index + 2)
            return node
        return None

    @staticmethod
    def print_pre_order(root):
        """Pre-order traversal: Root -> Left -> Right"""
        if root:
            print(root.val, end=' ')
            Tree.print_pre_order(root.left)
            Tree.print_pre_order(root.right)

    @staticmethod
    def print_level_order(root):
        """Level-order traversal: prints nodes level by level"""
        if not root:
            return
        
        queue = deque([root])
        while queue:
            node = queue.popleft()
            print(node.val, end=' ')

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    @staticmethod
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
        t1.left = Tree.mergeTrees(t1.left, t2.left)
        t1.right = Tree.mergeTrees(t1.right, t2.right)

        return t1

# testing helper functions
def build_and_merge_trees(tree1_values, tree2_values):
    t1 = Tree(tree1_values)
    t2 = Tree(tree2_values)
    return Tree.mergeTrees(t1.root, t2.root)

def print_test_case(case_number, tree1_values, tree2_values):
    merged_tree_root = build_and_merge_trees(tree1_values, tree2_values)

    print(f"Test Case {case_number}:")
    print("Merged Tree (Pre-order Traversal): ", end="")
    Tree.print_pre_order(merged_tree_root)
    print("\nMerged Tree (Level-order Traversal): ", end="")
    Tree.print_level_order(merged_tree_root)
    print("\n")


if __name__ == "__main__":
    print_test_case(1, [1, 3, 2, 4, 0], 
                       [2, 1, 3, 0, 4, 0, 7])
    print_test_case(2, [1], 
                       [1, 2, 7])
    print_test_case(3, [5, 1], None)
    print_test_case(4, [3, 4, 5], 
                       [1, 2, 3])
    print_test_case(5, [7, 8, 9, 1, 2, 3, 4], 
                       [5, 6, 0, 7])
    print_test_case(6, [1, 2], 
                       [3, 4, 5, 6])
    print_test_case(7, [3], 
                       [])
    print_test_case(8, [], 
                       [4, 5, 6])
    print_test_case(9, [1, None, 2], 
                       [1, 2])
    print_test_case(10,[2, 3, 4, 5], 
                       [1, 2, 3, None, None, 6])
    print_test_case(11,[3, 4, 5, 6, 7], 
                       [1, None, 2])
    print_test_case(12,[None, None, 3], 
                       [1, 2])
    print_test_case(13,[5, 4, 3, 2, 1], 
                       [1, 2, 3, 4, 5])
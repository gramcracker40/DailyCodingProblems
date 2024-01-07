#Good morning! Here's your coding interview problem for today.

#This problem was asked by Google.

#Given the root to a binary tree, implement serialize(root), 
#which serializes the tree into a string, and deserialize(s), 
# which deserializes the string back into the tree.

#For example, given the following Node class


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node:({self.val},{self.left},{self.right})"


def serialize(node: Node):
    '''
    runs through an individual node and returns its serialized version
    '''
    val = node.val
    
    if node.left:
        left = serialize(node.left)
    else:
        left = None
    
    if node.right:
        right = serialize(node.right)
    else:
        right = None

    serialized = [val, left, right]

    return serialized


def deserialize(serialized: list):
    '''
    deserializes the serialized node from serialize() into a Node(object)
    '''
    val = serialized[0]
    if serialized[1]:
        left = deserialize(serialized[1])
    else:
        left = None

    if serialized[2]:
        right = deserialize(serialized[2])
    else:
        right = None

    deserialized = Node(val, left, right)

    return deserialized



test_node = Node('root', Node('left', Node('left.left')), Node('right'))
ser_test = serialize(test_node)
deser_test = deserialize(ser_test)

### Test provided by DailyCodingProblems below
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

print(ser_test)
print(deser_test)
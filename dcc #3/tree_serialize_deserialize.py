"""Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

"""
There are two ways to solve this
Method 1: Using plain old coding. Pre-order traversal for serializing and parsing to deserialize
Method 2: Python's __repr__ and __eval__ 
"""

import re
import unittest


class Node2:
    """
    This class has the whole Method 2
    Pretty much self-explanatory
    """

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return '{}:{{{},{}}}'.format(self.val, self.left, self.right)

    serialize = repr
    deserialize = eval


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    # Edge case -->
    if node is None:
        return None
    # <-- Edge case

    root = node.val
    left = None
    right = None

    if node.left:  # Recurse to serialize left subtree
        left = serialize(node.left)
    if node.right:  # Recurse to serialize right subtree
        right = serialize(node.right)
    if left is None and right is None:  # If left and right subtree is None, meaning leaf node
        serialized = "{}".format(root)
    else:  # Else some tree with left and/ or right subtree
        serialized = ("{}:{{{},{}}}".format(root, left, right))
    return serialized


def deserialize(serialized):
    if serialized is None:
        return None
    if serialized == 'None':
        return None
    if not serialized.__contains__(":") or not serialized.__contains__(","):
        return Node(serialized)

    pattern = "^(\w+):{([\w.]+),([\w.]+)}$"  # Pattern to detect [root:{left, right}] for making Node object
    regex_match = re.match(pattern, serialized)
    if regex_match is not None:
        tree = regex_match.groups()  # Get groups from regex, 1st is root, 2nd is left and 3rd is right
        root = tree[0]
        left = tree[1]
        right = tree[2]
        deserialized = Node(root, Node(left) if left != 'None' else None, Node(right) if right != 'None' else None)
        return deserialized
    else:
        root = Node(serialized[:serialized.index(":")])  # Get root from string
        subtree = serialized[serialized.index("{") + 1:-1]  # Rest of tree
        if subtree[:4] == 'None':  # Check for left subtree
            subtree_left = subtree[0:4]
            subtree_right = subtree[5:]
        else:  # Split the rest of tree to find corresponding left tree and right tree
            subtree_left_start = 0
            subtree_right_start = 0
            start_brace_counter = 0
            start_end_counter = 0
            for i in range(len(subtree)):
                if subtree[i] == '{':
                    start_brace_counter += 1
                elif subtree[i] == '}':
                    start_end_counter += 1
                    if start_brace_counter == start_end_counter:
                        subtree_right_start = i + 1
                        break
            subtree_left = subtree[subtree_left_start:subtree_right_start]
            subtree_right = subtree[subtree_right_start + 1:]

        # Recursively deserialize the left and right subtrees
        root.left = deserialize(subtree_left)
        root.right = deserialize(subtree_right)
        return root


class TestSolution(unittest.TestCase):
    def test(self):  # Test for Method 1
        # Base case
        node = Node('root', Node('left', Node('left.left')), Node('right'))
        assert deserialize(serialize(node)).left.left.val == 'left.left'

        # Basic tree
        node = Node(1, Node(2, Node(3)), Node(4, None, Node(5)))
        assert deserialize(serialize(node)).left.left.val == '3'
        assert deserialize(serialize(node)).right.right.val == '5'
        assert deserialize(serialize(node)).right.left is None

        # Complete binary tree
        node = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
        assert deserialize(serialize(node)).val == '1'
        assert deserialize(serialize(node)).left.val == '2'
        assert deserialize(serialize(node)).right.val == '3'
        assert deserialize(serialize(node)).left.left.val == '4'
        assert deserialize(serialize(node)).left.right.val == '5'
        assert deserialize(serialize(node)).right.left.val == '6'
        assert deserialize(serialize(node)).right.right.val == '7'

        # Tree having only left children
        node = Node(1, Node(2, Node(3, Node(4, Node(5)))))
        assert deserialize(serialize(node)).left.left.left.left.val == '5'

        # Tree having only right children
        node = Node(1, None, Node(2, None, Node(3, None, Node(4, None, Node(5)))))
        assert deserialize(serialize(node)).right.right.right.right.val == '5'

    def test2(self):  # Test for Method 2
        # Base case
        node = Node2('root', Node2('left', Node2('left.left')), Node2('right'))
        assert deserialize(serialize(node)).left.left.val == 'left.left'

        # Basic tree
        node = Node2(1, Node2(2, Node2(3)), Node2(4, None, Node2(5)))
        assert deserialize(serialize(node)).left.left.val == '3'
        assert deserialize(serialize(node)).right.right.val == '5'
        assert deserialize(serialize(node)).right.left is None

        # Complete binary tree
        node = Node2(1, Node2(2, Node2(4), Node2(5)), Node2(3, Node2(6), Node2(7)))
        assert deserialize(serialize(node)).val == '1'
        assert deserialize(serialize(node)).left.val == '2'
        assert deserialize(serialize(node)).right.val == '3'
        assert deserialize(serialize(node)).left.left.val == '4'
        assert deserialize(serialize(node)).left.right.val == '5'
        assert deserialize(serialize(node)).right.left.val == '6'
        assert deserialize(serialize(node)).right.right.val == '7'

        # Tree having only left children
        node = Node2(1, Node2(2, Node2(3, Node2(4, Node2(5)))))
        assert deserialize(serialize(node)).left.left.left.left.val == '5'

        # Tree having only right children
        node = Node2(1, None, Node2(2, None, Node2(3, None, Node2(4, None, Node2(5)))))
        assert deserialize(serialize(node)).right.right.right.right.val == '5'


if __name__ == '__main__':
    unittest.main()

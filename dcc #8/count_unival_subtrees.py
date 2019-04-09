import unittest

"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""


class Node:
    """
    Basic Node structure
    """
    val = None
    left = None
    right = None

    def __init__(self, val):
        self.val = val


def count_unival_subtrees(node):
    """
    Counts the number of unival subtrees, and if current tree under this node is unival or not

    --> Doing pre-order traversal and check for every node unival-ness is okay, but goes to O(n^2).
    Check coding-dojo video for why it is n^2.

    --> Other solution is to recursively go the leaves of the tree and go upwards counting unival
    This Solution is O(n).

    :param node: Node at which check is considered against
    :return: pair of number of subtrees and if tree under current node is unival
    """
    # Base case -->
    if node is None:  # Hit a leaf node. It is always a unival tree
        return 0, True
    # <-- Base case
    left_count, left_unival = count_unival_subtrees(node.left)  # Go left depth wise
    right_count, right_unival = count_unival_subtrees(node.right)  # Go right depth wise
    unival = True  # Assume the tree under current node is unival

    # Checks for if tree under current node is really unival or not -->
    if not left_unival and not right_unival:
        unival = False
    if node.left and node.left.val != node.val:
        unival = False
    if node.right and node.right.val != node.val:
        unival = False
    # <-- End check

    if unival:  # Tree under given node is unival, add 1 for itself
        return left_count + right_count + 1, True
    else:  # Tree under given node is not unival, add return left and right count
        return left_count + right_count, False


class Test(unittest.TestCase):
    def setUp(self):
        # Tree with the above diagram
        self.data = Node(0)

        self.data.left = Node(1)
        self.data.right = Node(0)

        self.data.right.left = Node(1)
        self.data.right.right = Node(0)

        self.data.right.left.left = Node(1)
        self.data.right.left.right = Node(1)

    def test_base_case(self):
        self.assertEqual(count_unival_subtrees(self.data)[0], 5)


if __name__ == '__main__':
    unittest.main()

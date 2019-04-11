import unittest

"""
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
 return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

Solution:
Could have done using basic array comparison by checking each array element for prefix and returning those
but the below method is more efficient in "system design terms"
NOTE: The more efficient data structure is a TRIE
Convert the given set of strings to a Trie, and then just traverse it to get required result
"""


class Node:
    """
    Node object for the Trie. It contains the value and list of child Nodes that have been formed due to preprocessing
    """
    val = None  # Value of Node, i.e., a character
    pointers = []  # List of pointers to child Nodes

    def __init__(self, val=None):
        self.val = val
        self.pointers = []

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.val == other.val
        if isinstance(other, str):
            return self.val == other


def preprocess_set(all_words):
    """
    Converts the set of given words to a Trie and returns the root node
    :param all_words: Set of words to be converted in Trie
    :return: root node of the trie
    """
    root = Node()  # Root node value is None for Trie
    copy_root = root  # Make a copy of root to return later
    for word in all_words:  # Loop through all words
        for letter in word:  # Loop through all letters of the word
            new_node = Node(letter)  # Make a new node for the letter
            if letter in root.pointers:  # Check if the letter is already present in child nodes of the current root
                pointer = root.pointers.index(letter)  # It is present, get it's index
                root = root.pointers[pointer]  # Propagate root to the index
            else:  # New letter for the current root
                root.pointers.append(new_node)  # Append it to its pointer
                root = new_node  # Propagate root to the new node
        root = copy_root  # Reset root to beginning, since this word is complete and we need root node for new word
    return copy_root  # Return the original root


def check_prefix_exists(root, prefix):
    """
    Thie function checks if the prefix pattern is present in the trie or not
    :param root: The root node of the trie
    :param prefix: The prefix pattern to be searched
    :return: Pair of if prefix exists and the node at which the prefix ends
    """
    for letter in prefix:  # Check every letter in prefix
        if letter in root.pointers:  # Check if that letter is present in the current root's pointers
            root = root.pointers[root.pointers.index(letter)]  # It is present. Change root to that node.
        else:  # Letter not present in root. Meaning prefix not in trie
            return False, None  # Return false and none
    return True, root  # Return True (prefix found) and the last matched node


def helper_get_words_from_prefix(node, prefix):
    """
    Helper function to invoke main function get_word_from_prefix(node, prefix)
    :param node: Root node of the trie
    :param prefix: Prefix to get words from
    :return: List of words starting with the prefix given
    """

    # Edge case -->
    if node is None or prefix is None:
        raise ValueError('none type provided. node={}, prefix={}'.format(node, prefix))
    if not isinstance(node, Node):
        raise TypeError('node is of type {}. Should be {}'.format(type(node), type(Node)))
    if not isinstance(prefix, str):
        raise TypeError('prefix is of type {}. Should be {}'.format(type(node), type(str)))
    # <-- Edge case

    exists, prefix_end_node = check_prefix_exists(node, prefix)  # Check if prefix exists in trie
    if exists:  # Yes, it exists
        results = []  # Initialize empty array
        get_words_from_prefix(prefix_end_node, prefix, results)  # Pass that array to the function to be filled
        return results  # Return the array
    else:  # Nope, return None
        return None


def get_words_from_prefix(node, prefix, results):
    """
    Given a prefix and prefix node of the trie, it does a DFS to go to leaf nodes and fills in the results array
    :param node: The prefix node of the trie
    :param prefix: Prefix to form words with
    :param results: Results array passed from helper function
    :return: The filled results array
    """
    if node.pointers:  # Check if node has pointers
        for pointer in node.pointers:  # It has pointers, go down one level
            get_words_from_prefix(pointer, prefix + pointer.val,
                                  results)  # recurse till leaf with prefix updated to incorporate the child letter
    else:  # No pointers, meaning a leaf node
        results.append(prefix)  # Append the prefix to results array
        return results  # Return the results array


words = {'dog', 'deer', 'deal', 'lol'}


class Test(unittest.TestCase):
    def setUp(self):
        self.words = {'dog', 'deer', 'deal', 'lol'}
        self.trie_root_node = preprocess_set(words)

    def test_base_case(self):
        self.assertItemsEqual(helper_get_words_from_prefix(self.trie_root_node, 'de'), ['deer', 'deal'])

    def test_custom_case1(self):
        self.assertItemsEqual(helper_get_words_from_prefix(self.trie_root_node, 'd'), ['deer', 'deal', 'dog'])

    def test_custom_case2(self):
        self.assertItemsEqual(helper_get_words_from_prefix(self.trie_root_node, 'do'), ['dog'])

    def test_empty_prefix(self):
        self.assertItemsEqual(helper_get_words_from_prefix(self.trie_root_node, ''), self.words)

    def test_none_prefix(self):
        self.assertRaises(ValueError, helper_get_words_from_prefix, self.trie_root_node, None)

    def test_none_node(self):
        self.assertRaises(ValueError, helper_get_words_from_prefix, None, 'de')

    def test_none_node_none_prefix(self):
        self.assertRaises(ValueError, helper_get_words_from_prefix, None, None)

    def test_invalid_class_node(self):
        self.assertRaises(TypeError, helper_get_words_from_prefix, 1, 'de')

    def test_invalid_class_prefix(self):
        self.assertRaises(TypeError, helper_get_words_from_prefix, self.trie_root_node, 1)


if __name__ == '__main__':
    unittest.main()

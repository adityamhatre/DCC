import unittest

"""
An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev 
fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked 
list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index. 

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and 
dereference_pointer functions that converts between nodes and memory addresses.
"""

# Since python has no pointer system, create one virtually
# Memory map of id->Node where id=id(Node)
nodes = {}


def dereference_pointer(address):
    """
    Returns the Node object at the address
    :param address: Memory address of the desired node
    :return: Node at the provided memory address
    """
    return nodes[address]


def get_pointer(node):
    """
    Returns the pointer to the node
    :param node: The node whose pointer is desired
    :return: Pointer to the node
    """
    return id(node)


class Node:
    data = None
    both = None

    def __init__(self, data=None):
        self.data = data

    def get_next_node(self, previous):
        """
        Retrieves the next node from the current node using self address XOR'ed with the previous node's address
        :param previous: Previous node's memory address
        :return: Returns next node in the list or None if this is the last node
        """
        try:
            return dereference_pointer(get_pointer(previous) ^ self.both)
        except KeyError:
            return None

    def __repr__(self):
        return "{}: {}, {}".format(id(self), self.data, self.both)


class DoublyLinkedList:
    size = 0

    def __init__(self):
        head_node = Node()
        self.head = get_pointer(head_node)
        nodes[get_pointer(head_node)] = head_node  # Saving head node's pointer in the memory map

    def add(self, data):
        """
        Adds a new node to the list Set the 'both' field of the current node to be XOR of current memory address and
        previous node address.

        next_node_address = previous_node_address XOR current_node_address
        Future me: WORK IT OUT. I worked out for this. Try and recreate with basic binary addresses like 00,01,10,11

        Read problem description.


        :param data: The data to be added in the new node
        """

        # Edge case -->
        if data is None:
            raise ValueError("Cannot add None. NoneType provided.")
        # <-- Edge case

        new_node = Node(data)  # Creating new node
        if dereference_pointer(self.head).both is None:
            dereference_pointer(self.head).both = get_pointer(new_node) ^ 0
            nodes[get_pointer(new_node)] = new_node
        else:
            prev = dereference_pointer(self.head)
            curr = dereference_pointer(prev.both)
            while curr.both is not None:
                t = curr
                curr = curr.get_next_node(prev)
                prev = t
            curr.both = get_pointer(prev) ^ get_pointer(new_node)
            nodes[get_pointer(new_node)] = new_node
        self.size += 1  # Increment size of list

    def get(self, i):
        """
        Gets the node at the ith index
        :param i: The index
        :return: Node at the index
        """
        if type(i) is not int:
            raise TypeError('{} provided. Required: int'.format(type(i)))
        if i < 0 or i >= self.size:
            raise IndexError("index {} out of bounds".format(i))
        return self.traverse(get_mode=True, index=i)

    def traverse(self, get_mode=False, index=None):
        """
        Traverses the whole list
        :param get_mode: Optional param; only used by get()
        :param index:  Optional param; only used by get()
        """
        prev = dereference_pointer(self.head)
        curr = dereference_pointer(prev.both)
        counter = 0
        while curr is not None:
            if get_mode:
                if counter == index:
                    return curr
            if not get_mode:
                print(curr.data)
            t = curr
            if curr.both is not None:
                curr = curr.get_next_node(prev)
            else:
                break
            prev = t
            counter += 1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.dll = DoublyLinkedList()

    def test_add(self):
        self.dll.add(1)
        self.assertTrue(self.dll.get(0), 1)

        self.dll.add(2)
        self.assertTrue(self.dll.get(1), 2)

    def test_add_none(self):
        self.assertRaises(ValueError, self.dll.add, None)

    def test_get(self):
        self.dll.add(1)
        self.dll.add(2)
        self.assertTrue(self.dll.get(0).data, 1)
        self.assertTrue(self.dll.get(1).data, 2)

    def test_get_index_out_of_bounds(self):
        self.dll.add(1)
        self.dll.add(2)
        self.assertRaises(IndexError, self.dll.get, -1)
        self.assertRaises(IndexError, self.dll.get, 2)

    def test_invalid_get(self):
        self.dll.add(1)
        self.assertRaises(TypeError, self.dll.get, 1.5)


if __name__ == '__main__':
    unittest.main()

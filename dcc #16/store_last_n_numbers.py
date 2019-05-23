"""
You run an e-commerce website and want to record the last N order ids in a log.
Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
"""
import unittest


class FixedLengthArray:
    """
    FixedLengthArray is a cyclic data structure that keeps the last :param buffer_size elements, i.e.,
    works like a cache
    """
    total_seen = 0  # Total number of elements seen until now
    last_added_at = None  # Track the index at which last element was placed

    def __init__(self, buffer_size=5):
        # Edge cases -->
        if buffer_size is None:
            raise TypeError("buffer size should not be none")
        if type(buffer_size) is not int:
            raise TypeError("buffer size should be int")
        if buffer_size < 0:
            raise ValueError("buffer size should be greater than 0")
        # <-- Edge cases

        self.buffer_size = buffer_size
        self.a = [None] * buffer_size

    def record(self, order_id):
        """
        Records (inserts) the :param order_id in the buffer
        :param order_id: The value to be recorded
        """

        # Edge case -->
        if order_id is None:
            raise TypeError("order id cannot be None")
        # <-- Edge case

        # Create a cyclic insertion logic
        if self.total_seen == 0:
            self.last_added_at = 0
        else:
            self.last_added_at = self.total_seen % self.buffer_size

        self.total_seen += 1  # Increment the number of added elements
        self.a[self.last_added_at] = order_id  # Place the element at the calculated index

    def get_last(self, i):
        """
        Get's the last :param ith placed element from the array
        :param i: The last position for which value is to be retrieved
        :return: Element at the calculated position
        """

        # Edge cases -->
        if i <= 0:
            raise ValueError("i should be greater than 0")
        if i > self.buffer_size:
            raise ValueError("i cannot be larger than buffer size")
        # <-- Edge cases

        # Calculate the index and return the value at that index
        return self.a[(self.total_seen - i) % self.buffer_size]


class Test(unittest.TestCase):
    def setUp(self):
        self.buffer_size = 5
        self.fixed_length_array = FixedLengthArray(self.buffer_size)
        self.orders = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    def test_base_case(self):
        for order in self.orders:
            self.fixed_length_array.record(order)
        self.assertEqual(self.fixed_length_array.get_last(1), 90)
        self.assertEqual(self.fixed_length_array.get_last(2), 80)
        self.assertEqual(self.fixed_length_array.get_last(4), 60)

    def test_record_none(self):
        self.assertRaises(TypeError, self.fixed_length_array.record, None)

    def test_get_last_negative(self):
        self.assertRaises(ValueError, self.fixed_length_array.get_last, -1)

    def test_get_last_0(self):
        self.assertRaises(ValueError, self.fixed_length_array.get_last, 0)

    def test_get_last_greater_than_buffer(self):
        self.assertRaises(ValueError, self.fixed_length_array.get_last, self.buffer_size + 1)

    def test_base_init_data_structure(self):
        self.assertIsInstance(self.fixed_length_array, FixedLengthArray)

    def test_init_none_buffer(self):
        self.assertRaises(TypeError, FixedLengthArray, None)

    def test_init_negative_buffer(self):
        self.assertRaises(ValueError, FixedLengthArray, -1)

    def test_init_floating_buffer(self):
        self.assertRaises(TypeError, FixedLengthArray, 1.1)


if __name__ == '__main__':
    unittest.main()

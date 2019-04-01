"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""
import unittest


def check_two_numbers_add_up_to_target(array, target):
    """
    Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
    :param array: Array of number
    :param target: Value, the sum needs to be checked against
    :return: Boolean indicating two numbers in list add up to target
    """

    # Edge cases -->
    if array is None or target is None:
        return False
    if len(array) < 1:
        return False
    if len(array) is 1:
        return array[0] == target
    # <-- Edge cases

    values = set()  # Set for visited numbers
    for el in array:  # For every element in array
        if el is None:  # Skip 'None' elements
            continue
        if target - el in values:  # Check if it's complement exists in the set of already visited numbers
            return True  # Return True if exists
        values.add(el)  # Else add the current value to the set of visited numbers
    return False  # Sum cannot be achieved by two elements. Return False


class TestSolution(unittest.TestCase):
    def test(self):
        # Normal case
        a = [10, 15, 3, 7]
        k = 17
        self.assertTrue(check_two_numbers_add_up_to_target(a, k))

        # Empty array
        a = []
        k = 17
        self.assertFalse(check_two_numbers_add_up_to_target(a, k))

        # Empty target
        a = []
        k = None
        self.assertFalse(check_two_numbers_add_up_to_target(a, k))

        # None array and target
        a = []
        k = 17
        self.assertFalse(check_two_numbers_add_up_to_target(a, k))

        # None array and None target
        a = None
        k = None
        self.assertFalse(check_two_numbers_add_up_to_target(a, k))

        # None element in array
        a = [None, 10, 7]
        k = 17
        self.assertTrue(check_two_numbers_add_up_to_target(a, k))

        # None element in array
        a = [None, 10, 7]
        k = 16
        self.assertFalse(check_two_numbers_add_up_to_target(a, k))


if __name__ == '__main__':
    unittest.main()

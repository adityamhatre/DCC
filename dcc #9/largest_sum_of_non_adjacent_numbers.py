import unittest

"""Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0
or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10,
since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""


def largest_sum_of_non_adjacent_numbers(arr):
    """
    Calculates the largest possible sum of non-adjacent elements in the array.
    ONLY TAKES int

    How it works:
    Start from end of the array. Now we have two options.
    Option 1: Include that element for the sum
    Option 2: Don't include that element in the sum

    If we select option 1, that means the next element should be the one that is 2 places before it. Since we want
    non-adjacent elements
    If we select option 2, that means we can skip this element and select the element that is left to it.

    Recurse down to the start of the array to get desired sum

    :param arr: Input array
    :return: Max sum possible using non-adjacent elements
    """
    # Edge cases -->
    if not arr:
        return None
    if arr.__contains__(None):
        return None
    for a in arr:
        if type(a) is not int:
            return None
    if len(arr) == 0:
        return 0
    # <-- Edge cases

    # Base case -->
    if len(arr) < 3:
        return max(arr)
    # <-- Base case

    # Include the last element in the sum, and recurse with skipping one element to left of it
    including_last = arr[-1] + largest_sum_of_non_adjacent_numbers(arr[:-2])

    # Exclude the last element in the sum, and recurse with one element to left of it
    excluding_last = largest_sum_of_non_adjacent_numbers(arr[:-1])

    # Get the maximum of the above two variables, this is our result
    return max(including_last, excluding_last)


class Test(unittest.TestCase):
    def test_given_case_1(self):
        self.assertEqual(largest_sum_of_non_adjacent_numbers([2, 4, 6, 2, 5]), 13)

    def test_given_case_2(self):
        self.assertEqual(largest_sum_of_non_adjacent_numbers([5, 1, 1, 5]), 10)

    def test_with_negative(self):
        self.assertEqual(largest_sum_of_non_adjacent_numbers([5, 3, -1]), 5)
        self.assertEqual(largest_sum_of_non_adjacent_numbers([5, 6, -1]), 6)

    def test_with_negatives(self):
        self.assertEqual(largest_sum_of_non_adjacent_numbers([-5, -3, -1]), -3)

    def test_with_zeroes(self):
        self.assertEqual(largest_sum_of_non_adjacent_numbers([0, 0, -1]), 0)
        self.assertEqual(largest_sum_of_non_adjacent_numbers([0, 0, 1]), 1)

    def test_with_None_elements(self):
        self.assertEqual(largest_sum_of_non_adjacent_numbers([0, None, 1, 2]), None)

    def test_with_None_array(self):
        self.assertEqual(largest_sum_of_non_adjacent_numbers(None), None)

    def test_with_invalid_elements(self):
        self.assertEqual(largest_sum_of_non_adjacent_numbers([1, 2, 3.5]), None)
        self.assertEqual(largest_sum_of_non_adjacent_numbers([1, 2, 3, 'a']), None)


if __name__ == '__main__':
    unittest.main()

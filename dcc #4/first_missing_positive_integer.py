import unittest

"""
Given an array of integers, find the first missing positive integer in linear time and constant space. In other
words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and
negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""


def first_missing_positive_integer(arr):
    """
    Move every element to it's index position
    Meaning if current element is 1, swap it with a[0]. Because a[1-1]=a[0]
    Meaning if current element is 2, swap it with a[1]. Because a[2-1]=a[1]
    Ignore elements less than 1 and greater than size of array, because that would mean array has missing elements
    and those missing elements are not in that skipped elements.

    For eg., [1, 2, -1, 10]
    1 and 2 are in correct place
    -1 is ignored
    10 is ignored, because it's place is a[9]. But out array size is 4.

    Then just iterate over array to check if index, value pair matches as value==index+1
    If all values match, that means all elements are at correct place. Return the size of array + 1

    This function returns the missing positive integer from the array

    :param arr: The input array
    :return: int; the missing positive integer
    """

    # Edge case -->
    if not arr:
        return 1
    # <-- Edge case

    # Iterate over array to move elements to "correct" place
    i = 0
    while i < len(arr):
        curr = arr[i]
        if not curr:  # Skipping None elements
            i += 1
            continue
        if 0 >= curr or curr >= len(arr):  # Skipping elements which are less than 1 and greater than len of arr
            i += 1
            continue
        if i + 1 == curr:  # Skipping elements which are already in place
            i += 1
            continue
        if curr == arr[curr - 1]:  # Duplicate element check
            i += 1
            continue
        arr[i], arr[curr - 1] = arr[curr - 1], arr[i]
        if i != 0:
            i -= 1
        else:
            i = 0

    # Iterate over array
    for i, v in enumerate(arr):
        if arr[i] == i + 1:  # If this condition meets, element is in place. So skip
            continue
        else:  # Else return index+1
            return i + 1
    #  All elements in place, return next integer, i.e., len(arr) + 1
    return len(arr) + 1


class Test(unittest.TestCase):
    def test_normal_case_1(self):
        self.assertEqual(first_missing_positive_integer([3, 4, -1, 1]), 2)

    def test_normal_case_2(self):
        self.assertEqual(first_missing_positive_integer([1, 2, 0]), 3)

    def test_empty(self):
        self.assertEqual(first_missing_positive_integer([]), 1)

    def test_with_none_elements_and_duplicates(self):
        self.assertEqual(first_missing_positive_integer([-1, 1, 2, None, 2, 0]), 3)

    def test_with_none_elements(self):
        self.assertEqual(first_missing_positive_integer([None]), 1)
        self.assertEqual(first_missing_positive_integer([None, None, None, None]), 1)

    def test_all_present_with_negatives(self):
        self.assertEqual(first_missing_positive_integer([3, 2, 4, -1, -2, 1]), 5)


if __name__ == '__main__':
    unittest.main()

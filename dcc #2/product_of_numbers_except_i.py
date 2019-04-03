"""Given an array of integers, return a new array such that each element at index i of the new array is the product
of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [
3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?


Aditya M: ASSUMING SINGLE ELEMENT RETURNS SAME ELEMENT
"""

import unittest


def with_division_product_of_all_numbers_except_i(arr):
    """
    Given a list of numbers, returns a new list with product of elements at all position except i
    :param arr: List of numbers
    :return: list with product of elements at all position except i
    """

    # Edge cases --->
    if arr is None:
        return []
    if len(arr) == 0 or len(arr) == 1:
        return arr
    if len(filter(lambda x: x is None, arr)) > 0:
        return []
    if len(filter(lambda x: x == 0, arr)) > 1:
        return [0] * len(arr)
    # <--- Edge cases

    running_product = 1
    return_arr = []
    if arr.__contains__(0):
        for el in arr:
            if el == 0:
                continue
            running_product = el * running_product
        for el in arr:
            if el == 0:
                return_arr.append(running_product)
            else:
                return_arr.append(0)
        return return_arr
    else:
        for el in arr:
            running_product = running_product * el
        for el in arr:
            return_arr.append(running_product / el)
        return return_arr


def without_division_product_of_all_numbers_except_i(arr):
    """
    Given a list of numbers, returns a new list with product of elements at all position except i
    :param arr: List of numbers
    :return: list with product of elements at all position except i
    """

    # Edge cases --->
    if arr is None:
        return []
    if len(arr) == 0 or len(arr) == 1:
        return arr
    if len(filter(lambda x: x is None, arr)) > 0:
        return []
    if len(filter(lambda x: x == 0, arr)) > 1:
        return [0] * len(arr)
    # <--- Edge cases

    # Generate a left running product, i.e., product of all values to left of i'th element
    # Generate a right running product, i.e., product of all values to right of i'th element
    # Multiply each element of both arrays to get desired output

    # Generating left running product -->
    left = 1
    left_arr = [left]
    for el in arr[:-1]:
        left *= el
        left_arr.append(left)
    # <-- Generating left running product

    # Generating right running product -->
    right = 1
    right_arr = [1] * len(arr)
    i = len(arr) - 1

    while i > 0:
        right *= arr[i]
        right_arr[i - 1] = right
        i -= 1
    # <-- Generating right running product

    # Multiplying every element of both arrays -->
    return_arr = []
    for i, j in zip(left_arr, right_arr):
        return_arr.append(i * j)
    # <-- Multiplying every element of both arrays

    return return_arr


class TestSolution(unittest.TestCase):
    def test(self):
        # Normal case
        arr = [1, 2, 3, 4, 5]
        ans_arr = [120, 60, 40, 30, 24]
        self.assertTrue(without_division_product_of_all_numbers_except_i(arr) == ans_arr)

        # With one zero
        arr = [1, 2, 0, 3]
        ans_arr = [0, 0, 6, 0]
        self.assertTrue(without_division_product_of_all_numbers_except_i(arr) == ans_arr)

        # With two zeroes
        arr = [1, 0, 0, 3]
        ans_arr = [0, 0, 0, 0]
        self.assertTrue(without_division_product_of_all_numbers_except_i(arr) == ans_arr)

        # With single element
        arr = [10]
        ans_arr = [10]
        self.assertTrue(without_division_product_of_all_numbers_except_i(arr) == ans_arr)

        # With same elements
        arr = [3, 3, 3]
        ans_arr = [9, 9, 9]
        self.assertTrue(without_division_product_of_all_numbers_except_i(arr) == ans_arr)

        # With negative elements
        arr = [1, -2, 3, -4, 5]
        ans_arr = [120, -60, 40, -30, 24]
        self.assertTrue(without_division_product_of_all_numbers_except_i(arr) == ans_arr)

        # With empty array
        arr = []
        ans_arr = []
        self.assertTrue(without_division_product_of_all_numbers_except_i(arr) == ans_arr)

        # With none values
        arr = [1, None, 0, 3]
        ans_arr = []
        self.assertTrue(without_division_product_of_all_numbers_except_i(arr) == ans_arr)

        # With all none values
        arr = [None, None, None]
        ans_arr = []
        self.assertTrue(without_division_product_of_all_numbers_except_i(arr) == ans_arr)

    def test2(self):
        # Normal case
        arr = [1, 2, 3, 4, 5]
        ans_arr = [120, 60, 40, 30, 24]
        self.assertTrue(with_division_product_of_all_numbers_except_i(arr) == ans_arr)

        # With one zero
        arr = [1, 2, 0, 3]
        ans_arr = [0, 0, 6, 0]
        self.assertTrue(with_division_product_of_all_numbers_except_i(arr) == ans_arr)

        # With two zeroes
        arr = [1, 0, 0, 3]
        ans_arr = [0, 0, 0, 0]
        self.assertTrue(with_division_product_of_all_numbers_except_i(arr) == ans_arr)

        # With single element
        arr = [10]
        ans_arr = [10]
        self.assertTrue(with_division_product_of_all_numbers_except_i(arr) == ans_arr)

        # With same elements
        arr = [3, 3, 3]
        ans_arr = [9, 9, 9]
        self.assertTrue(with_division_product_of_all_numbers_except_i(arr) == ans_arr)

        # With negative elements
        arr = [1, -2, 3, -4, 5]
        ans_arr = [120, -60, 40, -30, 24]
        self.assertTrue(with_division_product_of_all_numbers_except_i(arr) == ans_arr)

        # With empty array
        arr = []
        ans_arr = []
        self.assertTrue(with_division_product_of_all_numbers_except_i(arr) == ans_arr)

        # With none values
        arr = [1, None, 0, 3]
        ans_arr = []
        self.assertTrue(with_division_product_of_all_numbers_except_i(arr) == ans_arr)

        # With all none values
        arr = [None, None, None]
        ans_arr = []
        self.assertTrue(with_division_product_of_all_numbers_except_i(arr) == ans_arr)


if __name__ == '__main__':
    unittest.main()

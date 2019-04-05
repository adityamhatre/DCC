import unittest

"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
 For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
"""


def cons(a, b):
    """
    Function implementation given in question.

    READ SLOWLY:
    This is a function that takes two args, returns a function that takes one function with two args as input

    Notes: Higher order function. Think lambda. Function that returns a function
    :param a: A value
    :param b: Another value
    :return: Function that takes a and b as argument
    """

    def pair(f):
        return f(a, b)

    return pair


def car(func):
    """
    A function that takes function with two args as input
    :param func: Input function
    :return: The first arg of the input function
    """

    # Edge case ->
    if not callable(func):
        raise TypeError("{}({}) is not a function".format(func, type(func)))

    # <-- Edge case

    def get_first(a, _):
        """
        This is the body of function with two args as input
        :param a: 1st arg
        :param _: 2nd arg
        :return: 1st arg
        """
        return a

    # Call the input function with the above function's body
    return func(get_first)


def car_lambda(func):
    """
    A function that takes function with two args as input
    :param func: Input function
    :return: The first arg of the input function USING LAMBDA
    """

    # Edge case ->
    if not callable(func):
        raise TypeError("{}({}) is not a function".format(func, type(func)))

    # <-- Edge case

    # Call the input function with the lambda
    return func(lambda x, _: x)


def cdr(func):
    """
    A function that takes function with two args as input
    :param func: Input function
    :return: The second arg of the function
    """

    # Edge case ->
    if not callable(func):
        raise TypeError("{}({}) is not a function".format(func, type(func)))

    # <-- Edge case

    def get_second(_, b):
        """
        This is the body of function with two args as input
        :param _: 1st arg
        :param b: 2nd arg
        :return: 2nd arg
        """
        return b

    # Call the input function with the above function's body
    return func(get_second)


def cdr_lambda(func):
    """
    A function that takes function with two args as input
    :param func: Input function
    :return: The second arg of the function USING LAMBDA
    """
    # Edge case ->
    if not callable(func):
        raise TypeError("{}({}) is not a function".format(func, type(func)))

    # <-- Edge case

    # Call the input function with the lambda
    return func(lambda _, y: y)


class Test(unittest.TestCase):
    # Base case given in question
    def test_car_base(self):
        self.assertEqual(car(cons(3, 4)), 3)

    # Base case given in question
    def test_cdr_base(self):
        self.assertEqual(cdr(cons(3, 4)), 4)

    # None input in cons function for car
    def test_car_none_input(self):
        self.assertEqual(car(cons(None, 1)), None)

    # None input in cons function for cdr
    def test_cdr_none_input(self):
        self.assertEqual(cdr(cons(1, None)), None)

    # None input in car
    def test_car_edge_case(self):
        self.assertRaises(TypeError, car, None)

    # None input in cdr
    def test_cdr_edge_case(self):
        self.assertRaises(TypeError, cdr, None)

    # Base case given in question
    def test_car_lambda_base(self):
        self.assertEqual(car_lambda(cons(3, 4)), 3)

    # Base case given in question
    def test_cdr_lambda_base(self):
        self.assertEqual(cdr_lambda(cons(3, 4)), 4)

    # None input in cons function for car_lambda
    def test_car_lambda_none_input(self):
        self.assertEqual(car_lambda(cons(None, 1)), None)

    # None input in cons function for cdr_lambda
    def test_cdr_lambda_none_input(self):
        self.assertEqual(cdr_lambda(cons(1, None)), None)

    # None input in car_lambda
    def test_car_lambda_edge_case(self):
        self.assertRaises(TypeError, car_lambda, None)

    # None input in cdr_lambda
    def test_cdr_lambda_edge_case(self):
        self.assertRaises(TypeError, cdr_lambda, None)


if __name__ == '__main__':
    unittest.main()

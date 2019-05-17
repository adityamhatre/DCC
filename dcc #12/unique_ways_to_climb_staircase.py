"""
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N,
write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive
integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""
import unittest


def unique_ways_to_climb_staircase(n, x=None):
    """
    This function gives the total number of ways to climb the staircase of n steps taking x steps
    :param n: Number of steps in staircase
    :param x: Number of steps that one can take in single step
    :return: total number of unique ways
    """
    # Edge case -->
    if n is None:
        raise ValueError("n should not be none")
    if n < 0:
        raise ValueError("n should be greater than 0")
    if x is None:
        x = [1]
    if n == 0:
        return 1
    if len(list(filter(lambda xx: xx < 0, x))) > 0:
        raise ValueError("step values should be greater than 0")
    # <-- Edge case

    steps_for_each_n = [1]  # Array storing answers for each n
    for i in range(1, n + 1):  # Loop through step 1 to n inclusive
        total = 0  # Init total variable
        for j in x:  # Loop through X for adding possible steps
            if i - j >= 0:  # Add only if difference greater than 0
                total += steps_for_each_n[i - j]  # Add to total
        steps_for_each_n.append(total)  # Append the answer for this n
    return steps_for_each_n[-1]  # We are concerned with final n, so return last element


class Test(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(unique_ways_to_climb_staircase(4, [1, 2]), 5)

    def test_base_case_2(self):
        self.assertEqual(unique_ways_to_climb_staircase(4, [1, 3, 5]), 3)

    def test_negative_steps(self):
        self.assertRaises(ValueError, unique_ways_to_climb_staircase, -1, [1, 2])

    def test_negative_possible_steps(self):
        self.assertRaises(ValueError, unique_ways_to_climb_staircase, 5, [1, -2])

    def test_none_n(self):
        self.assertRaises(ValueError, unique_ways_to_climb_staircase, None, [1, -2])


if __name__ == '__main__':
    unittest.main()

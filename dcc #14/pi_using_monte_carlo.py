"""
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.


"""
import random
import unittest
import math


def pi_using_monte_carlo():
    """
    Returns the estimated value of PI

    Generate random points between 0 and 1.
    Increment the counter if the point is in circle's limit
    The counter is the number of points in the circle, i.e., the area of the circle
    Use the formula in the code for the answer.
    :return: estimated value of pi
    """

    c = 0  # Counter for number of points in the unit circle

    interval = 10000000  # Denotes the granularity of the points. Higher the better

    for i in range(interval):  # Run "interval" times
        x = random.random()  # Generate x coordinate
        y = random.random()  # Generate y coordinate
        if x ** 2 + y ** 2 <= 1:  # Check if (x, y) in circle
            c += 1  # Increment the number of points in circle
        if i % 100000 == 0:
            print("Progress: {}%".format(i / 100000))
    print("Progress: {}%".format(interval / 100000))
    return 4 * c / interval  # Return calculated PI


class Test(unittest.TestCase):

    def test_base_case(self):
        self.assertAlmostEqual(pi_using_monte_carlo(), math.pi, 3)


if __name__ == '__main__':
    unittest.main()

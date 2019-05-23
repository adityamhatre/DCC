"""
Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
"""
import random


def select(i, count, x):
    """
    Helper function to determine if :param i should be picked or not depending on the probability

    :param i: Number in consideration
    :param count: Total numbers seen so far
    :param x: Current picked random number
    :return: :param x or :param i
    """

    probability = random.random()  # Generate random number for checking probability
    if count == 1:  # Only number so far, so pick this
        return i
    if probability <= 1 / count:  # Check if generated probability falls under calculated probability to pick new number
        return i  # Pick new number
    else:  # Generated probability is out of bounds
        return x  # Return last picked number


def random_element_from_stream(stream):
    """
    Get's a random number from infinite stream
    :param stream: Stream of numbers
    :return: Random number from the stream
    """

    count = 0  # Count to keep track of how many numbers seen so far
    x = stream[0]  # Candidate number
    for i in stream:  # Go through each number in stream
        count += 1  # Increase seen numbers count
        x = select(i, count, x)  # Call the helper function
    return x  # Return value


# HAVE NO IDEA HOW WOULD I TEST THIS.
# CAN DO A TEST CASE TO CHECK IF GENERATED NUMBER IS PRESENT IN THE LIST OR NOT. BUT THAT'S FAIRLY OBVIOUS

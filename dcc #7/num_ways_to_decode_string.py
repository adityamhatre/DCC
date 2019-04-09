import unittest

"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""


def num_ways_decode(string, cache=None):
    """
    Returns the number of ways, the given numeric string can be decoded to alphabet
    :param string: Input numeric string
    :param cache: Cache, used for memoization
    :return: number of ways the string can be decoded
    """
    # Edge cases -->
    if cache is None:
        cache = {}
    if string is None:
        return 0
    for s in string:
        if s.isalpha():
            return 0
    # <-- Edge cases

    # Base cases -->
    if string == "":
        return 1
    if len(string) == 1:
        if string[0] == "0":
            return 0
        return 1
    if len(string) > 1:
        if string[0] == "0":
            return 0
    # <-- Base cases

    first_digit = int(string[0])  # Extract first digit from string
    combined_first_second = 10 * first_digit + int(string[1])  # Combine with second digit
    if combined_first_second > 26:  # Check if greater than 26
        return 1  # Only one way to decode
    else:  # Else there are recursive num_ways(first) + num_ways(second) ways to decode
        first = string[1:]  # Exclude first char and get rest of string
        second = string[2:]  # Exclude first two chars and get rest of string

        # Check cache for existing elements, if not, then add to cache
        cache[first] = num_ways_decode(first, cache) if first not in cache else cache[first]
        cache[second] = num_ways_decode(second, cache) if second not in cache else cache[second]

        # Return the sum of num_ways_decode of first and second
        return cache[first] + cache[second]


class Test(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(num_ways_decode("12345"), 3)

    def test_case_for_memoization(self):
        self.assertEqual(num_ways_decode("111"), 3)

    def test_case_12131(self):
        self.assertEqual(num_ways_decode("12131"), 5)

    def test_case_start_with_0(self):
        self.assertEqual(num_ways_decode("011"), 0)
        self.assertEqual(num_ways_decode("01213"), 0)

    def test_case_empty(self):
        self.assertEqual(num_ways_decode(""), 1)

    def test_case_random(self):
        self.assertEqual(num_ways_decode("226"), 3)

    def test_case_none(self):
        self.assertEqual(num_ways_decode(None), 0)

    def test_case_invalid_chars(self):
        self.assertEqual(num_ways_decode("123a"), 0)


if __name__ == '__main__':
    unittest.main()

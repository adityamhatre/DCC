"""
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

import unittest


def process(considering, single):
    """
    Helper function to get number of distinct chars in current window
    :param considering: The substring or letter depending on the :param single
    :param single: Boolean to determine considering a new window or extending a new window. If this is true, we are
    extending the window
    :return: Length of distinct chars in window
    """

    if not single:  # Clear map of count since this is a new window
        for l in hashed:
            hashed[l] = 0

    for l in considering:  # Update count of chars in the map
        hashed[l] = 1 if l not in hashed else hashed[l] + 1

    # Calculate the unique chars in the map whose count > 0
    s = 0
    for l in hashed:
        if hashed[l] > 0:
            s += 1

    return s  # Return the count


# HashMap to store occurrences of chars in the window
hashed = {}


def longest_substring_k_distinct_characters(s, k):
    """
    Gets the longest substring length with at most :param k unique chars
    :param s: String to be processed
    :param k: Maximum number of unique character allowed
    :return: Length of longest substring

    This problem is solved using sliding window.
    Start by window size at i=0, check the unique chars, if unique chars less than :param k, extend the window by 1
    If unique chars exceeds :param k, move the window by 1 from left side and do over again.
    """

    # Edge cases -->
    if s is None:
        raise ValueError("s must be non None")
    if len(s) <= 1:
        return len(s)
    if k is None:
        raise ValueError("k must be non None")
    if k < 1:
        raise ValueError("k must be positive integer")
    if type(k) is not int:
        raise TypeError("k must be int")
    # <-- Edge cases

    # Initialization -->
    i = 0
    default_k = k
    answer = ""
    single = False
    # <-- Initialization

    while i < len(s):  # Loop through every char
        if i + k > len(s):  # If window end reached end of string, return answer
            return len(answer)
        if not single:  # Not single, meaning new window
            considering = s[i:i + k]
        else:  # Single, meaning we are extending the window
            considering = s[i + k - 1]
        if process(considering, single) <= default_k:  # Unique chars within limits
            if not single:  # Not single, meaning new window, therefore new answer
                if len(considering) >= len(answer):
                    answer = considering
                    single = True  # Try to extend the window with single char
            else:  # Single, meaning we can add this "single" letter to the answer since unique chars
                # count is still within limits
                answer += considering
            k += 1  # Extend the window
        else:  # Unique chars not within limits, reset the window by moving start point by 1
            single = False  # Get new substring
            i += 1  # Move start point by 1
            k = default_k  # Reset window size to original k


class Test(unittest.TestCase):
    def test_base_case(self):
        s = "abcba"
        k = 2
        self.assertEqual(longest_substring_k_distinct_characters(s, k), 3)

    def test_different_cases(self):
        s = "helhlthere"
        k = 5
        self.assertEqual(longest_substring_k_distinct_characters(s, k), 10)

        s = "hehlothe"
        k = 2
        self.assertEqual(longest_substring_k_distinct_characters(s, k), 3)

        s = "abbcdef"
        k = 4
        self.assertEqual(longest_substring_k_distinct_characters(s, k), 5)

        s = "helhstherresthever"
        k = 5
        self.assertEqual(longest_substring_k_distinct_characters(s, k), 12)

        s = "helhsther"
        k = 5
        self.assertEqual(longest_substring_k_distinct_characters(s, k), 8)

        s = "karappa"
        k = 3
        self.assertEqual(longest_substring_k_distinct_characters(s, k), 6)

        s = "hhhhelhsther"
        k = 5
        self.assertEqual(longest_substring_k_distinct_characters(s, k), 11)

        s = "hhhhhhhhh"
        k = 5
        self.assertEqual(longest_substring_k_distinct_characters(s, k), 9)

        s = "ab"
        k = 2
        self.assertEqual(longest_substring_k_distinct_characters(s, k), 2)

    def test_none_string(self):
        s = None
        k = 1
        self.assertRaises(ValueError, longest_substring_k_distinct_characters, s, k)

    def test_none_k(self):
        s = "adsf"
        k = None
        self.assertRaises(ValueError, longest_substring_k_distinct_characters, s, k)

    def test_negative_k(self):
        s = "adsf"
        k = -1
        self.assertRaises(ValueError, longest_substring_k_distinct_characters, s, k)

    def test_not_int_k(self):
        s = "adsf"
        k = 1.5
        self.assertRaises(TypeError, longest_substring_k_distinct_characters, s, k)


if __name__ == '__main__':
    unittest.main()

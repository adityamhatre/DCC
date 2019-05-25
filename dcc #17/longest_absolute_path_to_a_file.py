"""
Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty
second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file
file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For
example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length
is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to a
file in the abstracted file system. If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.
"""
import unittest


class File:
    """
    File Class to store information about file.
    """

    def __init__(self, inode, name, level):
        """
        Initialize file
        :param inode: The id of the file
        :param name: The name of the file
        :param level: The level in the file system of the file
        """
        self.inode = inode
        self.name = name
        self.level = level

    def __repr__(self):
        return "{}\t{}\t{}".format(self.inode, self.name, self.level)


class FileSystem:
    """
    Data Structure to store all files
    """

    def __init__(self):
        self.files = []

    def add(self, file_obj):
        self.files.append(file_obj)


child_parent_map = {}  # The backbone of this algorithm. Map of child inode to it's parent inode
file_system = FileSystem()


def parent_of(inode, level, temp_len):
    """
    This function find's the immediate parent of an inode by traversing the file system in reverse It finds the
    parent when the level of the ith inode is exactly 1 less than the input's inode level The function then recurses
    until it reaches the root dir of the file system saving the length until now in the :param temp_len

    :param inode: The input file inode whose parent is to be found
    :param level: The level of the input file
    :param temp_len: The current length of absolute path
    :return:
    """
    # Check in map, if we have the parent of this child inode
    if inode in child_parent_map:  # Yes, we have
        # Add the length of current file name and plus 1 for the "\" part
        temp_len += len(file_system.files[inode].name) + 1

        # Now check if we want to recurse or not. If the current level is not 0, meaning this is not root, so recurse,
        # else we have reached the root, now add the root name len
        if not child_parent_map[inode] == 0:
            return parent_of(child_parent_map[inode], level - 1, temp_len)
        else:
            return temp_len + len(file_system.files[0].name)

    # Start from one less inode to start finding parent
    i = inode - 1

    # Loop until we reach the root or find the parent
    while i >= 0:
        # If the ith file's level is 1 less than current file's level
        # We have found the parent of the current file
        if file_system.files[i].level == level - 1:
            # Save the child -> parent inode values to be used later
            child_parent_map[inode] = i

            # Add the length of current file name and plus 1 for the "\" part
            temp_len += len(file_system.files[inode].name) + 1

            # Now check if we want to recurse or not. If the current level is not 0,
            # meaning this is not root, so recurse,  else we have reached the root, now add the root name len
            if not file_system.files[i].level == 0:
                return parent_of(file_system.files[i].inode, level - 1, temp_len)
            else:
                return temp_len + len(file_system.files[0].name)
        i -= 1

    # Cannot find the parent of the file, return root dir's name length as default length
    return temp_len + len(file_system.files[0].name)


def longest_absolute_path_to_a_file(file_system_string):
    """
    Find's the longest and not deepest absolute path to a file from the root
    :param file_system_string: The file system represented as a string
    :return: The longest absolute path to a file
    """

    # Edge cases-->
    if file_system_string is None:
        raise TypeError("input file string is none")

    if file_system_string == "":
        return 0

    if not file_system_string.__contains__("."):
        return 0
    # <--Edge cases

    # Split the file system based on new line, so we preserve the order in which they are represented
    nodes = file_system_string.split("\n")

    max_len = 0  # Return variable

    # Loop through all nodes and add them to the data structure
    for i, node in enumerate(nodes):
        _inode = i
        _name = node.replace("\t", "")
        _level = node.count("\t")
        _file = File(_inode, _name, _level)
        file_system.add(_file)

    # Start from the last file and start finding it's parent until the root
    # We start from reverse since that way it's easier to link a child to a parent file,
    # i.e., we don't have to keep track of current subdir when traversing the file system
    for f in reversed(file_system.files):
        if f.name.__contains__("."):
            # Find the length of the absolute path of the current file
            len_of_current_file = parent_of(f.inode, f.level, temp_len=0)

            # Find the maximum length
            max_len = max(max_len, len_of_current_file)

    # Return the maximum length until now
    return max_len


class Test(unittest.TestCase):
    def tearDown(self):
        global child_parent_map
        global file_system
        child_parent_map = {}
        file_system = FileSystem()

    def test_base_case(self):
        fs = "dir\n\tsubdir1\n\t\tsubsubdir1\n\t\tfile1.ext\n\t\tfile2.ext\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tsubsubsubdir1\n" \
             "\t\t\tfile2.ext\n\t\t\tsubsubsubdir2\n\tfile3.ext"
        self.assertEqual(longest_absolute_path_to_a_file(fs), 32)

    def test_none_file_system(self):
        fs = None
        self.assertRaises(TypeError, longest_absolute_path_to_a_file, fs)

    def test_no_file_in_file_system(self):
        fs = "dir\n\tsubdir1\n\t\tsubdir2"
        self.assertEqual(longest_absolute_path_to_a_file(fs), 0)

    def test_my_case(self):
        fs = "dir\n\ts1\n\t\tf1.ext\n\t\tf2.ext2\n\t\ts2\n\t\t\tf1.ext\n\ts2\n\t\tf1.ext\n\tffffffffffffffff.ext"
        self.assertEqual(longest_absolute_path_to_a_file(fs), 24)


if __name__ == '__main__':
    unittest.main()

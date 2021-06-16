# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]), [28, 26])

if __name__ == '__main__':
    unittest.main()
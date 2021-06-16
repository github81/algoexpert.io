# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0), [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]])

if __name__ == '__main__':
    unittest.main()
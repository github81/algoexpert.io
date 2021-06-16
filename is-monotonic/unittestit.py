# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11]
        expected = True
        actual = program.isMonotonic(array)
        self.assertEqual(actual, expected)
        
if __name__ == '__main__':
    unittest.main()
    
    

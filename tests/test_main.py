# Import necessary libraries
import unittest
import sys
import os

# Add the project root directory to the Python path
# This allows us to import the 'main' module from the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import add

class TestAdd(unittest.TestCase):
    """Test suite for the add function in main.py"""

    def test_add(self):
        """Test cases for the add function."""
        # Test with two positive integers
        self.assertEqual(add(2, 3), 5)
        # Test with a negative and a positive integer
        self.assertEqual(add(-1, 1), 0)
        # Test with two negative integers
        self.assertEqual(add(-1, -1), -2)
        # Test with floating point numbers
        self.assertAlmostEqual(add(1.1, 2.2), 3.3)

# This allows the test to be run from the command line
if __name__ == '__main__':
    unittest.main()

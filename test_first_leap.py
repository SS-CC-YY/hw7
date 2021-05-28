import unittest
import leap_year

class testCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(leap_year.leap_year(2020), "It is a leap year!")
    
if __name__ == "__main__":
    unittest.main(verbosity=2)
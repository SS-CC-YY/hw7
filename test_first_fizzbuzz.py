import unittest
import first_fizzbuzz

class testCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(first_fizzbuzz.fizzbuzz(3), "Fizz")
    def test_case_2(self):
        self.assertEqual(first_fizzbuzz.fizzbuzz(5), "Buzz")
    def test_case_3(self):
        self.assertEqual(first_fizzbuzz.fizzbuzz(15), "FizzBuzz")

if __name__ == "__main__":
    unittest.main(verbosity=2)
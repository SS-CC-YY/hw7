import unittest
import first_fizzbuzz

class testCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(first_fizzbuzz.fizzbuzz(3), "Fizz")
    def test_case_2(self):
        self.assertEqual(first_fizzbuzz.fizzbuzz(27), "Fizz")
    def test_case_3(self):
        self.assertEqual(first_fizzbuzz.fizzbuzz(99), "Fizz")

    def test_case_4(self):
        self.assertEqual(first_fizzbuzz.fizzbuzz(5), "Buzz")
    def test_case_5(self):
        self.assertEqual(first_fizzbuzz.fizzbuzz(25), "Buzz")
    def test_case_6(self):
        self.assertEqual(first_fizzbuzz.fizzbuzz(95), "Buzz")

    def test_case_7(self):
        self.assertEqual(first_fizzbuzz.fizzbuzz(15), "FizzBuzz")
    def test_case_8(self):
        self.assertEqual(first_fizzbuzz.fizzbuzz(45), "FizzBuzz")
    def test_case_9(self):
        self.assertEqual(first_fizzbuzz.fizzbuzz(60), "FizzBuzz")

if __name__ == "__main__":
    unittest.main(verbosity=2)
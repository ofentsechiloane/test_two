import unittest
from my_module import (
    sum_even_numbers, 
    reverse_string, 
    count_vowels, 
    factorial, 
    fibonacci, 
    word_count_in_file
)

class TestMyModule(unittest.TestCase):

    # Test sum of even numbers
    def test_sum_even_numbers(self):
        self.assertEqual(sum_even_numbers([1, 2, 3, 4, 5, 6]), 12)
        self.assertEqual(sum_even_numbers([7, 9, 11]), 0)
        self.assertEqual(sum_even_numbers([]), 0)

    # Test reversing a string
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")
        self.assertEqual(reverse_string(""), "")

    # Test counting vowels
    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("xyz"), 0)

    # Test factorial calculation
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)

    # Test Fibonacci sequence
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(10), 55)

    # Test reading a file and counting word occurrences
    def test_word_count_in_file(self):
        test_file = "test_text.txt"
        # create a temporary test file
        with open(test_file, "w") as f:
            f.write("hello world hello python")

        expected_count = {
            "hello": 2,
            "world": 1,
            "python": 1
        }
        self.assertEqual(word_count_in_file(test_file), expected_count)

if __name__ == "__main__":
    unittest.main()

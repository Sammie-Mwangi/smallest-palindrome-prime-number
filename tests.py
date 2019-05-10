import unittest
from logic.check_prime_number import check_if_number_is_prime
from logic.check_palindrome_number import check_if_number_is_palindrome

class SmallestPalindromePrime(unittest.TestCase):
    def number_is_prime(self):
        self.assertTrue(check_if_number_is_prime(7))
        self.assertTrue(check_if_number_is_prime(17))
        self.assertFalse(check_if_number_is_prime(8))
        self.assertFalse(check_if_number_is_prime(9998))

    def number_is_palindrome(self):
        self.assertTrue(check_if_number_is_palindrome(99))
        self.assertTrue(check_if_number_is_palindrome(88))
        self.assertFalse(check_if_number_is_palindrome(12345634))
        


if __name__ == '__main__':
    unittest.main()


# Running  the tests ==> python -m unittest tests.SmallestPalindromePrime.number_is_prime
#                    ==> python -m unittest tests.SmallestPalindromePrime.number_is_palindrome
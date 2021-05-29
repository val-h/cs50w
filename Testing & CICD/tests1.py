import unittest

from prime import is_prime


class Tests(unittest.TestCase):

    def test_1(self):
        """Check that 1 is not prime."""
        self.assertFalse(is_prime(1))

    def test_2(self):
        """Check that 2 is prime."""
        self.assertTrue(is_prime(2))

    def test_5(self):
        """Check that 5 is prime."""
        self.assertTrue(is_prime(5))

    def test_8(self):
        """Check that 8 is not prime."""
        self.assertFalse(is_prime(8))

    def test_10(self):
        """Check that 10 is not prime."""
        self.assertFalse(is_prime(10))

    def test_13(self):
        """Check that 13 is prime."""
        self.assertTrue(is_prime(13))

    def test_17(self):
        """Check that 17 is prime."""
        self.assertTrue(is_prime(17))

    def test_20(self):
        """Check that 20 is not prime."""
        self.assertFalse(is_prime(20))

    def test_25(self):
        """Check that 25 is not prime."""
        self.assertFalse(is_prime(25))


if __name__ == "__main__":
    unittest.main()

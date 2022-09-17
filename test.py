import unittest

from cleaner import Cleaner

class BaseTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.cleaner = Cleaner()

    def test_is_correct_path(self):
        self.assertEqual(self.cleaner.is_correct_path("D:/"), True)
        self.assertEqual(self.cleaner.is_correct_path("/"), False)


if __name__ == "__main__":
    unittest.main()

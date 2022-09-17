from genericpath import isfile
import unittest
import stat
import os

from cleaner import Cleaner

class BaseTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.cleaner = Cleaner()

    def test_is_correct_path(self):
        self.assertEqual(self.cleaner.is_correct_path("D:/"), True)
        self.assertEqual(self.cleaner.is_correct_path("/"), False)

    def test_remove_file(self):
        import util
        test_folder_name = util.mk_test_dir()
        for obj in os.listdir(test_folder_name):
            if self.cleaner.is_file(f"{test_folder_name}/{obj}"):
                self.cleaner.remove_file(f"{test_folder_name}/{obj}")
        self.assertEqual(len(util.return_only_files(test_folder_name)), 0)

if __name__ == "__main__":
    unittest.main()
from genericpath import isfile
import unittest
import stat
import os
import util


from base_cleaner import BaseCleaner
from cleaner import Cleaner

class BaseCleanerTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.cleaner = BaseCleaner()

    def test_is_correct_path(self):
        self.assertEqual(self.cleaner.is_correct_path("D:/"), True)
        self.assertEqual(self.cleaner.is_correct_path("/"), False)
        self.assertEqual(self.cleaner.is_correct_path("/Univesity"), False)

    def test_remove_file(self):
        test_folder_name = util.mk_test_dir()
        for obj in os.listdir(test_folder_name):
            if self.cleaner.is_file(f"{test_folder_name}/{obj}"):
                self.cleaner.remove_file(f"{test_folder_name}/{obj}")
        self.assertEqual(len(util.return_only_files(test_folder_name)), 0)

    def test_remove_dir_not_recursive(self):
        test_folder_name = util.mk_test_dir()
        self.cleaner.remove_dir(test_folder_name)
        self.assertEqual(len(util.return_only_files(test_folder_name)), 0)

    def test_remove_dir_recursive(self):
        test_folder_name = util.mk_test_dir()
        self.cleaner.remove_dir(test_folder_name, recursive=True)
        self.assertEqual(os.path.exists(test_folder_name), False)


if __name__ == "__main__":
    unittest.main()
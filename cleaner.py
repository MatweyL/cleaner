import os
from pathlib import Path


class Cleaner:

    def __init__(self):
        pass

    def is_correct_path(self, path):
        """User must type only absolute paths"""
        return Path(path).is_absolute()

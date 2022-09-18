import os
from pathlib import Path


class BaseCleaner:

    def __init__(self):
        pass

    def is_correct_path(self, path):
        """User must type only absolute paths"""
        return Path(path).is_absolute()

    def is_file(self, path):
        return os.path.isfile(path)

    def remove_file(self, path):
        os.remove(path)
        print(f"removed {path}")

    def remove_dir(self, path, recursive=False):
        """recursive files and folders deletion"""
        objs = os.listdir(path)
        for obj in objs:
            path_to_obj = f"{path}/{obj}"
            if self.is_file(path_to_obj):
                self.remove_file(path_to_obj)
            elif recursive:
                self.remove_dir(path_to_obj, recursive=recursive)
        try:
            os.rmdir(path)
            print(f"removed dir {path}")
        except BaseException as e:
            pass

    def get_objects_will_be_removed(self, path, recursive):
        objects_to_remove = []
        objs = os.listdir(path)
        for obj in objs:
            path_to_obj = f"{path}/{obj}"
            objects_to_remove.append(path_to_obj)
            if not self.is_file(path_to_obj) and recursive:
                objects_to_remove.extend(self.get_objects_will_be_removed(path_to_obj, recursive=recursive))
        return objects_to_remove


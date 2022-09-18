from base_cleaner import BaseCleaner


class Cleaner(BaseCleaner):

    def __init__(self):
        super().__init__()

    def clean(self):
        path = input("path: ")
        if not self.is_correct_path(path):
            print("path: {path} is not absolute")
        else:
            if self.is_file(path):
                print(f"file {path} will be removed")
                confirmation = input("delete (y/n): ")
                if confirmation == 'y':
                    self.remove_file(path)
            else:
                recursive = False
                delete_mode = input("recursive deletion mode (y/n)): ")
                if delete_mode == 'y':
                    recursive = True
                print("these objects will be removed:")
                for obj in self.get_objects_will_be_removed(path, recursive):
                    print(obj)
                confirmation = input("delete (y/n): ")
                if confirmation == 'y':
                    self.remove_dir(path, recursive)
        print("done")

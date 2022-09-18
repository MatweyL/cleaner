import os
from random import randint
from datetime import datetime


def get_project_root():
    return os.path.dirname(os.path.abspath(__file__))


def mk_file(path, filename):
    with open(f"{path}/{filename}", "w") as file:
        file.write("smth")


def mk_dir(path, dirname):
    os.mkdir(f"{path}/{dirname}")


def mk_test_dir():
    base_folder_name = "folder{}"
    base_file_name = "file{}.txt"
    test_folder_name = f"{get_project_root()}/folder"
    if os.path.exists(test_folder_name):
        test_folder_name += str(hash(datetime.now()))
    if not os.path.exists(test_folder_name):
        os.mkdir(test_folder_name)
        base_path = test_folder_name
        for i in range(10):
            r = randint(0, 8)
            if r % 4 != 0:
                mk_file(base_path, base_file_name.format(i))
            else:
                mk_dir(base_path, base_folder_name.format(i))
                base_path = f"{base_path}/{base_folder_name.format(i)}"
    return test_folder_name


def return_only_files(path):
    files = []
    if os.path.exists(path):
        objects = os.listdir(path)
        for obj in objects:
            if os.path.isfile(obj):
                files.append(obj)

    return files



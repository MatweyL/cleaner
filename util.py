import os

def get_project_root():
    return os.path.dirname(os.path.abspath(__file__))



def mk_test_dir():
    base_folder_name = "folder{}"
    base_file_name = "file{}.txt"
    test_folder_name = f"{get_project_root()}/folder"
    try:
        os.rmdir(test_folder_name)
    except BaseException:
        pass
    if not os.path.exists(test_folder_name):
        os.mkdir(test_folder_name)
        for i in range(5):
            with open(f"{test_folder_name}/{base_file_name.format(i)}", "w") as file:
                file.write("smth")
    return test_folder_name


def return_only_files(path):
    files = []
    objects = os.listdir(path)
    for obj in objects:
        if os.path.isfile(obj):
            files.append(obj)

    return files
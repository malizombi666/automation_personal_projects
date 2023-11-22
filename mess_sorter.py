import os
import shutil


def exists_directory(main_directory, name):
    with os.scandir(main_directory) as items:
        for item in items:
            if item.is_dir() and item.name == name:
                return 1
            else:
                return 0


def create_new_directory(new_dir_name, dir_path):
    new_dir_path = os.path.join(dir_path, new_dir_name)
    try:
        os.mkdir(new_dir_path)
        print(f'a new {new_dir_name} directory has been created')
    except FileExistsError:
        print(f'the directory already exists')
    except Exception as e:
        print(f"an error occured: {e}")


def extension(file):
    try:
        ind = file.name.rindex('.')
        return file.name[ind + 1:].lower()
    except ValueError:
        return file.name


def move_to_its_directory(file_path, destination_directory_path):
    try:
        shutil.move(file_path, destination_directory_path)
    except Exception as e:
        print(f"An error occured {e}")


def list_files(directory):
    with os.scandir(directory) as items:
        for item in items:
            print(f'item is --> {item}')
            if item.is_file():
                if exists_directory(directory, extension(item)):
                    move_to_its_directory(os.path.join(
                        directory, item), os.path.join(directory, extension(item)))
                else:
                    create_new_directory(extension(item), directory)
                    move_to_its_directory(os.path.join(
                        directory, item), os.path.join(directory, extension(item)))
            # add a part if the item is a directory
                # print(item.name)


directory_path = '/Users/manelle/Downloads/'
list_files(directory_path)


# count = 0
# with os.scandir(directory_path) as items:
#     for item in items:
#         if item.is_file():
#             count += 1
#             print(extension(item))
# print(f'count is {count}')
# with open(directory_path, "r") as directory:
#     files = directory.readlines()


# for item in directory_path:
#     print(extension(item))
# print(extension(mane.mp3))

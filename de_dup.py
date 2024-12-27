import os


def find_matching_files(directory):
    duplicates = {}
    # Traverse through the directory
    dir_files = os.listdir(directory)
    for i in range(len(dir_files)):
        file_1 = dir_files[i]
        print(f"Checking file: {file_1}")
        file_1_path = os.path.join(directory, file_1)
        if os.path.isfile(file_1_path):
            for j in range(i + 1, len(dir_files)):
                file_2 = dir_files[j]
                file_2_path = os.path.join(directory, file_2)
                if os.path.isfile(file_2_path):
                    if os.path.getsize(file_1_path) == os.path.getsize(file_2_path):
                        print(f"Files {file_1} and {file_2} are duplicates")
                        if file_1 not in duplicates:
                            duplicates[file_1] = [file_2]
                        else:
                            duplicates[file_1].append(file_2)


if __name__ == "__main__":
    directory = input("Enter the directory path to search: ")
    matching_files = find_matching_files(directory)

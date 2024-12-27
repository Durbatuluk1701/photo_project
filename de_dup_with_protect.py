import os
import hashlib
import sys
from tqdm import tqdm


def calculate_hash(file_path, block_size=65536):
    file_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for block in iter(lambda: f.read(block_size), b""):
            file_hash.update(block)
    return file_hash.hexdigest()


def find_duplicate_files(directory):
    # Start by making a progress bar
    # Get the total number of files to process
    total_files = sum([len(files) for r, d, files in os.walk(directory)])
    progress_bar = tqdm(total=total_files, desc="Processing files")

    files_hash = {}
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_hash = calculate_hash(file_path)
            if file_hash not in files_hash:
                files_hash[file_hash] = [file_path]
            else:
                files_hash[file_hash].append(file_path)
            progress_bar.update(1)

    progress_bar.close()
    return files_hash


if __name__ == "__main__":
    arguments = sys.argv[1:]
    if len(arguments) != 1:
        print("Usage: python de_dup_new.py <directory>")
        sys.exit(1)

    hash_map = find_duplicate_files(arguments[0])
    photos_with_dups = [
        len(hash_map[item]) for item in hash_map if len(hash_map[item]) > 1
    ]
    # print the total number of duplicates
    total_duplicates = sum(photos_with_dups)
    print(f"Total Number of Photos with Duplicates found: {len(photos_with_dups)}")
    print(f"Total Number of Duplicates found: {total_duplicates}")
    # ask user if they want to go through the cleaning process
    response = input("Do you want to remove duplicates? (y/n): ")
    if response.lower() != "y":
        sys.exit(0)
    # iterate through the hash_map
    for item in hash_map:
        cur_item = hash_map[item]
        if len(cur_item) > 1:
            print(f"Files {','.join(cur_item)} are all duplicates")
            # print each file corresponding to a number
            for i in range(0, len(cur_item)):
                print(f"{i}: {cur_item[i]}")
            # Ask the user which file they want to keep
            response = input("Enter the number of the file you want to keep: ")
            response = int(response)
            # tell user which file is being saved
            print(f"Saving file: {cur_item[response]}")
            # Delete all other files
            for i in range(0, len(cur_item)):
                if i != response:
                    print(f"Removing file: {cur_item[i]}")
                    os.remove(cur_item[i])

import os
import hashlib
import sys


def calculate_hash(file_path, block_size=65536):
    file_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for block in iter(lambda: f.read(block_size), b""):
            file_hash.update(block)
    return file_hash.hexdigest()


def find_duplicate_files(directory):
    files_hash = {}
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_hash = calculate_hash(file_path)
            if file_hash not in files_hash:
                files_hash[file_hash] = [file_path]
            else:
                files_hash[file_hash].append(file_path)
    return files_hash


if __name__ == "__main__":
    arguments = sys.argv[1:]
    if len(arguments) != 1:
        print("Usage: python de_dup_new.py <directory>")
        sys.exit(1)

    hash_map = find_duplicate_files(arguments[0])
    for item in hash_map:
        cur_item = hash_map[item]
        if len(cur_item) > 1:
            print(f"Files {','.join(cur_item)} are all duplicates")
            for i in range(1, len(cur_item)):
                print(f"Removing file: {cur_item[i]}")
                os.remove(cur_item[i])

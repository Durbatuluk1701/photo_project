import os
import sys
import datetime


def rename_photos(directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if os.path.isfile(file_path):
                # Code for file
                # Get the last modified date of the file
                _, extension = os.path.splitext(file_path)
                last_modified = os.path.getmtime(file_path)
                last_mod_date = datetime.datetime.fromtimestamp(last_modified)
                counter = 0
                while True:
                    new_file_name = os.path.join(dirpath, f"{last_mod_date.isoformat().replace(":", "-")}{f"_({counter})" if counter > 0 else ""}{extension}")
                    if os.path.exists(new_file_name):
                        counter += 1
                        continue
                    else:
                        os.rename(file_path, new_file_name)
                        break
            else:
                # Code for directory
                break


if __name__ == "__main__":
    arguments = sys.argv[1:]
    if len(arguments) != 1:
        print(f"Usage: python {sys.argv[0]} <directory>")
        sys.exit(1)

    rename_photos(arguments[0])

import os
import tkinter as tk
from PIL import Image, ImageTk


def get_file_info(file_path):
    if os.path.exists(file_path):
        # Get file size
        size_bytes = os.path.getsize(file_path)
        size_kb = size_bytes / 1024  # Convert bytes to kilobytes
        size_mb = size_kb / 1024  # Convert kilobytes to megabytes

        # Get file modification time
        modification_time = os.path.getmtime(file_path)

        return {
            "size_bytes": size_bytes,
            "size_kb": size_kb,
            "size_mb": size_mb,
            "modification_time": modification_time,
        }
    else:
        return None


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
                        # file_1_fd = open(file_1_path, "rb")
                        # file_1_bin = file_1_fd.read()
                        # file_1_fd.close()
                        # file_2_fd = open(file_2_path, "rb")
                        # file_2_bin = file_2_fd.read()
                        # file_2_fd.close()
                        # if file_1_bin == file_2_bin:
                        print(f"Files {file_1} and {file_2} are duplicates")
                        if file_1 not in duplicates:
                            duplicates[file_1] = [file_2]
                        else:
                            duplicates[file_1].append(file_2)
                    # file_1_fd = open(os.path.join(directory, file_1), "rb")
                    # file_1_bin = file_1_fd.read()
                    # file_1_fd.close()
                    # file_2_fd = open(os.path.join(directory, file_2), "rb")
                    # file_2_bin = file_2_fd.read()
                    # file_2_fd.close()
                    # if file_1_bin == file_2_bin:
                    #     print(f"Files {file_1} and {file_2} are duplicates")
            # file_1_fd = open(file_1, "rb")
            # file_1_bin = file_1_fd.read()
            # file_1_fd.close()
            # for alt_file in dir_files:
            #     file_2_fd = open(alt_file, "rb")
            #     file_2_bin = file_2_fd.read()
            #     file_2_fd.close()
            #     if file_1_bin == file_2_bin:
            #         print(f"Files {file_1} and {alt_file} are duplicates")


# def display_side_by_side(files, directory):
#     root = tk.Tk()
#     root.title("Matching Images")

#     for pattern, filenames in files.items():
#         if len(filenames) >= 2:
#             frame = tk.Frame(root)
#             frame.pack()

#             label = tk.Label(frame, text=f"Files matching pattern '{pattern}':")
#             label.pack()

#             images = []
#             for filename in filenames:
#                 image_path = os.path.join(directory, filename)
#                 image = Image.open(image_path)
#                 image.thumbnail((200, 200))  # Thumbnail size for display
#                 tk_image = ImageTk.PhotoImage(image)
#                 images.append(tk_image)

#                 image_label = tk.Label(frame, image=tk_image)
#                 image_label.pack(side=tk.LEFT, padx=5)

#     root.mainloop()


if __name__ == "__main__":
    directory = input("Enter the directory path to search: ")
    # pattern = input("Enter the pattern to search for: ")

    matching_files = find_matching_files(directory)
    # display_side_by_side(matching_files, directory)

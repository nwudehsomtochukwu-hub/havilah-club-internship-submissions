# Day 15 - Python Automation Project
# File Organiser: sorts the files in a folder into subfolders by file extension

import os
import shutil

BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(BASE_FOLDER, "data", "input")
OUTPUT_PATH = os.path.join(BASE_FOLDER, "data", "output")


# Function 1: Get the folder name for a file

def get_extension(file_name):
    extension = os.path.splitext(file_name)[1].lower().lstrip(".")

    if extension == "":
        return "No Extension"
    return extension.upper()


# Function 2: Avoid overwriting files with the same name

def get_free_name(folder, file_name):
    name, extension = os.path.splitext(file_name)
    new_name = file_name
    counter = 1

    while os.path.exists(os.path.join(folder, new_name)):
        new_name = name + "_" + str(counter) + extension
        counter = counter + 1

    return new_name


# Function 3: Check that the input folder is usable

def check_folder(folder):
    if not os.path.exists(folder):
        print("Error: the folder '" + folder + "' was not found.")
        return False

    if not os.path.isdir(folder):
        print("Error: '" + folder + "' is not a folder.")
        return False

    try:
        names = os.listdir(folder)
    except OSError as error:
        print("Error: could not open the folder:", error)
        return False

    file_count = 0
    for name in names:
        if os.path.isfile(os.path.join(folder, name)):
            file_count = file_count + 1

    if file_count == 0:
        print("There are no files to organise in '" + folder + "'.")
        return False

    return True


# Function 4: Move the files

def organise_files(input_path, output_path):
    moved = {}   # folder name -> number of files moved into it

    for file_name in sorted(os.listdir(input_path)):
        source = os.path.join(input_path, file_name)
        if not os.path.isfile(source):
            continue

        folder_name = get_extension(file_name)
        destination_folder = os.path.join(output_path, folder_name)
        os.makedirs(destination_folder, exist_ok=True)

        new_name = get_free_name(destination_folder, file_name)
        destination = os.path.join(destination_folder, new_name)

        if os.path.abspath(source) == os.path.abspath(destination):
            continue

        try:
            shutil.move(source, destination)
            moved[folder_name] = moved.get(folder_name, 0) + 1
            print("Moved:", file_name, "->", folder_name + "/" + new_name)
        except OSError as error:
            print("Could not move", file_name, "-", error)

    return moved


# Function 5: Show a summary

def print_summary(moved):
    print("\n--- Summary ---")
    total = 0
    for folder_name in moved:
        print(folder_name + ":", moved[folder_name], "file(s)")
        total = total + moved[folder_name]
    print("Total files organised:", total)


# Main

def main():
    print("File Organiser")
    folder = input("Enter the folder to organise (press Enter for data/input): ").strip()

    if folder == "":
        folder = INPUT_PATH

    if check_folder(folder):
        moved = organise_files(folder, OUTPUT_PATH)
        print_summary(moved)
    else:
        print("Nothing was changed.")


main()

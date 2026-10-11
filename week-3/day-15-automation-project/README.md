# Day 15 - Python Automation Project: File Organiser

## Project description

The File Organiser is a Python program that scans a folder and moves each file into a subfolder named after its file extension. For example, `report.pdf` goes into `PDF/`, and `notes.txt` goes into `TXT/`. Files with no extension go into a folder called `No Extension`. This saves time compared with sorting messy folders by hand.

## Plan

I planned the program before writing the code, using Input -> Process -> Output -> Edge Cases.

**Input**
- A folder path typed by the user. If the user presses Enter, the default folder `data/input` is used.

**Process**
1. Check that the folder exists, is a folder, and contains at least one file.
2. Go through the files in the folder, in alphabetical order.
3. Work out each file's extension and the matching destination folder.
4. Create the destination folder if it does not exist yet.
5. Move the file, and keep count of how many files go into each folder.

**Output**
- A "Moved" message for each file, then a summary of how many files went into each folder, and the total.
- The organised files inside `data/output/`.

**Edge cases**
1. The folder does not exist, or the path is not a folder.
2. The folder is empty, so there is nothing to organise.
3. A file has no extension.
4. A file with the same name already exists in the destination folder (it must not be overwritten).
5. Empty input from the user (the default folder is used).

## Requirements

- Python 3
- Only the standard library modules `os` and `shutil`, so there is nothing to install with `pip`.

## Project structure

```
day-15-automation-project/
├── main.py
├── README.md
└── data/
    ├── input/      # test files to organise
    └── output/     # created by the program
```

The test folder `data/input/` has 8 files with different extensions: `report.pdf`, `notes.txt`, `todo.txt`, `photo.jpg`, `scores.csv`, `script.py`, `song.mp3`, and `LICENSE` (no extension). They are small placeholder files, not real documents.

## How to run

1. Open a terminal (it can be in any folder, because the program finds its own `data` folder).
2. Run:
   ```
   python week-3/day-15-automation-project/main.py
   ```
   (or run `python main.py` from inside the `day-15-automation-project` folder).
3. When asked for a folder, press Enter to use `data/input`, or type another folder path.

The program moves the files, so `data/input/` will be empty after a successful run. To run it again from scratch, delete the `data/output` folder and copy the test files back into `data/input/`.

## Example output

```
File Organiser
Enter the folder to organise (press Enter for data/input): 
Moved: LICENSE -> No Extension/LICENSE
Moved: notes.txt -> TXT/notes.txt
Moved: photo.jpg -> JPG/photo.jpg
Moved: report.pdf -> PDF/report.pdf
Moved: scores.csv -> CSV/scores.csv
Moved: script.py -> PY/script.py
Moved: song.mp3 -> MP3/song.mp3
Moved: todo.txt -> TXT/todo.txt

--- Summary ---
No Extension: 1 file(s)
TXT: 2 file(s)
JPG: 1 file(s)
PDF: 1 file(s)
CSV: 1 file(s)
PY: 1 file(s)
MP3: 1 file(s)
Total files organised: 8
```

Folders created in `data/output/`:

```
CSV/   JPG/   MP3/   No Extension/   PDF/   PY/   TXT/
```

## How the code is organised

| Function | What it does |
|---|---|
| `get_extension(file_name)` | Returns the folder name for a file, such as `PDF`, or `No Extension` |
| `get_free_name(folder, file_name)` | Returns a name that is not already used, such as `report_1.pdf` |
| `check_folder(folder)` | Checks the folder exists, is a folder, and has files in it |
| `organise_files(input_path, output_path)` | Moves the files and counts them |
| `print_summary(moved)` | Prints how many files went into each folder |

## Edge cases handled

| Edge case | What the program does |
|---|---|
| Folder does not exist | Prints an error message and changes nothing |
| Path is a file, not a folder | Prints an error message and changes nothing |
| Folder is empty | Prints "There are no files to organise" and changes nothing |
| File has no extension | Moves it into the `No Extension` folder |
| Same file name already in the destination | Renames the new file (`report_1.pdf`) instead of overwriting |
| User presses Enter without typing a path | Uses the default folder `data/input/` |
| A file cannot be moved (for example, permission problems) | Prints a message and continues with the other files, using `try` / `except` |

## Testing

I ran the program on my computer with normal input and with edge cases. Here is what I observed.

| Test | What I did | Result I observed |
|---|---|---|
| Normal run | Pressed Enter with the 8 test files in `data/input/` | All 8 files were moved. The summary showed 7 folders and "Total files organised: 8" |
| File with no extension | `LICENSE` was one of the 8 test files | It was moved to `No Extension/LICENSE` |
| Empty folder | Pressed Enter when `data/input/` had no files | "There are no files to organise in ..." followed by "Nothing was changed." |
| Missing folder | Typed `data/nope` | "Error: the folder 'data/nope' was not found." followed by "Nothing was changed." |
| Single file | Put only `report.pdf` in `data/input/` and pressed Enter | "Moved: report.pdf -> PDF/report.pdf" and "Total files organised: 1" |

The program did not crash in any of these cases.

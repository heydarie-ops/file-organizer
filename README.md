# File Organizer

A Python CLI tool that automatically organizes files in a folder based on their extension (images, documents, videos, etc.).

## Features

- Automatically sorts files into categorized folders (Images, Documents, Excel, Videos, etc.)
- Dry-run mode to preview changes before actually moving files
- Logs every file movement with timestamp to `log.txt`
- Cross-platform (works on Windows, macOS, and Linux)

## Usage

Run the script from the command line, passing the folder path you want to organize:
To preview what the script would do without actually moving any files, use the `--dry-run` 

## Requirements

- Python 3.x (no external libraries needed, uses only the standard library)

## How it works

The script reads all files in the given folder, checks each file's extension, and moves it into a matching 
subfolder (e.g., `.jpg` → `Images`, `.pdf` → `Documents`). Every move is logged with a timestamp in `log.txt` for tracking purposes.

# Chrome Download Automation

A simple Python tool to automatically manage Chrome downloads.  

This script monitors your Chrome downloads folder, copies the latest 2 files to a designated folder, and renames them automatically. It’s designed for workflows like managing resumes and cover letters efficiently.

---

## Features

- Copies original files to a separate folder.
- Renames files to fixed names (`resume` and `cover_letter`) while keeping extensions.
- Works silently in the background.
- Easy to convert to a standalone `.exe` for use without Python.

---

## Setup

1. **Clone the repository** or download the code:

```bash
git clone https://github.com/themalikfahid/chrome-download-automation.git
```

Install Python 3.11+ (if not installed).
Make sure Python is added to your system PATH.

Install required packages:
```bash
pip install requests
```
Configure paths in code.py (or your script):
```bash
CHROME_DOWNLOAD_PATH = r"C:\Users\YourUser\Downloads"
PATH_ORIGINAL = r"D:\processed\original"
PATH_RENAMED = r"D:\processed\renamed"
```
Set fixed names for the two files:
```bash
FIXED_NAME_1 = "resume"
FIXED_NAME_2 = "cover_letter"
Running as Python Script
python code.py
```
The script will continuously monitor your Chrome downloads folder.

-- Once 2 new files are detected, they will be copied and renamed automatically.

-- Building an EXE

## To run the tool without Python:

Install PyInstaller:
```bash
pip install pyinstaller
```
## Build the EXE:
```bash
pyinstaller --onefile --noconsole code.py
```
Your EXE will appear in the dist folder:
```bash
dist\code.exe
```
Run the EXE directly, or add a shortcut to Windows Startup for automatic background execution.


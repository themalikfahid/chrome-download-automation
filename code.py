import os
import time
import shutil

# ===== CONFIG =====
CHROME_DOWNLOAD_PATH = r"C:\Users\YourUser\Downloads"
PATH_ORIGINAL = r"D:\processed\original"
PATH_RENAMED = r"D:\processed\renamed"

FIXED_NAME_1 = "resume"
FIXED_NAME_2 = "cover_letter"

CHECK_INTERVAL = 3

os.makedirs(PATH_ORIGINAL, exist_ok=True)
os.makedirs(PATH_RENAMED, exist_ok=True)

processed_files = []

def get_new_completed_files():
    files = []
    for f in os.listdir(CHROME_DOWNLOAD_PATH):
        full_path = os.path.join(CHROME_DOWNLOAD_PATH, f)

        if (
            os.path.isfile(full_path)
            and not f.endswith(".crdownload")
            and full_path not in processed_files
        ):
            files.append(full_path)

    files.sort(key=lambda x: os.path.getmtime(x))
    return files

while True:
    new_files = get_new_completed_files()

    if len(new_files) >= 2:
        file1 = new_files[0]
        file2 = new_files[1]

        for src_path, fixed_name in zip(
            [file1, file2],
            [FIXED_NAME_1, FIXED_NAME_2]
        ):
            filename = os.path.basename(src_path)
            _, ext = os.path.splitext(filename)

            shutil.copy2(src_path, os.path.join(PATH_ORIGINAL, filename))
            shutil.copy2(
                src_path,
                os.path.join(PATH_RENAMED, fixed_name + ext)
            )

            processed_files.append(src_path)

    time.sleep(CHECK_INTERVAL)
# SyncFil

**SyncFil** is a Python script that synchronizes movie files between two network drives. It checks the source directory for missing files in the target directory and copies them over, ensuring both directories have the same files. This tool supports running in a **dry-run mode** to simulate the synchronization process without making any changes.

## Features

- Sync files from a source network drive to a target network drive.
- **Dry-run mode** to simulate the process without actually copying files.
- Copies only the files missing in the target directory.
- Can handle large directory structures by comparing files recursively.

## Requirements

- **Python 3.x** installed on your system.
- **shutil** and **argparse** libraries (both come pre-installed with Python).
- Access to the source and target network directories.

## Installation

1. Clone the repository or download the `sync_files.py` script.

   ```bash
   git clone https://github.com/yourusername/syncfil.git
   cd syncfil

# SyncFil

**SyncFil** is a Python script that synchronizes movie files between two network drives. It checks the source directory for missing files in the target directory and copies them over, ensuring both directories have the same files. This tool supports running in a **dry-run mode** to simulate the synchronization process without making any changes.

## Features

- Sync files from a source network drive to a target network drive.
- **Dry-run mode** to simulate the process without actually copying files.
- Copies only the files missing in the target directory.
- Can handle large directory structures by comparing files recursively.

## Requirements

- **Python 3.x** installed on your system.
- **shutil** and **argparse** libraries (both come pre-installed with Python).
- Access to the source and target network directories.

## Installation

1. Clone the repository or download the `sync_files.py` script.

   ```bash
   git clone https://github.com/yourusername/syncfil.git
   cd syncfil

2. Ensure you have Python 3.x installed.
You can verify this by running:

   ```bash
   python --version

3. (Optional)  If you're converting the script into an .exe (see Building an Executable below), you’ll need PyInstaller installed:

   ```bash
   pip install pyinstaller

Usage
Sync Files (with Dry-Run Option)
Run the script to synchronize files. You must provide the source and target paths.

Dry-run (simulate):

   ```bash
   python sync_files.py "\\sklad.local\\movies" "\\raspberrypi.local\\Movies" --dry-run

Actual Sync (copy files):

   ```bash
   python sync_files.py "\\sklad.local\\movies" "\\raspberrypi.local\\Movies"

Command-Line Options
source: Path to the source directory (e.g., \\sklad.local\movies).
target: Path to the target directory (e.g., \\raspberrypi.local\Movies).
--dry-run: Simulate the file copy process without actually copying any files.
-h or --help: Display help information.
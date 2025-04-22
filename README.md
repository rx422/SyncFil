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

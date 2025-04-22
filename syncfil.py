#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# sync_files.py - Syncs files from one network drive to another
#
# Copyright (C) 2025 <rx422>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import os
import shutil
import argparse

def get_all_files_with_relative_paths(root_path):
    files = {}
    for dirpath, _, filenames in os.walk(root_path):
        for filename in filenames:
            abs_path = os.path.join(dirpath, filename)
            rel_path = os.path.relpath(abs_path, root_path)
            files[rel_path.lower()] = abs_path
    return files

def copy_missing_files(source_root, target_root, source_files, target_files, dry_run=False):
    copied = 0
    for rel_path, source_abs in source_files.items():
        if rel_path not in target_files:
            target_abs = os.path.join(target_root, rel_path)
            print(f"{'[DRY-RUN] ' if dry_run else ''}Copying: {rel_path}")
            if not dry_run:
                os.makedirs(os.path.dirname(target_abs), exist_ok=True)
                shutil.copy2(source_abs, target_abs)
            copied += 1
    return copied

def sync_files(source_path, target_path, dry_run=False):
    print(f"Scanning source: {source_path}...")
    source_files = get_all_files_with_relative_paths(source_path)

    print(f"Scanning target: {target_path}...")
    target_files = get_all_files_with_relative_paths(target_path)

    print(f"\nFiles only in source: {len(set(source_files) - set(target_files))}")
    print(f"Files only in target: {len(set(target_files) - set(source_files))}")
    print(f"Common files: {len(set(source_files) & set(target_files))}")

    copied_count = copy_missing_files(source_path, target_path, source_files, target_files, dry_run)
    print(f"\n{'[DRY-RUN] ' if dry_run else ''}Copied {copied_count} file(s).")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Sync movie files from one network drive (source) to another (target), copying missing files."
    )
    parser.add_argument(
        "source",
        help="Path to the source directory (e.g., '\\\\sklad.local\\Movies')"
    )
    parser.add_argument(
        "target",
        help="Path to the target directory (e.g., '\\\\raspberrypi.local\\Movies')"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate the file copy process without actually copying any files."
    )
    args = parser.parse_args()

    sync_files(args.source, args.target, dry_run=args.dry_run)

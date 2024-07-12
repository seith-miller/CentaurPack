# pack.py

import os
from .utils import write_file_marker, write_dir_marker
from .ignore import IgnoreManager

def pack_directory(directory, output_file, verbose=False):
    text_extensions = ['.py', '.js', '.html', '.css', '.md', '.txt', '.json', '.yml', '.yaml']
    max_file_size = 1024 * 1024  # 1 MB limit
    ignore_manager = IgnoreManager()

    with open(output_file, 'w', encoding='utf-8') as f:
        if verbose:
            print(f"Packing directory: {directory}")
        f.write("<<CENTAURPACK_VERSION:1.0>>\n")
        for root, dirs, files in os.walk(directory):
            rel_path = os.path.relpath(root, directory)
            if rel_path != '.' and not ignore_manager.is_ignored(rel_path):
                write_dir_marker(f, rel_path)
                if verbose:
                    print(f"Adding directory: {rel_path}")
            for file in files:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, directory)
                _, ext = os.path.splitext(file)
                if ignore_manager.is_ignored(rel_path):
                    if verbose:
                        print(f"Skipping ignored file: {rel_path}")
                    continue
                if ext.lower() not in text_extensions:
                    if verbose:
                        print(f"Skipping non-text file: {rel_path}")
                    continue
                if os.path.getsize(file_path) > max_file_size:
                    if verbose:
                        print(f"Skipping large file: {rel_path}")
                    continue
                write_file_marker(f, rel_path)
                if verbose:
                    print(f"Adding file: {rel_path}")
                try:
                    with open(file_path, 'r', encoding='utf-8') as source_file:
                        f.write(source_file.read())
                except UnicodeDecodeError:
                    if verbose:
                        print(f"Skipping file due to encoding issues: {rel_path}")
                    continue
                f.write("\n<<ENDFILE>>\n")
    if verbose:
        print(f"Packing complete. Output file: {output_file}")

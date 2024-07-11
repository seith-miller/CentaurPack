import os
from utils import write_file_marker, write_dir_marker

def pack_directory(directory, output_file):
    with open(output_file, 'w') as f:
        f.write("<<FLATPACK_VERSION:1.0>>\n")
        for root, dirs, files in os.walk(directory):
            rel_path = os.path.relpath(root, directory)
            if rel_path != '.':  # Don't write a marker for the root directory
                write_dir_marker(f, rel_path)
            for file in files:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, directory)
                write_file_marker(f, rel_path)
                with open(file_path, 'r') as source_file:
                    f.write(source_file.read())
                f.write("\n<<ENDFILE>>\n")
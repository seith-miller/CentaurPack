import os
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def unpack_file(packed_file, output_dir, verbose=False):
    with open(packed_file, "r") as f:
        first_line = f.readline().strip()
        if not first_line.startswith("<<CENTAURPACK_VERSION:"):
            raise ValueError("Invalid CentaurPack file: Missing version header")

        current_file = None
        for line in f:
            original_line = line
            line = line.strip()
            if line.startswith("<<FILE:"):
                if current_file:
                    current_file.close()
                file_path = line[7:-2]  # Remove "<<FILE:" and ">>"
                full_path = os.path.join(output_dir, file_path)
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                current_file = open(full_path, "w")
            elif line.startswith("<<DIR:"):
                dir_path = line[6:-2]  # Remove "<<DIR:" and ">>"
                full_dir_path = os.path.join(output_dir, dir_path)
                os.makedirs(full_dir_path, exist_ok=True)
            elif line == "<<ENDFILE>>":
                if current_file:
                    current_file.close()
                    current_file = None
            elif current_file:
                current_file.write(original_line)
            else:
                logger.warning(f"Unexpected line: {line}")

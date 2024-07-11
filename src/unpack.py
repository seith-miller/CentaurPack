import os
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def unpack_file(packed_file, output_dir):
    try:
        with open(packed_file, 'r') as f:
            line = f.readline().strip()
            if not line.startswith("<<FLATPACK_VERSION:"):
                raise ValueError("Invalid flatpack file")
            
            current_file = None
            for line in f:
                line = line.rstrip('\n')
                if line.startswith("<<FILE:"):
                    if current_file:
                        current_file.close()
                    file_path = line[7:-2]  # Remove "<<FILE:" and ">>"
                    full_path = os.path.join(output_dir, file_path)
                    logger.debug(f"Creating file: {full_path}")
                    os.makedirs(os.path.dirname(full_path), exist_ok=True)
                    current_file = open(full_path, 'w')
                elif line.startswith("<<DIR:"):
                    dir_path = line[6:-2]  # Remove "<<DIR:" and ">>"
                    if dir_path:  # Only create directory if path is not empty
                        full_dir_path = os.path.join(output_dir, dir_path)
                        logger.debug(f"Creating directory: {full_dir_path}")
                        os.makedirs(full_dir_path, exist_ok=True)
                elif line == "<<ENDFILE>>":
                    if current_file:
                        logger.debug(f"Closing file: {current_file.name}")
                        current_file.flush()
                        current_file.close()
                        current_file = None
                elif current_file:
                    logger.debug(f"Writing to file {current_file.name}: {line}")
                    current_file.write(line + '\n')
                else:
                    logger.warning(f"Unexpected line: {line}")

            if current_file:
                current_file.flush()
                current_file.close()
    except IOError as e:
        logger.error(f"IO Error occurred: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")
        raise
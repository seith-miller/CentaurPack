def write_file_marker(file, path):
    file.write(f"<<FILE:{path}>>\n")


def write_dir_marker(file, path):
    file.write(f"<<DIR:{path}>>\n")


def read_file_marker(line):
    return line.strip()[7:-1]


def read_dir_marker(line):
    return line.strip()[6:-1]

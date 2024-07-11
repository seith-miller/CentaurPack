# Flatpack

Flatpack is a command-line tool for packing and unpacking directory structures into single files. It's designed to make sharing code and project structures easier.

## Features
- Pack entire directory structures into a single file
- Unpack Flatpack files back into their original directory structure
- Preserve file contents and directory hierarchy
- Simple command-line interface
- Support for .flatpackignore to exclude files and directories

## Installation
### Prerequisites
- Python 3.6 or higher

### Setup
1. Clone the repository:
git clone https://github.com/yourusername/flatpack.git
cd flatpack
Copy2. Create a virtual environment:
python3 -m venv venv
Copy3. Activate the virtual environment:
- On Unix or MacOS:
  ```
  source venv/bin/activate
  ```
- On Windows:
  ```
  venv\Scripts\activate
  ```
4. Install the project in editable mode:
pip install -e .
Copy
## Usage
After installation, you can use Flatpack with the following commands:

### Packing a directory
flatpack pack <directory> <output_file>
CopyThis will pack the contents of `<directory>` into `<output_file>`.

### Unpacking a file
flatpack unpack <input_file> <output_directory>
CopyThis will unpack the contents of `<input_file>` into `<output_directory>`.

### Using .flatpackignore

Flatpack supports a `.flatpackignore` file to exclude certain files or directories from being packed. This file works similarly to `.gitignore`.

To use this feature:

1. Create a file named `.flatpackignore` in the root directory of your project.
2. Add patterns for files or directories you want to ignore, one per line.

Example `.flatpackignore`:
Ignore all .log files
*.log
Ignore the entire 'build' directory
build/
Ignore a specific file
secret_key.txt
Copy
You can also specify a custom ignore file using the `--ignore-file` option:
flatpack pack <directory> <output_file> --ignore-file my_custom_ignore.txt
Copy
## Development
### Running Tests
To run all tests:
python run_tests.py
Copy
To run specific test files:
python -m unittest tests.test_pack
python -m unittest tests.test_unpack
Copy
### Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thanks to all contributors who have helped shape Flatpack
- Inspired by the need for simple, efficient code sharing
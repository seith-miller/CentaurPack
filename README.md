# CentaurPack

CentaurPack is a command-line tool for packing and unpacking directory structures into single files. It's designed to make sharing code and project structures easier.

## Features
- Pack entire directory structures into a single file
- Unpack CentaurPack files back into their original directory structure
- Preserve file contents and directory hierarchy
- Simple command-line interface

## Installation
### Prerequisites
- Python 3.6 or higher

### Setup
1. Clone the repository:
git clone https://github.com/centaurinc/centaurpack.git
cd centaurpack
2. Create a virtual environment:
python3 -m venv venv
3. Activate the virtual environment:
- On Unix or MacOS:
source venv/bin/activate
- On Windows:
venv\Scripts\activate
4. Install the project in editable mode:
pip install -e .

## Usage
After installation, you can use CentaurPack with the following commands:

### Packing a directory
centaurpack pack <directory> <output_file>
This will pack the contents of `<directory>` into `<output_file>`.

### Unpacking a file
centaurpack unpack <input_file> <output_directory>
This will unpack the contents of `<input_file>` into `<output_directory>`.

## Development
### Running Tests
To run all tests:
python run_tests.py

To run specific test files:
python -m unittest tests.test_pack
python -m unittest tests.test_unpack

### Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thanks to all contributors who have helped shape CentaurPack
- Inspired by the need for simple, efficient code sharing
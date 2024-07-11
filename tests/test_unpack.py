import os
import tempfile
import unittest
from src.unpack import unpack_file

class TestUnpack(unittest.TestCase):
    def setUp(self):
        self.test_file = tempfile.mktemp()
        self.output_dir = tempfile.mkdtemp()

        # Create a test flatpack file
        with open(self.test_file, "w") as f:
            f.write("<<FLATPACK_VERSION:1.0>>\n")
            f.write("<<DIR:subdir>>\n")
            f.write("<<FILE:file1.txt>>\n")
            f.write("Content of file1\n")
            f.write("<<ENDFILE>>\n")
            f.write("<<FILE:subdir/file2.txt>>\n")
            f.write("Content of file2\n")
            f.write("<<ENDFILE>>\n")

    def tearDown(self):
        os.remove(self.test_file)
        for root, dirs, files in os.walk(self.output_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.output_dir)

    def test_unpack_file(self):
        unpack_file(self.test_file, self.output_dir)
        
        print(f"\nOutput directory contents:")
        for root, dirs, files in os.walk(self.output_dir):
            level = root.replace(self.output_dir, '').count(os.sep)
            indent = ' ' * 4 * level
            print(f"{indent}{os.path.basename(root)}/")
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                print(f"{subindent}{f}")
        
        expected_file1 = os.path.join(self.output_dir, "file1.txt")
        expected_file2 = os.path.join(self.output_dir, "subdir", "file2.txt")
        
        print(f"\nChecking directory: {os.path.join(self.output_dir, 'subdir')}")
        print(f"Directory exists: {os.path.isdir(os.path.join(self.output_dir, 'subdir'))}")
        
        print(f"\nChecking file: {expected_file1}")
        print(f"File exists: {os.path.isfile(expected_file1)}")
        if os.path.isfile(expected_file1):
            with open(expected_file1, "r") as f:
                print(f"File contents: {f.read().strip()}")
        
        print(f"\nChecking file: {expected_file2}")
        print(f"File exists: {os.path.isfile(expected_file2)}")
        if os.path.isfile(expected_file2):
            with open(expected_file2, "r") as f:
                print(f"File contents: {f.read().strip()}")
        
        self.assertTrue(os.path.isdir(os.path.join(self.output_dir, "subdir")), "Subdirectory was not created")
        self.assertTrue(os.path.isfile(expected_file1), f"File not created: {expected_file1}")
        self.assertTrue(os.path.isfile(expected_file2), f"File not created: {expected_file2}")

        if os.path.isfile(expected_file1):
            with open(expected_file1, "r") as f:
                self.assertEqual(f.read().strip(), "Content of file1", "Content of file1 is incorrect")
        
        if os.path.isfile(expected_file2):
            with open(expected_file2, "r") as f:
                self.assertEqual(f.read().strip(), "Content of file2", "Content of file2 is incorrect")

    def test_unpack_invalid_file(self):
        with open(self.test_file, "w") as f:
            f.write("This is not a valid flatpack file")
        
        with self.assertRaises(ValueError):
            unpack_file(self.test_file, self.output_dir)

if __name__ == '__main__':
    unittest.main()
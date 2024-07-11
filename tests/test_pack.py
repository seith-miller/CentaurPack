import os
import tempfile
import unittest
from src.pack import pack_directory

class TestPack(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.output_file = tempfile.mktemp()

        # Create a test directory structure
        os.makedirs(os.path.join(self.test_dir, "subdir"))
        with open(os.path.join(self.test_dir, "file1.txt"), "w") as f:
            f.write("Content of file1")
        with open(os.path.join(self.test_dir, "subdir", "file2.txt"), "w") as f:
            f.write("Content of file2")

    def tearDown(self):
        os.remove(self.output_file)
        for root, dirs, files in os.walk(self.test_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.test_dir)

    def test_pack_directory(self):
        pack_directory(self.test_dir, self.output_file)
        
        with open(self.output_file, "r") as f:
            content = f.read()
        
        self.assertIn("<<FLATPACK_VERSION:1.0>>", content)
        self.assertIn("<<DIR:subdir>>", content)
        self.assertIn("<<FILE:file1.txt>>", content)
        self.assertIn("Content of file1", content)
        self.assertIn("<<FILE:subdir/file2.txt>>", content)
        self.assertIn("Content of file2", content)

    def test_pack_empty_directory(self):
        empty_dir = tempfile.mkdtemp()
        pack_directory(empty_dir, self.output_file)
        
        with open(self.output_file, "r") as f:
            content = f.read()
        
        self.assertIn("<<FLATPACK_VERSION:1.0>>", content)
        self.assertNotIn("<<FILE:", content)
        self.assertNotIn("<<DIR:", content)

        os.rmdir(empty_dir)

if __name__ == '__main__':
    unittest.main()
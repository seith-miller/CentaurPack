import unittest
from flatpack.ignore import IgnoreManager
import tempfile
import os

class TestIgnoreManager(unittest.TestCase):
    def setUp(self):
        self.ignore_file = tempfile.mktemp()
        with open(self.ignore_file, 'w') as f:
            f.write("*.pyc\n")
            f.write("__pycache__/\n")
            f.write("*.log\n")
            f.write("venv/\n")

        self.ignore_manager = IgnoreManager(ignore_file=self.ignore_file)

    def tearDown(self):
        if os.path.exists(self.ignore_file):
            os.remove(self.ignore_file)

    def test_ignore_patterns(self):
        self.assertTrue(self.ignore_manager.is_ignored("file.pyc"))
        self.assertTrue(self.ignore_manager.is_ignored("__pycache__/file.py"))
        self.assertTrue(self.ignore_manager.is_ignored("logs/error.log"))
        self.assertTrue(self.ignore_manager.is_ignored("venv/bin/activate"))
        self.assertFalse(self.ignore_manager.is_ignored("file.py"))
        self.assertFalse(self.ignore_manager.is_ignored("src/main.py"))

if __name__ == '__main__':
    unittest.main()

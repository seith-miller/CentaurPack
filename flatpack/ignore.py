# ignore.py

import fnmatch
import os

class IgnoreManager:
    def __init__(self, ignore_file='.flatpackignore'):
        self.ignore_file = ignore_file
        self.patterns = []
        self.load_patterns()

    def load_patterns(self):
        if os.path.exists(self.ignore_file):
            with open(self.ignore_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        self.patterns.append(line)

    def is_ignored(self, path):
        for pattern in self.patterns:
            # Check for exact pattern match
            if fnmatch.fnmatch(path, pattern):
                print(f"Path '{path}' matches pattern '{pattern}'")
                return True
            # Check for directory pattern match
            if pattern.endswith('/') and path.startswith(pattern[:-1]):
                print(f"Path '{path}' matches directory pattern '{pattern}'")
                return True
            else:
                print(f"Path '{path}' does not match pattern '{pattern}'")
        return False

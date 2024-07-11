import unittest
import os
import sys

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

def run_tests():
    # Discover and run tests
    loader = unittest.TestLoader()
    start_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tests'))
    suite = loader.discover(start_dir, pattern='test_*.py')

    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    return result.wasSuccessful()

if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
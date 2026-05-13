# test_mlserver.py
"""
Tests for MLServer module.
"""

import unittest
from mlserver import MLServer

class TestMLServer(unittest.TestCase):
    """Test cases for MLServer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MLServer()
        self.assertIsInstance(instance, MLServer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MLServer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

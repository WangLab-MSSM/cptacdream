import unittest

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import cptacdream as _


class TestCPTACDream(unittest.TestCase):
    # hello world
    def test_hello_world_is_str(self):
        self.assertIsInstance(_.hello_world(), str)
        self.assertIsInstance(_.joke(), int)


if __name__ == '__main__':
    unittest.main()

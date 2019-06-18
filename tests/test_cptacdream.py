import unittest


class TestCptacDream(unittest.TestCase):
    # hello world
    def test_hello_world_is_str(self):
        self.assertIsInstance('hello world', str)


if __name__ == '__main__':
    unittest.main()

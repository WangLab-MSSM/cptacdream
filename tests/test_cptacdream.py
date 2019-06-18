import unittest

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import docker

import cptacdream as _


class TestCPTACDream(unittest.TestCase):
    # sanity check
    def test_hello_world_is_str(self):
        self.assertIsInstance(_.hello_world(), str)

    def test_docker_client_returns_client_obj(self):
        self.assertIsInstance(_.docker_client(), docker.client.DockerClient)


if __name__ == '__main__':
    unittest.main()

import unittest
import random

from Lab10 import *


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.root = Node(5)
        self.root.left = Node(3)
        self.root.right = Node(7)
        self.root.left.left = Node(2)
        self.root.left.right = Node(4)
        self.root.right.left = Node(6)
        self.root.right.right = Node(8)

    def test_add_node(self):
        add_node(self.root, 1)
        self.assertIsNotNone(self.root.left.left.left)

    def test_find_node(self):
        found_node = find_node(self.root, 4)
        self.assertIsNotNone(found_node)
        self.assertEqual(found_node.value, 4)


    def test_find_min(self):
        min_node = find_min(self.root.right)
        self.assertEqual(min_node.value, 6)

    def test_swap_children(self):
        swap_children(self.root)
        self.assertEqual(self.root.left.value, 7)
        self.assertEqual(self.root.right.value, 3)


if __name__ == '__main__':
    unittest.main()

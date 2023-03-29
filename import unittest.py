import unittest
from Lab10 import Node, find_node

class TestBinaryTree(unittest.TestCase):

    def test_find_node(self):
        root = Node(5)
        node2 = Node(2)
        node7 = Node(7)
        node1 = Node(1)
        node3 = Node(3)
        node6 = Node(6)
        node8 = Node(8)

        root.left = node2
        root.right = node7
        node2.left = node1
        node2.right = node3
        node7.left = node6
        node7.right = node8

        self.assertEqual(find_node(root, 5), root)
        self.assertEqual(find_node(root, 2), node2)
        self.assertEqual(find_node(root, 7), node7)
        self.assertEqual(find_node(root, 1), node1)
        self.assertEqual(find_node(root, 3), node3)
        self.assertEqual(find_node(root, 6), node6)
        self.assertEqual(find_node(root, 8), node8)
        
if __name__ == '__main__':
    unittest.main()

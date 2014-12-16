import unittest
from trii import DecisionTree


class TriiTests(unittest.TestCase):
    def test_tree_works(self):
        tree = DecisionTree(lambda x: x % 2)
        tree.add_child(0, 'even')
        tree.add_child(1, 'odd')

        self.assertEqual(tree.decide({'x': 5}), 'odd')
        self.assertEqual(tree.decide({'x': 8}), 'even')

    def test_subtree(self):
        tree = DecisionTree((lambda x: x % 2))
        tree.add_child(0, 'even')
        subtree = DecisionTree(lambda x: x % 3)
        tree.add_child(1, subtree)
        subtree.add_child(0, 'divisible by 3')
        subtree.add_child(lambda x: x != 0, 'not divisible by 3')

        self.assertEqual(tree.decide({'x': 3}), 'divisible by 3')
        self.assertEqual(tree.decide({'x': 5}), 'not divisible by 3')
        self.assertEqual(tree.decide({'x': 2}), 'even')


if __name__ == '__main__':
    unittest.main()

import unittest
from trii import DecisionTree


class TriiTests(unittest.TestCase):
    def test_tree_works(self):
        tree = DecisionTree((lambda x: x % 2))
        tree.add_child(0, 'even')
        tree.add_child(1, 'odd')

        result = tree.decide({'x': 5})
        self.assertEqual(result, 'odd')


if __name__ == '__main__':
    unittest.main()

import unittest

from leafnode import LeafNode 

class TestLeafNode(unittest.TestCase):

    def test_eq(self):
        node = LeafNode("tag", "value", "props")
        node2 = LeafNode("tag", "value", "props")
        self.assertEqual(node, node2)

    def test_one_not_eq(self):
        node = LeafNode("tag", "value", "props")
        node2 = LeafNode("not_tag", "value", "props")
        self.assertNotEqual(node, node2)

    def test_all_not_eq(self):
        node = LeafNode("tag", "value", "props")
        node2 = LeafNode("not_tag", "not_value", "not_props")
        self.assertNotEqual(node, node2)

    def test_print(self):
        node = LeafNode("tag", "value", "props")
        print(node)

    def test_to_html(self):
        node = LeafNode("tag", "value", "props")
        print(node.to_html())

if __name__ == "__main__":
    unittest.main()

import unittest

from htmlnode import HTMLNode 

class TestHTMLNode(unittest.TestCase):

    def test_empty_eq(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_eq(self):
        node = HTMLNode("tag", "value", "children", "props")
        node2 = HTMLNode("tag", "value", "children", "props")
        self.assertEqual(node, node2)

    def test_one_not_eq(self):
        node = HTMLNode("tag", "value", "children", "props")
        node2 = HTMLNode("not_tag", "value", "children", "props")
        self.assertNotEqual(node, node2)

    def test_all_not_eq(self):
        node = HTMLNode("tag", "value", "children", "props")
        node2 = HTMLNode("not_tag", "not_value", "not_children", "not_props")
        self.assertNotEqual(node, node2)

    def test_print(self):
        node = HTMLNode("tag", "value", "children", "props")
        print(node)

if __name__ == "__main__":
    unittest.main()

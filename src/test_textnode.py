import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a test node", TextType.BOLD)
        node2 = TextNode("This is a test node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_link(self):
        node = TextNode("This is a test node", TextType.LINK, "www.google.com")
        node2 = TextNode("This is a test node", TextType.LINK, "www.google.com")
        self.assertEqual(node, node2)

    def test_not_eq_link(self):
        node = TextNode("This is a test node", TextType.LINK, "www.google.com")
        node2 = TextNode("This is a test node", TextType.LINK, "www.bing.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_types(self):
        node = TextNode("This is a test node", TextType.IMAGE, "www.image.com")
        node2 = TextNode("This is a test node", TextType.LINK, "www.image.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a test node!", TextType.BOLD, "www.image.com")
        node2 = TextNode("This is a test node.", TextType.BOLD, "www.image.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()

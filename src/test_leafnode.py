import unittest

from leafnode import *


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a  href="https://www.google.com">Click me!</a>')

    def test_to_html_exeption(self):
        node = LeafNode("p", value=None)
        self.assertRaises(ValueError, node.to_html)


if __name__ == "__main__":
    unittest.main()
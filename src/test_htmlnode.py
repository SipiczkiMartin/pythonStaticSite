import unittest

from htmlnode import *


class TestHtmlNode(unittest.TestCase):
    def test_props(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(props=props)
        print(node.props_to_html())
    
    def test_no_props(self):
        node = HTMLNode()
        print(node.props_to_html())

    def test_to_html(self):
        node = HTMLNode()
        self.assertRaises(NotImplementedError,node.to_html)




if __name__ == "__main__":
    unittest.main()
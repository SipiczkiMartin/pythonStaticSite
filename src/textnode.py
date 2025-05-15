from enum import Enum
from leafnode import LeafNode
from inlinedeliminer import *

class TextType(Enum):
    TEXT = "Text"
    BOLD = "Bold"
    ITALIC = "Italic"
    CODE = "Code"
    LINK = "Link"
    IMAGE = "Image"

class TextNode:
    def __init__(self,text,text_type,url = None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url
    
    def __eq__(self, value):
        return self.text == value.text and self.text_type == value.text_type and self.url == value.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None,value=text_node.text)
        case TextType.BOLD:
            return LeafNode("b",value=text_node.text)
        case TextType.ITALIC:
            return LeafNode("i",value=text_node.text)
        case TextType.CODE:
            return LeafNode("code",value=text_node.text)
        case TextType.LINK:
            return LeafNode("a",value=text_node.text,props={"href":text_node.url})
        case TextType.IMAGE:
            return LeafNode("img",value="",props={"src":text_node.url,"alt":text_node.text})
        case _:
            raise Exception("Wrong NodeType")

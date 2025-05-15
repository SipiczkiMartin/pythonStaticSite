from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value = None, children = children, props = props)

    def to_html(self):
        if not self.tag:
            raise ValueError("All leaf nodes must have a value")
        
        if not self.children:
            raise ValueError("Children missing from parent")
        
        node_string= f"<{self.tag}>"
        
        for child in self.children:
            node_string += child.to_html()
        
        return f"{node_string}</{self.tag}>"
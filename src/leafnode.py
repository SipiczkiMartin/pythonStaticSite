from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children = None, props = props)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        
        if self.tag == None:
            return self.value
        else:
            if self.props == None:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            else:
                props_string = self.props_to_html()
                return f"<{self.tag} {props_string}>{self.value}</{self.tag}>"
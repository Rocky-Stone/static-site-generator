from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if (self.tag == None):
            raise ValueError("No tag!")
        if (self.children == None):
            raise ValueError("No children!")
        start_html = f"<{self.tag}"
        if (self.props is not None):
            start_html += f"{self.props}>"
        else:
            start_html += ">"
        end_html = f"</{self.tag}>"
        child_html = ""
        for child in self.children:
            child_html += child.to_html()
        return start_html + child_html + end_html

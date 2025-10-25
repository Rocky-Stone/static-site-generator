from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if (self.value == None):
            raise ValueError("No value!")
        if (self.tag == None):
            return self.value
        else:
            start_html = f"<{self.tag}"
            if (self.props is not None):
                start_html += f"{self.props}>"
            else:
                start_html += ">"
            end_html = f"</{self.tag}>"
            return f"{start_html}{self.value}{end_html}"

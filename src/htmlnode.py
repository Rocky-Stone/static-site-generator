

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props  

    def to_html(self):
        raise NotImplementedError("Not implemented, abstract!")

    def props_to_html(self):
        html = ""
        for key, value in props.items():
            html = html + f"{self.key}={self.value} "
        return html.strip()

    def __repr__(self):
        return f"\nnode:\n\ttag: {self.tag}\n\tvalue: {self.value}\n\tchildren: {self.children}\n\tprops: {self.props}"

    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

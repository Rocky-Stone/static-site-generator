from textnode import TextNode
from textnode import TextType
from leafnode import LeafNode

def text_node_to_html_node(text_node):
    text = text_node.text
    tag = None
    props = None

    text_type = text_node.text_type
    match text_type:
        case TextType.PLAIN:
            tag = None
        case TextType.BOLD:
            tag = "b"
        case TextType.ITALIC:
            tag = "i"
        case TextType.CODE:
            tag = "code"
        case TextType.LINK:
            tag = "link"
            props = {"href": text_node.url}
        case TextType.IMAGE:
            tag = "img"
            props = {"src": text_node.url, "alt": text}
        case _:
            raise ValueError("TextNode has incompatable TextType")
    return LeafNode(tag, text, props) 

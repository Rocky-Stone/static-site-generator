#print("hello world")
from textnode import TextNode
from textnode import TextType 

def main():
    text_node = TextNode("This is bold text", TextType.BOLD, None)
    text_node2 = TextNode("This is a image", TextType.IMAGE, "www.pics.com")
    print(text_node)
    print(text_node2)

main()

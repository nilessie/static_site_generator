import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_none(self):
        htmlnode1 = HTMLNode()
        self.assertEqual(htmlnode1.tag, None)
        self.assertEqual(htmlnode1.value, None)
        self.assertEqual(htmlnode1.children, None)
        self.assertEqual(htmlnode1.props, None)
    
    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
            }
        
        htmlnode1 = HTMLNode()
        htmlnode1.props = props
        self.assertEqual(htmlnode1.props_to_html(),  ' href="https://www.google.com" target="_blank"')
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

        node1 = LeafNode("b", "Hello, world!")
        self.assertNotEqual(node1.to_html(), "<p>Hello, world!</p>")



if __name__ == "__main__":
    unittest.main()
import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_create_html_node(self):
        node = HTMLNode("a", None, None, None)
        node2 = HTMLNode(None, "This is a test", None, None)
        node3 = HTMLNode(None, None, [node, node2], None)
        node4 = HTMLNode(None, None, None, {"href": "https://www.google.com"})
        self.assertEqual(repr(node), "HTMLNode('a', None, None, None)")
        self.assertEqual(repr(node2), "HTMLNode(None, 'This is a test', None, None)")
        self.assertEqual(repr(node3), "HTMLNode(None, None, [HTMLNode('a', None, None, None), HTMLNode(None, 'This is a test', None, None)], None)")
        self.assertEqual(repr(node4), "HTMLNode(None, None, None, {'href': 'https://www.google.com'})")

    def test_props_to_html(self):
        node = HTMLNode("a", "This is a test", None, {"href": "https://www.google.com"})
        attributes = node.props_to_html()
        self.assertEqual(attributes, ' href="https://www.google.com"')

    def test_to_html(self):
        node = HTMLNode("a", "This is a test", None, {"href": "https://www.google.com"})
        self.assertRaises(NotImplementedError, node.to_html)

    

if __name__ == "__main__":
    unittest.main()
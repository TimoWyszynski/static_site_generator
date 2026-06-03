import unittest
from generate_page import extract_title

class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        md = """
# This is a h1
"""
        title = extract_title(md)
        self.assertEqual(title, "This is a h1")

if __name__ == "__main__":
    unittest.main()
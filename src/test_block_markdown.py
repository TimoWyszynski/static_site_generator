import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_markdown_block_to_block_type_heading1(self):
        md = "# This is a heading."
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.HEADING, block_type)

    def test_markdown_block_to_block_type_heading2(self):
        md = "## This is a heading."
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.HEADING, block_type)

    def test_markdown_block_to_block_type_heading3(self):
        md = "### This is a heading."
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.HEADING, block_type)

    def test_markdown_block_to_block_type_heading4(self):
        md = "#### This is a heading."
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.HEADING, block_type)

    def test_markdown_block_to_block_type_heading5(self):
        md = "##### This is a heading."
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.HEADING, block_type)

    def test_markdown_block_to_block_type_heading6(self):
        md = "###### This is a heading."
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.HEADING, block_type)

    def test_markdown_block_to_block_code(self):
        md = "```\nThis is code```"
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.CODE, block_type)

    def test_markdown_block_to_block_quote1(self):
        md = ">This is code"
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.QUOTE, block_type)

    def test_markdown_block_to_block_quote2(self):
        md = "> This is code"
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.QUOTE, block_type)

    def test_markdown_block_to_block_quote3(self):
        md = "> This is code\n> This is to"
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.QUOTE, block_type)

    def test_markdown_block_to_block_unordered_list1(self):
        md = "- This is a list"
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.UNORDERED_LIST, block_type)

    def test_markdown_block_to_block_unordered_list2(self):
        md = "- This is a list\n- This is to"
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.UNORDERED_LIST, block_type)

    def test_markdown_block_to_block_ordered_list1(self):
        md = "1. This is a list"
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.ORDERED_LIST, block_type)

    def test_markdown_block_to_block_ordered_list2(self):
        md = "1. This is a list\n2. This is to"
        block_type = block_to_block_type(md)
        self.assertEqual(BlockType.ORDERED_LIST, block_type)


if __name__ == "__main__":
    unittest.main()
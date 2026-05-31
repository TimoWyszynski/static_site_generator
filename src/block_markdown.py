from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(markdown_block: str) -> BlockType:
    if markdown_block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    elif markdown_block.startswith("```\n") and markdown_block.endswith("```"):
        return BlockType.CODE
    elif all(line.startswith(">") for line in markdown_block.split("\n")):
        return BlockType.QUOTE
    elif all(line.startswith("- ") for line in markdown_block.split("\n")):
        return BlockType.UNORDERED_LIST
    elif all(line.startswith(f"{i}. ") for i, line in enumerate(markdown_block.split("\n"), start=1)):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
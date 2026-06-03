from block_markdown import markdown_to_html_node
import os

def extract_title(markdown: str):
    blocks = markdown.split("\n")
    for block in blocks:
        if block.startswith("# "):
            return block.replace("# ", "")
    raise Exception("Could not find h1 header in markdown")

def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as f, open(template_path) as t:
        markdown = f.read()
        template = t.read()

        html_markdown = markdown_to_html_node(markdown).to_html()
        markdown_title = extract_title(markdown)

        template = template.replace("{{ Title }}", markdown_title)
        template = template.replace("{{ Content }}", html_markdown)

        os.makedirs(os.path.dirname(dest_path), exist_ok=True)

        with open(dest_path, "w") as w:
            w.write(template)
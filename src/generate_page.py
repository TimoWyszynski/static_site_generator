from block_markdown import markdown_to_html_node
import os
from pathlib import Path

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

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    contents = os.listdir(dir_path_content)
    for content in contents:
        content_path = os.path.join(dir_path_content, content)
        dest_path = os.path.join(dest_dir_path, content)
        if os.path.isfile(content_path):
            if content_path.endswith(".md"):
                generate_page(content_path, template_path, dest_path.replace(".md",".html"))
            else:
                continue
        else:
            generate_pages_recursive(content_path, template_path, dest_path)
    return
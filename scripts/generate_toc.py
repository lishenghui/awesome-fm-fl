import re


def generate_toc(markdown_content):
    toc = []
    lines = markdown_content.split("\n")
    for line in lines:
        if line.startswith("#"):
            level = len(line) - len(line.lstrip("#"))
            title = line.lstrip("# ")
            # Create a slug for the link
            slug = re.sub(r"[^\w\s-]", "", title).strip().lower()
            slug = re.sub(r"[-\s]+", "-", slug)
            toc.append((level, title, slug))
    return toc


def build_html_toc(toc_items):
    html = '<div class="contents collapsible" depth="3" local="">\n'
    html += '<strong>Table of Contents</strong>\n'
    html += '<ul>\n'
    
    path = [] # stack of levels
    
    for i, (level, title, slug) in enumerate(toc_items):
        
        while path and level <= path[-1]:
            path.pop()
            html += '</ul></details></li>\n'

        # Check if it should have children
        has_children = (i + 1 < len(toc_items)) and (toc_items[i+1][0] > level)

        if has_children:
            # Level 2 is open by default
            open_attr = " open" if level == 2 else ""
            html += f'<li><details{open_attr}><summary><a href="#{slug}">{title}</a></summary><ul>\n'
            path.append(level)
        else:
            html += f'<li><a href="#{slug}">{title}</a></li>\n'

    # Close remaining tags
    html += '</ul></details></li>\n' * len(path)
    
    html += '</ul>\n</div>'
    return html


def main():
    readme_path = "/Users/sheli564/Desktop/awesome-fm-fl/README.md"
    with open(readme_path, "r") as f:
        content = f.read()

    toc_items = generate_toc(content)
    # We only want ## and deeper
    toc_items = [item for item in toc_items if item[0] >= 2]

    html_toc = build_html_toc(toc_items)

    # Replace the old TOC
    new_content = re.sub(
        r'<div class="contents collapsible".*?</div>',
        html_toc,
        content,
        flags=re.DOTALL,
    )

    with open(readme_path, "w") as f:
        f.write(new_content)


if __name__ == "__main__":
    main()

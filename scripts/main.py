import yaml

import types
import os
import re
from entry_table import PaperTable, ResourcePaperTable, convert_entry
import pypandoc

rst_headders = ["#", "*", "^", "'", "*", "+", "#", "_", "`", ":", ".", "!", "<", ">"]


def parse_helper(blocks, config, tags, level=0):
    if type(config) is str:
        if "frameworks" in config:
            table = ResourcePaperTable(config)
        else:
            table = PaperTable(config)
        for block in blocks:
            paper_item = convert_entry(block, filter_tags=[config])
            if paper_item:
                table.add_paper(paper_item)
        if table.papers:
            return table.to_rst_table(rst_headders[level])
        return None
    elif isinstance(config, types.GeneratorType) or type(config) is list:
        tables = []
        for c in config:
            paper_item = parse_helper(blocks, c, tags, level)
            if paper_item:
                tables.append(paper_item)
        return tables
    elif type(config) is dict:
        tables = []
        for k, v in config.items():
            if k == 'prompt_tuning':
                leaf_tags = []
                def get_leaf_tags(item):
                    if isinstance(item, str):
                        leaf_tags.append(item)
                    elif isinstance(item, dict):
                        for _, value in item.items():
                            get_leaf_tags(value)
                    elif isinstance(item, list):
                        for i in item:
                            get_leaf_tags(i)
                get_leaf_tags(v)

                table = PaperTable(k)
                added_papers = set()
                
                for block in blocks:
                    entry_tags_match = re.search(r"tags.*?\n|tags.*,\n", block)
                    if entry_tags_match:
                        entry_tags_str = entry_tags_match.group(0)
                        entry_tags = entry_tags_str.lower().replace("}", "").replace("{", "")
                        entry_tags = entry_tags.split("=")[1].strip().strip("{").strip("}").strip().split(",")
                        entry_tags = [tag.strip().strip('"').strip().lower() for tag in entry_tags]
                        processed_leaf_tags = [t.lower().replace('_', ' ') for t in leaf_tags]

                        if any(plt in entry_tags for plt in processed_leaf_tags):
                            paper_item = convert_entry(block, filter_tags=[])
                            if paper_item and paper_item.title not in added_papers:
                                table.add_paper(paper_item)
                                added_papers.add(paper_item.title)
                
                if table.papers:
                    paper_item = table.to_rst_table(rst_headders[level])
                else:
                    paper_item = None
            else:
                paper_item = parse_helper(blocks, v, tags + [k], level + 1)

            if paper_item:
                if k == 'prompt_tuning':
                    tables.append(paper_item)
                else:
                    if "protection" in k:
                        pass

                    def custom_title(text):
                        words = text.split()
                        title_cased_words = [
                            word.title() if not word.isupper() else word for word in words
                        ]
                        return " ".join(title_cased_words)

                    k = k.replace("_", " ")
                    heading = custom_title(k)
                    # heading = k.title()
                    tables.append(
                        f"\n{heading}\n" f"{rst_headders[level] * (len(heading) + 1)}\n\n"
                    )
                    tables.append(paper_item)
        return tables


def writer_helper(file, content):
    if type(content) is str:
        file.write(content)
    elif type(content) is list:
        for c in content:
            writer_helper(file, c)


def convert_bibtex(input_file, output_file, config_file):
    with open(input_file, "r", encoding="utf-8") as file:
        content = file.read()

    blocks = re.findall(r"@.*?({.*?(?:}\n}|,\n}|\"\n}|}}\n))", content, flags=re.DOTALL)

    with open(config_file, "r", encoding="utf-8") as file:
        config = yaml.safe_load_all(file)
        result = parse_helper(blocks, config, [])

        header = read_file("docs/overview.rst")
        citaiton = read_file("docs/citation.rst")
        with open(output_file, "w", encoding="utf8") as file:
            file.write(header)
            writer_helper(file, result)
            file.write(citaiton)
        # print(result)


def read_file(header_path):
    with open(header_path, "r", encoding="utf8") as file:
        header = file.read()
    return header


input_file = "docs/bibs/references.bib"
output_rst_file = "README.rst"
config_file = "scripts/contents.yaml"
convert_bibtex(input_file, output_rst_file, config_file)

output = pypandoc.convert_file(
    output_rst_file,
    "gfm",
    outputfile=output_rst_file.replace(".rst", ".md"),
    extra_args=["--wrap=preserve"],
)

os.remove(output_rst_file)

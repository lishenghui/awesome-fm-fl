import re


def convert_bibtex(input_file, output_file):
    with open(input_file, "r") as file:
        content = file.read()

    # 匹配含有 archivePrefix={arXiv} 的 @misc 条目
    def convert_entry(match):
        entry = match.group(0)
        eprint = re.search(r"eprint={([^}]+)}", entry)
        if eprint:
            eprint_value = eprint.group(1)
            url_line = f",\n      url={{https://arxiv.org/abs/{eprint_value}}},"
            article = f" \n      journal={{arXiv preprint arXiv:{eprint_value}}},\n"
            if entry[-1] == "\n":
                entry = entry[:-1]
            entry += url_line
            entry += article
            return re.sub(r"@misc{", "@article{", entry, 1)
        return entry

    converted_content = re.sub(r"@misc{.*?}\n", convert_entry, content, flags=re.DOTALL)
    # converted_content = re.sub(r'@misc{[^}]*?archivePrefix={arXiv}[^}]*?}', convert_entry, content, flags=re.DOTALL)

    with open(output_file, "w") as file:
        file.write(converted_content)


file = "./docs/bibs/references.bib"

convert_bibtex(file, file)

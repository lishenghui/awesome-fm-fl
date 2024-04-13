from dataclasses import dataclass
import re


month_map = {"jan": "01",
             "feb": "02",
             "mar": "03",
             "apr": "04",
             "may": "05",
             "jun": "06",
             "jul": "07",
             "aug": "08",
             "sep": "09",
             "oct": "10",
             "nov": "11",
             "dec": "12"}

@dataclass
class PaperInfo:
    title: str
    url: str
    year: str
    venue: str
    month: str = None
    github: str = "-"

    def __post_init__(self):
        if "arxiv" in self.url.lower():
            self.venue = "arXiv"
            if "doi.org" in self.url:
                year_month = self.url.split("/")[-1][6:10]
            else:
                year_month = self.url.split("/")[-1][:4]
            self.year = "20" + year_month[:2]
            self.month = year_month[-2:]

        if self.month in month_map:
            self.month = month_map[self.month]

    def to_rst_row(self):
        year = f"{self.year}-{self.month}" if self.month else f"20{self.year}"
        def parse_github(github):
            if github == "-":
                return f"     - -"
            if "github" in github:
                splits = github.split("/")[-2:]
                github = (f"     - .. image:: "
                          f"https://img.shields.io/github/stars/{splits[0]}/"
                          f"{splits[1]} \n"
                          f"          :target: {github} \n"
                          f"          :alt: GitHub Repo stars")
            return github
        # Plain title
        # row = f"   * - `{self.title} <{self.url}>`_\n"

        # Bold title
        row = (f"   * - .. raw:: html\n\n"
               f"          <strong><a href=\"{self.url}\">{self.title}</a></strong> \n")
        row += f"     - {self.venue}\n"
        row += f"     - {year}\n"
        row += parse_github(self.github)
        row += "\n"
        return row
def convert_bibtex(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()
    def convert_entry(match) -> PaperInfo:
        entry = match
        tags = re.search(r'tags.*?\n|tags.*,\n', entry)

        def parse_feild(field):
            return re.search(rf'{field}\s*=\s*(.*?)(?:,|\r?\n)', entry).group(
                1).strip("\"").strip("{").strip("}")

        if tags:
            tags = tags.group(0)
            # Convert to lowercase
            tags = tags.lower()
            if "application" in tags:
                title = parse_feild("title")
                title = title.replace("{", "").replace("}", "")
                url = parse_feild("url")
                year = parse_feild("year").strip("\"")

                try:
                    github = parse_feild("github")
                except AttributeError:
                    # print(f"Github not found for {title}")
                    github = "-"

                try:
                    venue = parse_feild("venue").strip("\"")
                except AttributeError:
                    venue = "-"
                try:
                    month = parse_feild("month")
                except AttributeError:
                    month = None
                paper_info = PaperInfo(title, url, year, venue, month=month, github=github)
                return paper_info
        return None

    blocks = re.findall(r'@.*?({.*?(?:}\n}|,\n}|\"\n}|}}\n))', content, flags=re.DOTALL)
    papers = []
    for block in blocks:
        paper_item = convert_entry(block)
        if paper_item:
            papers.append(paper_item)

    papers.sort(key=lambda x: x.year, reverse=True)

    application_papers = "Application \n=================\n\n"
    application_papers += """
.. list-table::
   :widths: 70 10 10 20
   :header-rows: 1
   
"""
    application_papers += "   * - Title\n     - Venue\n     - Year\n     - GitHub\n"
    for paper in papers:
        application_papers += (paper.to_rst_row())
    with open(output_file, 'w') as file:
        file.write(application_papers)

input_file = 'references.bib'  # 替换为你的输入文件路径
output_file = 'applications.rst'  # 替换为你期望的输出文件路径

convert_bibtex(input_file, output_file)

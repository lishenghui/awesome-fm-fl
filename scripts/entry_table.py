from dataclasses import dataclass
from typing import List
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
    venue: str = None
    month: str = None
    github: str = "-"

    def __post_init__(self):
        if not self.venue and "arxiv" in self.url.lower():
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
        year = f"{self.year}-{self.month}" if self.month else f"{self.year}"
        def parse_github(github):
            if github == "-":
                return f"     - -"
            if "github" in github:
                splits = github.split("/")[3:5]
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


@dataclass
class PaperTable:
    category: str
    papers: List[PaperInfo] = None

    def __post_init__(self):
        self.category = self.category.replace("_", " ").title()
    def add_paper(self, paper: PaperInfo):
        if self.papers is None:
            self.papers = []
        self.papers.append(paper)

    def to_rst_table(self, header="="):
        assert self.papers is not None, f"No papers added to the table, category: {self.category}"
        self.papers.sort(key=lambda x: (x.year, x.month if x.month else "01"),
                         reverse=True)
        application_papers = f"{self.category} \n{header * len(self.category)} \n\n"
        application_papers += """
.. list-table::
   :widths: 70 10 10 20
   :header-rows: 1

"""
        application_papers += "   * - Title\n     - Venue\n     - Year\n     - GitHub\n"
        for paper in self.papers:
            application_papers += (paper.to_rst_row())
        return application_papers


def convert_entry(match, filter_tags=None) -> PaperInfo:
    entry = match
    tags = re.search(r'tags.*?\n|tags.*,\n', entry)

    def parse_feild(field):
        return re.search(rf'\b{field}\s*=\s*(.*?)(?:,|\r?\n)', entry).group(
            1).strip("\"").strip("{").strip("}")

    paper_info = None
    if tags:
        tags = tags.group(0)
        tags = tags.lower().replace("}", "").replace("{", "")
        tags = tags.split("=")[1].strip().strip("{").strip("}").strip().split(",")
        tags = [tag.strip().strip("\"").strip().lower() for tag in tags]
        # Convert to lowercase
        for tag in filter_tags:
            tag = tag.lower().replace("_", " ")
            if tag not in tags:
                return paper_info
        # if "application" in tags and "recommendation systems" in tags:
        title = parse_feild("title")
        title = title.replace("{", "").replace("}", "")
        url = parse_feild("url")
        year = parse_feild("year").strip("\"")

        try:
            github = parse_feild("github")
        except AttributeError:
            github = "-"

        try:
            venue = parse_feild("venue").strip("\"")
        except AttributeError:
            venue = None
        try:
            month = parse_feild("month")
        except AttributeError:
            month = None
        paper_info = PaperInfo(title, url, year, venue, month=month, github=github)

    return paper_info
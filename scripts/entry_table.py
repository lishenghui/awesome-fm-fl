from dataclasses import dataclass
from typing import List
import re

month_map = {
    "jan": "01",
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
    "dec": "12",
}


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
                github = (
                    f"     - .. raw:: html\n\n"
                    f"          <img "
                    f'src="https://img.shields.io/github/stars/{splits[0]}/'
                    f"{splits[1]}"
                    f'" alt="GitHub Repo stars" style="vertical-align: '
                    f'middle; width: auto; height: auto;"/>\n'
                )
            return github

        # Bold title
        row = (
            f"   * - .. raw:: html\n\n"
            f'          <strong><a href="{self.url}">{self.title}</a></strong> \n'
        )
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

    def get_table_head(self):
        head_str = """
.. list-table::
   :widths: 70 10 10 20
   :header-rows: 1

"""
        head_str += "   * - Title\n     - Venue\n     - Year\n     - GitHub\n"
        return head_str

    def to_rst_table(self, header="="):
        assert (
            self.papers is not None
        ), f"No papers added to the table, category: {self.category}"
        self.papers.sort(
            key=lambda x: (x.year, x.month if x.month else "01"), reverse=True
        )
        papers_str = f"{self.category} \n{header * len(self.category)} \n\n"
        papers_str += self.get_table_head()
        for paper in self.papers:
            papers_str += paper.to_rst_row()
        return papers_str


@dataclass
class ResourcePaperInfo(PaperInfo):
    developer: str = "-"
    developer_logo: str = "-"

    def to_rst_row(self):
        row = super().to_rst_row()
        if self.developer_logo == "-" or self.developer_logo == "":
            row += f"     - {self.developer}\n"
        else:
            row += (
                f"     - .. raw:: html\n\n"
                f"          <img "
                f'src="https://img.shields.io/badge/{self.developer}-white?logo='
                f"{self.developer_logo}"
                f'" alt="GitHub Repo stars" style="vertical-align: '
                f'middle; width: 150px; height: auto;"/>\n'
            )
        return row


@dataclass
class ResourcePaperTable(PaperTable):
    def get_table_head(self):
        head_str = """
.. list-table::
   :widths: 40 10 10 20 20
   :header-rows: 1

"""
        head_str += "   * - Title\n     - Venue\n     - Year\n     - GitHub\n     - Developed by\n"
        return head_str


def convert_entry(match, filter_tags=None) -> PaperInfo:
    entry = match
    tags = re.search(r"tags.*?\n|tags.*,\n", entry)

    def parse_feild(field):
        return (
            re.search(rf"\b{field}\s*=\s*(.*?)(?:,\r|\r?\n)", entry)
            .group(1)
            .strip('"')
            .strip("},")
            .strip("{")
            .strip("}")
        )

    paper_info = None
    if tags:
        tags = tags.group(0)
        tags = tags.lower().replace("}", "").replace("{", "")
        tags = tags.split("=")[1].strip().strip("{").strip("}").strip().split(",")
        tags = [tag.strip().strip('"').strip().lower() for tag in tags]
        # Convert to lowercase
        for tag in filter_tags:
            tag = tag.lower().replace("_", " ")
            if tag not in tags:
                return paper_info
        title = parse_feild("title")
        title = title.replace("{", "").replace("}", "")
        url = parse_feild("url")
        year = parse_feild("year").strip('"')

        try:
            github = parse_feild("github")
        except AttributeError:
            github = "-"

        try:
            venue = parse_feild("venue").strip('"')
        except AttributeError:
            venue = None
        try:
            month = parse_feild("month")
        except AttributeError:
            month = None

        if "resources" in tags:
            try:
                developer = parse_feild("developer")
            except AttributeError:
                developer = "-"
            try:
                developer_logo = parse_feild("developer logo")
            except AttributeError:
                developer_logo = "-"
            paper_info = ResourcePaperInfo(
                title,
                url,
                year,
                venue,
                month=month,
                github=github,
                developer=developer,
                developer_logo=developer_logo,
            )
        else:
            paper_info = PaperInfo(title, url, year, venue, month=month, github=github)

    return paper_info

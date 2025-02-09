from jinja2 import Template
from pathlib import Path

with open("template.html", "r") as f:
    html_template = f.read()

slides_and_titles = [
    ("index.md", "UE22 - backend"),
    ("slides1.md", "UE22 - backend 1/3"),
    ("slides2.md", "UE22 - backend 2/3"),
    ("slides3.md", "UE22 - backend 3/3"),
]

for slide, title in slides_and_titles:
    output_file = Path(slide).with_suffix(".html")
    with output_file.open("w") as f:
        f.write(Template(html_template).render(title=title, md_file=slide))

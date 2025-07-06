from jinja2 import Environment, FileSystemLoader
import os
import shutil
from datetime import datetime

env = Environment(loader = FileSystemLoader("templates"))
pages = ["index", "about", "gallery", "link", "contact"]

os.makedirs("dist", exist_ok = True)

if os.path.exists("dist/static"):
    shutil.rmtree("dist/static")
shutil.copytree("static", "dist/static")

css_version = datetime.now().strftime("%Y%m%d")

for page in pages:
    template = env.get_template(f"{page}.html")
    output = template.render(css_version = css_version)

    output_path = f"dist/{page}.html"
    with open(f"dist/{page}.html", "w", encoding = "utf-8") as f:
        f.write(output)
    
    print(f"{output_path} generated successfully.")
import os
import sys

# Tambahkan path ke folder .github agar bisa mengimpor parts
sys.path.insert(0, os.path.join(os.getcwd(), ".github"))

from parts import readme_template

BASE_DIR = os.getcwd()
MAIN_README = "README.md"

def find_readmes():
    readme_links = []

    for root, dirs, files in os.walk(BASE_DIR):
        if "README.md" in files and root != BASE_DIR:
            rel_path = os.path.relpath(root, BASE_DIR)
            url_path = rel_path.replace(" ", "%20").replace("\\", "/")
            readme_links.append((rel_path, f"[{rel_path}](./{url_path}/README.md)"))

    return sorted(readme_links)

def write_main_readme(readme_links):
    with open(MAIN_README, "w", encoding="utf-8") as f:
        # Write header
        f.write(readme_template.HEADER.strip() + "\n\n")

        # Write Table of Contents
        for folder, link in readme_links:
            indent = "  " * folder.count(os.sep)
            f.write(f"{indent}- {link}\n")

        # Write footer
        f.write("\n" + readme_template.FOOTER.strip() + "\n")

if __name__ == "__main__":
    links = find_readmes()
    write_main_readme(links)

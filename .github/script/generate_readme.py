import os
import sys
from collections import defaultdict

# Tambahkan path ke folder .github agar bisa mengimpor parts
sys.path.insert(0, os.path.join(os.getcwd(), ".github"))

from parts import readme_template

BASE_DIR = os.getcwd()
MAIN_README = "README.md"

def find_readme_structure():
    structure = defaultdict(lambda: defaultdict(list))

    for root, dirs, files in os.walk(BASE_DIR):
        if "README.md" in files and root != BASE_DIR:
            rel_path = os.path.relpath(root, BASE_DIR)
            parts = rel_path.split(os.sep)

            if len(parts) >= 3:
                materi = parts[0]
                modul = parts[1]
                subjudul = parts[2]
                url_path = rel_path.replace(" ", "%20").replace("\\", "/")
                structure[materi][modul].append((subjudul, f"./{url_path}/README.md"))

    return structure

def write_main_readme(structure):
    with open(MAIN_README, "w", encoding="utf-8") as f:
        f.write(readme_template.HEADER.strip() + "\n\n")

        for materi, modul_dict in sorted(structure.items()):
            f.write(f"**Materi:** {materi}\n\n")
            for modul, paths in sorted(modul_dict.items()):
                f.write(f"**Modul:** {modul}\n")
                f.write("**Learning Path:**\n")
                for subjudul, link in sorted(paths):
                    f.write(f"- [{subjudul}]({link})\n")
                f.write("\n")
        
        f.write(readme_template.FOOTER.strip() + "\n")

if __name__ == "__main__":
    structure = find_readme_structure()
    write_main_readme(structure)

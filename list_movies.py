import os
import pathlib

# Current directory
path = pathlib.Path(__file__).parent.resolve()

root_folder_flag = True
ident = "    "
with open("files_list.txt", "w", encoding="utf-8") as f:
    for root, dirs, files in os.walk(path):
        if root_folder_flag:
            root_folder_flag = False
            continue

        cwd_name = os.path.basename(root)
        parent_dir_name = os.path.basename(os.path.dirname(root))

        if parent_dir_name.startswith("_Colecao"):
            f.write(ident * 1)
        if parent_dir_name.startswith("Movie"):
            f.write(ident * 2)

        f.write(cwd_name + "\n")

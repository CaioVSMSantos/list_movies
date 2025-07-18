import os
import pathlib
import sys

def main():
    # Define nome-base do arquivo de saída, ou usa padrão
    if len(sys.argv) >= 2:
        base_name = sys.argv[1]
    else:
        base_name = "movies_list"

    output_file = f"{base_name}.txt"

    # Diretório atual (onde está este script)
    path = pathlib.Path(__file__).parent.resolve()

    root_folder_flag = True
    ident = "    "  # 4 espaços

    # Abre (ou cria) o arquivo de saída
    with open(output_file, "w", encoding="utf-8") as f:
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

    print(f"Lista de filmes gravada em '{output_file}'")

if __name__ == "__main__":
    main()

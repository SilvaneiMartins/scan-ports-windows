import os
import fnmatch

def search_filename(filename):
    for root, _, files in os.walk("/"):
        for file in files:
            if fnmatch.fnmatch(file, filename):
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                file_modifierd = os.path.getmtime(file_path)
                file_accessed = os.path.getatime(file_path)

                print(f"Nome do arquivo: {file}")
                print(f"Caminho completo: {file_path}")
                print(f"Tamanho do arquivo: {file_size} bytes")
                print(f"Última modificação: {file_modifierd}")
                print(f"Último acesso: {file_accessed}")

    print(f"O arquivo '{filename}' não foi encontrado no sistema.")

def main():
    filename = input("Digite o nome do arquivo que deseja procurar: ")

    search_filename(filename)

if __name__ == "__main__":
    main()

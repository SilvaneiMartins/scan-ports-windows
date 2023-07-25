import os

def search_file(directory, filename):
    for root, _, files in os.walk(directory):
        if filename in files:
            file_path = os.path.join(root, filename)
            file_size = os.path.getsize(file_path)
            file_modified = os.path.getmtime(file_path)
            file_accessed = os.path.getatime(file_path)

            print(f"Nome do arquivo: {filename}")
            print(f"Caminho completo: {file_path}")
            print(f"Tamanho do arquivo: {file_size} bytes")
            print(f"Última modificação: {file_modified}")
            print(f"Último acesso: {file_accessed}")

            return

    print(f"O arquivo '{filename}' não foi encontrado no diretório '{directory}'.")

def main():
    directory = input("Digite o caminho do diretório para procurar o arquivo: ")
    filename = input("Digite o nome do arqivo que deseja procurar: ")

    search_file(directory, filename)

if __name__ == "__main__":
    main()


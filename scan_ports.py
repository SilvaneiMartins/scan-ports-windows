import socket

def scan_ports(target, start_port, end_port):
    open_port = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Define o tempo de espera (em segundos) para a conexão
        sock.settimeout(1)
        result = sock.connect_ex((target, port))

        if result == 0:
            open_port.append(port)

        sock.close()

    return open_port

def save_to_file(filename, target, open_port):
    with open(filename, 'w') as file:
        file.write(f"Portas abertas em {target}:\n")
        for port in open_port:
            file.write(f"Porta {port}: aberta\n")

def main():
    target = input("Digite o endereço de IP ou hostname do alvo: ")
    start_port = int(input("Digite a porta inicial para varredura: "))
    end_port = int(input("digite a porta final para a varredura: "))

    open_port = scan_ports(target, start_port, end_port)

    if open_port:
        filename = f"{target}_port_scan.txt"
        save_to_file(filename, target, open_port)
        print(f"As informações firan salvas em '{filename}'.")
    else:
        print(f"Nenhuma porta aberta foi encontrada.")

if __name__ == "__main__":
    main()

import socket

def scan_local_ips():
    local_ips = []
    prefix = input("Digite o prefixo da rede (exemplo: 192.168.0.1): ")

    for i in range(1, 255):
        ip = f'{prefix}{id}'
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Define um tempo de espera (em segundos) para tentativa de conexão
        sock.settimeout(1)

        # Tente se conectar a uma porta específica (pode ser ajustada conforme necessário)
        # Porta 80 é usada aqui como exemplo, mas pode ser substituída por outra.
        result = sock.connect_ex((ip, 80))

        if result == 0:
            local_ips.append(ip)

        sock.close()

    return local_ips

def main():
    print("Realizando a varredura de IPs na rede local...")
    ips = scan_local_ips()

    if ips:
        print("IPs encontrados na rede local:")
        for ip in ips:
            print(ip)
    else:
        print("Nenhum IP encontrado na rede local.")

if __name__ == "__main__":
    main()




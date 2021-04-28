import socket


def client(target: str, port: int, data: str):
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        cli.connect((target, port))
        if len(data):
            cli.send(data.encode(encoding='ascii', errors='ignore'))
        while True:
            recv_len = 1
            response_data = ''
            while recv_len:
                incomming_data = cli.recv(4096)
                recv_len = len(incomming_data)
                response_data += incomming_data.decode(
                    encoding='utf-8',
                    errors='ignore'
                )


                if recv_len < 4096:
                    break

            print(response_data)
            new_data = input("")
            new_data += '\n'
            cli.send(new_data.encode(encoding='ascii'))
    except Exception as e:
        print(f'[*] Client close connection by error: {e}')
        cli.close()

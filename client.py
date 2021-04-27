import socket
import threading
import subprocess


def client(target, port, data):
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        cli.connect((target, port))
        if data:
            cli.send(data)
        while True:
            recv_len = 1
            response_data = ''

            while recv_len:
                incomming_data = cli.recv(4096)
                recv_len = len(incomming-data)
                response_data += incomming_data

                if recv_len < 4096:
                    break
            print(response_data)

            data = input('')
            data += '\n'
            cli.send(data)
    except:
        print(f'[*] Client close connection...')
        cli.close()

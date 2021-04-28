import socket
from handler import Handler

def server(target, port, upload_path, execute, command):
    print('Server')
    print('Target', target, port)
    print('path', upload_path)
    print('execute cmd', execute, command)

    if not target:
        target = "0.0.0.0"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('target', target)
    print('port', port)
    server.bind((target, port))
    server.listen(5)

    while True:
        cli_socket, addr = server.accept()
        handler = Handler(cli_socket)
        print('Handler trhead object', handler)
        cli_thread = threading.Thread(
            target=handler.client,
            args=(upload_path, execute, command,)
        )
        cli_thread.start()

import socket

def server(target, port):

    if not target:
        target = "0.0.0.0"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('target', target)
    print('port', port)
    server.bind((target, port))
    server.listen(5)

    while True:
        cli_socket, addr = server.accept()
        cli_thread = threading.Thread(
            target=client_handler,
            args=(cli_socket,)
        )
        cli_thread.start()

def server(target, port):

    # if no target is defined, we listen on all interfaces
    if not len(target):
            target = "0.0.0.0"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target,port))
    server.listen(5)

    while True:
        cli_socket, addr = server.accept()

        # spin off a thread to handle our new client
        cli_thread = threading.Thread(
            target=client_handler,
            args=(cli_socket,)
        )
        cli_thread.start()

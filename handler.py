from .cmd import command as cmd

class Handler:


    def __init__(self, cli_socket):
        self.cli = cli_socket

    def client(self, upload_path, execute: str, command: str):
        if upload_path:
            file_buffer = ''
            while True:
                data = self.cli.recv(1024)
                if not data:
                    break
                else:
                    file_buffer += data

            try:
                with open(upload_path, 'wb') as file:
                    file.write(file_buffer)
                    self.cli.send(f'File saved, path: {upload_path}\r\n')
            except:
                self.cli.send(f"Can't save file on path: {upload_path}\r\n")

        if execute:
            stdout = cmd(execute)
            self.cli.send(stdout)

        if command:
            while True:
                self.cli.send('TT:$ ')
                cmd_buffer = ''
                while '\n'not in cmd_buffer:
                    cmd_buffer += self.cli.recv(1024)

                    response = cmd(cmd_buffer)
                    self.cli.send(response)

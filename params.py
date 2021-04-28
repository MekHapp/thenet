import argparse
import sys

from server import server
from client import client

description = """
Examples:
thenet.py -t 192.168.0.1 -p 5555 -l -c"
thenet.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe"
thenet.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\""
echo 'ABCDEFGHI' | ./thenet.py -t 192.168.11.12 -p 135"
"""

parser = argparse.ArgumentParser(
    description='Thenet tool',
    epilog=description,
    formatter_class=argparse.RawDescriptionHelpFormatter
)
parser.add_argument(
    '-l',
    '--listen',
    dest='listen',
    help='Server listen <host>:<port>',
    action='store_true',
    default=False
)
parser.add_argument(
    '-e',
    '--execute',
    dest='execute',
    help='Execute the file over connection'
)
parser.add_argument(
    '-t',
    '--target',
    dest='target',
    help='ip direction to send data'
)
parser.add_argument(
    '-c',
    '--cmdshell',
    dest='cmd_shell',
    help='insert commands',
    action='store_true',
    default=True
)
parser.add_argument(
    '-p',
    '--port',
    dest='port',
    help='Port connection',
    type=int,
    default=0,
)

parser.add_argument(
    '-u',
    '--upload',
    dest='upload_path',
    help='Upload file an write to destination' ,
)

params = parser.parse_args()
print('params', params)

listen = params.listen
execute = params.execute
target = params.target
cmd_shell = params.cmd_shell
port = params.port
up_path = params.upload_path

if not listen and target and port > 0:
    print('In client send stdin')
    stdin = sys.stdin.read()
    print(stdin)
    client(target, port, stdin)

if listen:
    server(target, port, up_path, execute, cmd_shell)

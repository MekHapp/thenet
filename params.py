import argparse

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
    dest='listen connection',
    help='Server listen <host>:<port>',
    action='store_true',
    default=False
)
parser.add_argument(
    '-e',
    '--execute',
    help='Execute the file over connection'
)
parser.add_argument(
    '-t',
    '--target',
    help='ip direction to send data'
)
parser.add_argument(
    '-c',
    '--cmdshell',
    dest='command shell',
    help='insert commands',
    action='store_true',
    default=True
)
parser.add_argument(
    '-p',
    '--port',
    help='Port connection' ,
    type=int,
    default=80,
)

parser.add_argument(
    '-u',
    '--upload',
    help='Upload file an write to destination' ,
    type=int,
)

params = parser.parse_args()
print('params', params)

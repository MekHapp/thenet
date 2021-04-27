import subprocess


def command(command):
    command = command.rstrip()
    try:
        stdout = subprocess.check_output(
            command,
            stderr=subprocess.STDOUT,
            shell=True
        )
    except:
        stdout = f"Can't execute: {command}"
    return stdout

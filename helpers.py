import subprocess

def list_to_dict(list: list, keys: list):
    """
        Converts the list containing all information of a macOS package (.pkg) into a dictionary.
        First parameter is a list usually comes as the output of 'pkgutil --pkgs' shell command as string and splitted into a list.
        Second parameter contains a list of all the keys used in the dict. i.e. ['package-id', 'volume', 'location'].
    """
    dictionary = dict()
    for key in keys:
        try:
            index = list.index(f'{key}:')
            dictionary[list[index].strip(':')] = list[index + 1]
        except ValueError:
            print(f'{key} not found!')
    return dictionary

def run_shell_command(program: str, args: list, separator = None):
    """
        Runs a program from shell with all given arguments.
        The first parameter takes the name of the program to be run as a string. i.e. 'pkgutil'
        Second parameter is a list of all the arguments as individual strings passed to that program. i.e. ['--pkgs']
        All arguments must contain single dash (-) or double dash (--) as necessary.
    """
    cmd = [program]

    for arg in args:
        cmd.append(arg)

    return subprocess.run(cmd, stdout=subprocess.PIPE).stdout.decode("utf-8")

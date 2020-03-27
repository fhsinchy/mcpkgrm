import os
from pathlib import Path
from .helpers import list_to_dict, run_shell_command

class Package:
    """
        Represents a single macOS package (.pkg). Contains necessary informations such as package-id, package version,
        volume the package is installed on and the full location.
    """
    def __init__(self, package_id: str, version: str, volume: str, location: str):
        self.package_id = package_id
        self.version = version
        self.volume = volume
        self.location = location

    def rem_pkg(self):
        '''
            Removes all files/directories installed with this package and removes the package receipt from system.
        '''
        only_files = run_shell_command('pkgutil', ['--only-files', '--files', self.package_id]).strip().split('\n')
        if len(only_files) > 0:
            for file in only_files:
                f = Path(f'{self.volume}/{self.location}/{file}')
                if f.is_file():
                    print(file, end=' ')
                    try:
                        f.unlink()
                    except FileNotFoundError:
                        pass
                    print(u'\u2713')
        else:
            print('NO FILES TO REMOVE!')

        only_dirs = run_shell_command('pkgutil', ['--only-dirs', '--files', self.package_id]).strip().split('\n')
        if len(only_dirs) > 0:
            for dir_ in reversed(only_dirs):
                d = Path(f'{self.volume}/{self.location}/{dir_}')
                if d.is_dir():
                    print(dir_, end= ' ')
                    try:
                        f.rmdir()
                    except FileNotFoundError:
                        pass
                    print(u'\u2713')
        else:
            print('NO DIRECTORY TO REMOVE!')

        print('REMOVING PACKAGE RECEIPT ->', end=' ')
        run_shell_command('pkgutil', ['--forget', self.package_id])
        print(u'\u2713')

        return

    def __str__(self):
        return f'{self.package_id} v{self.version}'

class Color:
    '''
        Used for styling output texts.
    '''
    GREEN = '\033[92m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

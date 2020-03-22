import os
from classes import Package, Color
from helpers import run_shell_command, list_to_dict

# checking if the script has root permission or not.
if not os.geteuid() == 0:
    exit("\nROOT PERMISSION REQUIRED!\n")

# printing the warning message and getting the user to agree.
print(f'''
    {Color.RED}{Color.BOLD}
    I CAN NOT GUARANTEE YOUR SYSTEM'S INTEGRITY. 
    REMOVING THE WRONG PACAKGE OR ANY OF THE SYSTEM PACKAGES, 
    MAY CAUSE SYSTEM FAILURE. 
    PLEASE BE CAREFUL WHILE USING mcpkgrm.
    {Color.END}
''')
agreement = input(f'WRITE {Color.BOLD}{Color.UNDERLINE}AGREE{Color.END} TO CONTINUE: ')
if agreement.lower() != 'agree':
    exit('OKAY THEN!')
os.system('clear')

def package_list():
    '''
        Finds all the packages installed in the system and creates objects for each of them.
        Puts all the objects in a list for further use.
    '''
    pkg_objs = list()

    pkgs = run_shell_command('pkgutil', ['--pkgs']).split()

    for pkg in pkgs:
        pkg_info = run_shell_command('pkgutil', ['--pkg-info', pkg]).split()

        pkg_info_dict = list_to_dict(pkg_info, ['package-id', 'version', 'volume', 'location'])

        pkg_obj = Package (
            pkg_info_dict['package-id'],
            pkg_info_dict['version'],
            pkg_info_dict['volume'],
            pkg_info_dict['location'],
        )

        pkg_objs.append(pkg_obj)

    return pkg_objs

# printing the main menu.
while True:
    pkg_objs = package_list()

    for index, pkg_obj in enumerate(pkg_objs):
        print(f'{index} -> {pkg_obj}')
    print('\nANYTHING BUT A NUMBER -> Exit')

    try:
        pkg_num = int(input('SELECT A PACKAGE: '))
    except ValueError:
        exit('ALREADY DONE!')

    try:
        selected_pkg = pkg_objs[pkg_num]
    except IndexError:
        exit('NOW YOU WENT TOO FAR BOY!')

    os.system('clear')
    confirmed = input(f'ARE YOU SURE ABOUT UNINSTALLING {Color.BOLD}{Color.RED}{selected_pkg}?{Color.END}\nYes/No: ')        

    if confirmed.lower() == 'yes':
        os.system('clear')
        selected_pkg.rem_pkg() # calling the methods for package removal.
        exit(f'{Color.BOLD}{Color.GREEN}{selected_pkg}{Color.END} UNINSTALLED SUCCESSFULLY!')
    elif confirmed.lower() == 'no':
        os.system('clear')
    else:
        exit('YOU DISOBEYED THE MASTER!')

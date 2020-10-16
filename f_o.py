import getpass
import time
import subprocess
import platform

from functions.os_functions import init_f_o
from functions.utlis import Style, validate_path, open_folder, print_error, print_success, print_primary


print_primary(f"""
{Style.bold + '**** Running...f_o ****' + Style.reset + Style.lightcyan}

Hey {Style.bold + getpass.getuser() + Style.reset + Style.lightcyan},

Thanks for using f_o!

Please revise config.py for sorting customization.

To get started, enter a folder pathway, ex : {Style.underline + 'User/Documents/sort_folder' + Style.reset}
""")

while True:
    current_dir = input(
        Style.lightcyan + "Folder pathway : " + Style.reset).strip()
    if not current_dir:
        print_error("Please enter a folder pathway \n")
    elif not validate_path(current_dir):
        print_error(f'Pathway: {current_dir} does not exist \n')
    else:
        print_success("✔︎ Pathway Exists!\n")
        time.sleep(0.2)
        confirm_input = str(input(
            Style.orange + f'? Confirm folder pathway : {current_dir} (Y/n) > ' + Style.reset).lower())
        if confirm_input == 'y':
            # Opens folder
            open_folder(current_dir)
            # Initiates file sorting process
            init_f_o(current_dir)
            break
        elif confirm_input == 'n':
            print_error("Please enter correct file pathway \n")
        else:
            print_error("Please confirm with 'y' or 'n'\n")

time.sleep(0.2)
print_primary(f"""
{Style.bold + '**** Finished Running...f_o ****' + Style.reset}
""")

from functions.os_functions import init_f_o
from functions.utlis import Style, validate_path, print_error, print_success, print_primary

print_primary(f"""
**** Running...f_o ****

Please revise config.py for sorting customization.

To start, enter folder pathway. Ex : User/Documents/sort_folder
""")

run_f_o: bool = True
while run_f_o:
    current_dir = input(
        Style.lightcyan + "Folder pathway : " + Style.reset).strip()
    if not current_dir:
        print_error("Please enter a folder pathway \n")
    elif not validate_path(current_dir):
        print_error(f'{current_dir} does not exist')
    else:
        print_success("Pathway Exists!\n")
        confirm_input = str(input(
            Style.orange + f'Confirm folder pathway : {current_dir} (y/n) ' + Style.reset).lower())
        if confirm_input == 'y':
            # Initiates file sorting process
            init_f_o(current_dir)
            run_f_o = False
        elif confirm_input == 'n':
            print_error("Please enter correct file pathway \n")
        else:
            print_error("Please confirm with 'y' or 'n'\n")

print_primary("""
**** Finished Running...f_o ****
""")

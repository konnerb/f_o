from functions.os_functions import create_folders, sort_files
from functions.utlis import Style, validate_path, print_error, print_success, print_primary

print_primary("""
**** Running...f_o ****

Please enter folder pathway. Ex : User/Documents/sort_folder
""")

run_f_o: bool = True
while run_f_o:
    current_dir = input(
        Style.lightcyan + "Folder pathway : " + Style.reset).strip()
    if not current_dir:
        print_error("Please enter a folder pathway")
    elif not validate_path(current_dir):
        print_error(f'{current_dir} does not exist')
    else:
        print_success("Pathway Exists!")
        confirm_input = str(input(
            Style.orange + f'Confirm folder pathway : {current_dir} (y/n) ' + Style.reset))

        if confirm_input == 'y':
            run_use_config: bool = True
            while run_use_config:
                use_config: str = str(
                    input(Style.orange + f'Use manual config? (y/n) ' + Style.reset))
                config_param: bool = True if use_config == 'y' else False if use_config == 'n' else use_config == ''
                if use_config == 'y' or use_config == 'n':
                    create_folders(current_dir, manual_config=config_param)
                    run_use_config = False
                    run_f_o = False
                else:
                    print_error("Please confirm with 'y' or 'n'")
        elif confirm_input == 'n':
            print_error("Please enter correct file pathway")
        else:
            print_error("Please confirm with 'y' or 'n'")

print_primary("""
**** Finished Running...f_o ****
""")

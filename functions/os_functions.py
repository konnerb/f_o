import os
import shutil
import time

from functions.utlis import printProgressBar, validate_path, Style, print_error, print_success, print_primary

config: dict = {
    'Images': ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.HEIC'],
    'Documents': ['.pdf', '.doc', '.docx', '.xls', '.odt', '.ps', '.wpd', '.html'],
    'Music': ['.mp3', '.aiff', '.wav', '.acc', '.m4p', '.aa'],
    'Movies': ['.mp4', '.mov', '.flv', '.m4v', '.3gp', '.3gp', 'MTS', '.M2TS', '.TS']
}


def required_folders(current_dir: str):
    """
    Checks current directory for required folders.
    @params:
        current_dir  - Required  : current directory (Str)
    """
    total_files: int = 0
    newF: dict = {}

    for f in os.listdir(current_dir):
        total_files += 1
        filename, file_ext = os.path.splitext(f)
        #print(filename, file_ext)
        try:
            if not file_ext:
                pass
            else:
                for key in config:
                    #print(config[key], file_ext)
                    if file_ext in config[key]:
                        #print('File_Ext exists in config', key)
                        if key in newF:
                            newF[key] += 1
                            #print('iterated ', newF[key])
                            break
                        else:
                            newF[key] = 1
                            #print('created', newF[key])
                            break
                else:
                    #print('File_Ext not in config', key)
                    if 'Other' in newF:
                        newF['Other'] += 1
                        #print('Iterated other', filename)
                    else:
                        newF['Other'] = 1
                        #print('Created other', filename)

        except FileExistsError:
            print_error(f'{f} already exists...')
        except PermissionError:
            print_error('Access denied...')

    print_success(f'Required folders for sorting: {newF} Total files : {total_files}')

    return [key for key in newF]


def create_folders(current_dir: str, manual_config=False):
    """
    Creates required sorted folders
    @params:
        current_dir   - Required  : current directory (Str)
        manual_config - Optional  : Using manual configuration (Bool)
    """
    run_prompts: bool = True
    while run_prompts:
        if manual_config:
            folders: list = required_folders(current_dir)
            file_exists: list = [
                f for f in folders if validate_path(current_dir, f)]
        elif not manual_config:
            folders: list = [item for item in input(
                Style.lightcyan + "Enter folders seperated by coma : " + Style.reset).replace(", ", ",").split(",")]
            file_exists: list = [
                f for f in folders if validate_path(current_dir, f)]
        if folders == ['']:
            print_error("Please enter a folder.")
        else:
            if file_exists and file_exists != ['']:
                print_error(f'{file_exists} already exist')

            confirm_folders = str(input(
                Style.orange + f'Confirm folders created : {folders} (y/n) ' + Style.reset))

            if confirm_folders == 'y':
                gh = folders
                for folder in gh:
                    try:
                      # print(os.path.exists(current_dir + '/' + str(folder)))
                      # if not os.path.exists(current_dir + '/' + str(folder)):
                        os.mkdir(os.path.join(current_dir, str(folder)))
                        print_success(f'Created folder...{folder}')

                    except FileExistsError:
                        print_error(f'{folder} already exists...')
                    except PermissionError:
                        print_error('Access denied...')

                run_prompts = False
            elif confirm_folders == 'n':
                print_error("Please enter required folders.")
            else:
                print_error("Please confirm file pathway with 'y' or 'n'.")

    sort_files(current_dir, folders)


def sort_files(current_dir: str, folders: list):
    """
    Sorts files in provided directory
    @params:
        current_dir  - Required  : Current directory (Str)
        folders      - Required  : Required folders for sorting (List)
    """
    print_success('\nSorting...\n')
    files_length: int = len(os.listdir(current_dir))
    total_sorted_files: int = 0

    printProgressBar(total_sorted_files, files_length,
                     prefix='Progress:', suffix='Complete', length=50)
    t1_start = time.process_time()

    for f in os.listdir(current_dir):
        total_sorted_files += 1
        filename, file_ext = os.path.splitext(f)
        try:
            if not file_ext:
                pass
            else:
                for folder in folders:
                    if folder == 'Other':
                        pass
                    elif file_ext in config[folder]:
                        shutil.move(
                            os.path.join(current_dir, f'{filename}{file_ext}'),
                            os.path.join(current_dir, folder, f'{filename}{file_ext}'))
                        break
                    else:
                        pass
                else:
                    shutil.move(
                        os.path.join(current_dir, f'{filename}{file_ext}'),
                        os.path.join(current_dir, 'Other', f'{filename}{file_ext}'))

        except FileNotFoundError:
            print_error(f'{filename} not found...')

        except PermissionError:
            print_error('Access denied...')

        time.sleep(0.1)
        printProgressBar(total_sorted_files, files_length,
                         prefix='Progress:', suffix='Complete', length=50)

    t1_stop = time.process_time()
    print()
    print_success(
        f'Sorted : {total_sorted_files} files in {round(t1_stop - t1_start, 3)} seconds')

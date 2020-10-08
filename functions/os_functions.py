import os
import shutil
import time

from config import config
from functions.utlis import printProgressBar, validate_path, Style, print_error, print_success, print_primary

# Initiates file sorting process


def init_f_o(current_dir):
    create_folders(current_dir)


def create_folders(current_dir: str):
    """
    Creates required sorted folders
    @params:
        current_dir   - Required  : current directory (Str)
    """
    run_prompts: bool = True
    while run_prompts:
        folders: list = required_folders(current_dir)
        file_exists: list = [f for f in folders if validate_path(current_dir, f)]
        if not folders:
            print_error(
                f'Current directory : {current_dir} is empty or has no files')
            break
        else:
            time.sleep(0.2)
            if file_exists and file_exists != ['']:
                print_error(
                    f'{file_exists} already exist.. To continue, confirm with "y" below \n')

            confirm_folders = str(input(
                Style.orange + f'Confirm folders created : {folders} (y/n) > ' + Style.reset).lower())
            
            if confirm_folders == 'y':
                print()
                time.sleep(0.2)
                gh = folders
                for folder in gh:
                    try:
                        os.mkdir(os.path.join(current_dir, str(folder)))
                        print_success(f'Created folder...{folder}')

                    except FileExistsError:
                        print_error(f'{folder} already exists...')
                    except PermissionError:
                        print_error('Access denied...')

                run_prompts = False
            elif confirm_folders == 'n':
                print_error("\nPlease revise config. Then restart f_o :)")
                break
            else:
                print_error("\nPlease confirm file pathway with 'y' or 'n'.")

    if folders and confirm_folders == 'y':
        organize_files(current_dir, folders)


def required_folders(current_dir: str):
    """
    Checks current directory for required folders.
    @params:
        current_dir  - Required  : current directory (Str)
    """
    total_files: int = 0
    newF: dict = {}
    # loops over current_directory
    for f in os.listdir(current_dir):
        filename, file_ext = os.path.splitext(f)
        try:
            if not config:
                print_error(
                    "Please create a valid config e.g. config = {'Images': ['.png', 'Landsape'],} \n")
                break
            else:
                total_files += 1
                for key in config:
                    # Determins if this file should be removed
                    if (
                        key == 'DELETE' 
                        and config[key] != []
                        and any([d in filename for d in (config[key])])
                        or file_ext in config[key]
                      ):
                        if key in newF:
                            newF[key] += 1
                            break
                        else:
                            newF[key] = 1
                            break
                    # Determins if this file contains given key value in the config e.g. 'Hip-Hop'
                    elif any([s in filename for s in (config[key])]):
                        if key in newF:
                            newF[key] += 1
                            break
                        else:
                            newF[key] = 1
                            break
                    # Determins if this file contains an extenstion key value in the config e.g. '.pdf'
                    elif file_ext in config[key]:
                        if key in newF:
                            newF[key] += 1
                            break
                        else:
                            newF[key] = 1
                            break
                # If this file does not match any key values in the config, it will create an 'Others' folder
                else:
                    if 'Other' in newF:
                        newF['Other'] += 1
                    else:
                        newF['Other'] = 1

        except FileExistsError:
            print_error(f'{f} already exists...')
        except PermissionError:
            print_error('Access denied...')

    if 'DELETE' in newF:
        print_error('Deleting : ' + str(newF['DELETE']) + ' files')
        newF.pop('DELETE')
    
    if newF:
        print_success(f'\nRequired folders for sorting: {newF} Total files : {total_files}')

    return [key for key in newF]


def organize_files(current_dir: str, folders: list):
    """
    Sorts files in provided directory
    @params:
        current_dir  - Required  : Current directory (Str)
        folders      - Required  : Required folders for sorting (List)
    """
    print_success('\nSorting...\n')

    files_length: int = len(os.listdir(current_dir))
    total_sorted_files: int = 0
    deleted_files: int = 0

    printProgressBar(total_sorted_files, files_length, prefix='Progress:', suffix='Complete', length=50)
    t1_start = time.process_time()

    # loops over current_directory
    for f in os.listdir(current_dir):
        total_sorted_files += 1
        filename, file_ext = os.path.splitext(f)
        try:
            if not file_ext:
                pass
            # Removes file if contains given key value in the config e.g. 'Hip-Hop'
            elif (
                'DELETE' in config
                and config['DELETE'] != []
                and any([d in filename for d in (config['DELETE'])])
                or file_ext in config['DELETE']
              ):
                os.remove(current_dir + '/' + filename + file_ext)
                deleted_files += 1
                continue
            else:
                for folder in folders:
                    if folder == 'Other':
                        pass
                    elif not folder in config:
                        print_error(
                            f'{folder} not in config : {config.keys()}\n')
                        break
                    # Sorts file if contains given key value in the config e.g. 'Hip-Hop'
                    elif any([s in filename for s in (config[folder])]):
                        shutil.move(
                            os.path.join(current_dir, f'{filename}{file_ext}'),
                            os.path.join(current_dir, folder, f'{filename}{file_ext}'))
                        break
                    # Sorts this file if it contains an extenstion key value in the config e.g. '.pdf'
                    elif file_ext in config[folder]:
                        shutil.move(
                            os.path.join(current_dir, f'{filename}{file_ext}'),
                            os.path.join(current_dir, folder, f'{filename}{file_ext}'))
                        break
                    else:
                        pass
                # If this file does not match any key values in the config,
                # it will be sorted into an 'Others' folder
                else:
                    shutil.move(
                        os.path.join(current_dir, f'{filename}{file_ext}'),
                        os.path.join(current_dir, 'Other', f'{filename}{file_ext}'))

        except FileNotFoundError:
            print_error(f'{filename} not found...')

        except PermissionError:
            print_error('Access denied...')
        
        except OSError as error:
            print_error(f'{error} \n{filename} cannot be deleted...')

        time.sleep(0.1)
        printProgressBar(total_sorted_files, files_length, prefix='Progress:', suffix='Complete', length=50)

    t1_stop = time.process_time()
    time.sleep(0.2)
    print_success(
        f'\nSorted : {total_sorted_files - len(folders)} files \nDeleted : {deleted_files} files \nIn {round(t1_stop - t1_start, 3)} seconds')

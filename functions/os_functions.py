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

    print('Required folders for sorting: ',
          newF, 'Total files : ', total_files)


def create_folders(current_dir: str):
    """
    Creates required sorted folders
    @params:
        current_dir  - Required  : current directory (Str)
    """
    run_prompts: bool = True
    while run_prompts:
        required_folders(current_dir)
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


def sort_files(current_dir: str):
    """
    Sorts files in provided directory
    @params:
        current_dir  - Required  : current directory (Str)
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
            elif file_ext in ('.png', '.jpg', 'jpeg'):
                shutil.move(
                    os.path.join(current_dir, f'{filename}{file_ext}'),
                    os.path.join(current_dir, 'Images', f'{filename}{file_ext}'))
            elif file_ext in ('.mp3', '.aiff'):
                shutil.move(
                    os.path.join(current_dir, f'{filename}{file_ext}'),
                    os.path.join(current_dir, 'Music', f'{filename}{file_ext}'))
            elif file_ext in ('.pdf'):
                shutil.move(
                    os.path.join(current_dir, f'{filename}{file_ext}'),
                    os.path.join(current_dir, 'Documents', f'{filename}{file_ext}'))
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

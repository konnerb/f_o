import os
import shutil
import time

from functions.utlis import printProgressBar, Style, print_error, print_success, print_primary

#Creates Required Sorted Folders
def create_folders(current_dir):
  run_prompts = True
  while run_prompts: 
      folders = [item for item in input(Style.lightcyan + "Enter folders seperated with coma : " + Style.reset).split(", ")]
      if folders == ['']:
        print_error("Please enter a folder.")
      else:
        confirm_folders = str(input(Style.orange + f'Confirm folders created : {folders} (y/n) ' + Style.reset))
        if confirm_folders == 'y':
          gh = folders
          for folder in gh:
            try:
              # print(os.path.exists(current_dir + '/' + str(folder)))
              # if not os.path.exists(current_dir + '/' + str(folder)):
                os.mkdir(os.path.join(current_dir, str(folder)))
                print_success(f'Created folder...{folder}')

            except (FileExistsError, PermissionError):
              print_error(f'{folder} already exists...')

          run_prompts = False
        elif confirm_folders == 'n':
          print_error("Please enter required folders.")
        else:
          print_error("Please confirm file pathway with 'y' or 'n'.")

#Sorts Files in Provided Directory
def sort_files(current_dir):
  print_success('Sorting...\n')

  files_length = len(os.listdir(current_dir))
  total_sorted_files = 0
  
  printProgressBar(total_sorted_files, files_length, prefix = 'Progress:', suffix = 'Complete', length = 50)
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
          os.path.join(current_dir, 'Other Stuff', f'{filename}{file_ext}'))

    except (FileNotFoundError, PermissionError):
      pass
  
    time.sleep(0.1)
    printProgressBar(total_sorted_files, files_length, prefix = 'Progress:', suffix = 'Complete', length = 50)
  
  t1_stop = time.process_time() 
  print()
  print_success(f'Sorted : {total_sorted_files} files in {round(t1_stop - t1_start, 3)} seconds')

import os
import shutil
import time

from functions.utlis import printProgressBar, style

#Creates Required Sorted Folders
def create_folders(current_dir):
  run_prompts = True
  while run_prompts: 
      folders = [item for item in input(style.lightcyan + "Enter folders seperated with coma : " + style.reset).split(", ")]
      if folders == ['']:
        print(style.error + "Please enter a folder." + style.reset)
      else:
        confirm_folders = str(input(style.orange + f'Confirm folders created : {folders} (y/n) ' + style.reset))
        if confirm_folders == 'y':
          gh = folders
          for folder in gh:
            try:
              # print(os.path.exists(current_dir + '/' + str(folder)))
              # if not os.path.exists(current_dir + '/' + str(folder)):
                os.mkdir(os.path.join(current_dir, str(folder)))
                print(style.green + f'Created folder...{folder}' + style.reset)

            except (FileExistsError, PermissionError):
              print(folder, 'already exists...')

          run_prompts = False
        elif confirm_folders == 'n':
          print(style.error + "Please enter required folders." + style.reset)
        else:
          print(style.error + "Please confirm file pathway with 'y' or 'n'." + style.reset)

#Sorts Files in Provided Directory
def sort_files(current_dir):
  print(style.green + 'Sorting...' + style.reset)

  files_length = len(os.listdir(current_dir))
  total_sorted_files = 0
  
  printProgressBar(total_sorted_files, files_length, prefix = 'Progress:', suffix = 'Complete', length = 50)
  
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

  print(style.green + f'Sorted : {total_sorted_files} files' + style.reset)

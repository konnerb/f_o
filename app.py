import os
import shutil
import time

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def create_files(cur_dir):
  folders = [item for item in input("Enter folders seperated with coma : ").split(",")] 
  confirm_folders = input(f'Confirm Folders Created "{folders}" (y/n) ')
  if confirm_folders == 'y' and len(folders) > 0:
    gh = folders
    for folder in gh:
      os.mkdir(os.path.join(cur_dir,str(folder)))
      print(f'Created folder...{folder}')
  else:
    print("Please enter required folders.")

def sort_files(cur_dir):
  print('Sorting...')
  
  files_length = len(os.listdir(cur_dir))
  total_files = 0
  # Initial call to print 0% progress
  printProgressBar(total_files, files_length, prefix = 'Progress:', suffix = 'Complete', length = 50)
  
  for f in os.listdir(cur_dir):
    total_files += 1
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
    # Update Progress Bar
    printProgressBar(total_files, files_length, prefix = 'Progress:', suffix = 'Complete', length = 50)

  print(f'Sorted : {total_files} files')


print("""
**** Running...f_o ****

Please enter folder pathway. Ex : Users/Documents/sort_folder
""")

current_dir = input("Folder pathway : ")

if len(current_dir) == 0:
  print("Please enter folder pathway")
else:
  confirm_input = input(f'Confirm folder pathway {current_dir} (y/n) ')
  if confirm_input == 'y':
    create_files(current_dir)
    sort_files(current_dir)
  else:
    print("Please enter correct file pathway")

print("""
**** Finished Running...f_o ****
""")
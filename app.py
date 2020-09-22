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
        
#Creates Required Sorted Folders
def create_folders(cur_dir):
  folders = [item for item in input("Enter folders seperated with coma : ").split(", ")]
  if folders == ['']:
    print("Please enter a folder.")
    folders = [item for item in input("Enter folders seperated with coma : ").split(", ")]
  else:
    loop = True
    confirm_folders = str(input(f'Confirm folders created : {folders} (y/n) '))
    while loop:
      if confirm_folders == 'y':
        gh = folders
        for folder in gh:
          os.mkdir(os.path.join(cur_dir,str(folder)))
          print(f'Created folder...{folder}')
        loop = False
      elif confirm_folders == 'n':
        print("Please enter required folders.")
        folders = [item for item in input("Enter folders seperated with coma : ").split(", ")] 
        confirm_folders = str(input(f'Confirm folders created : {folders} (y/n) '))
      else:
        print("Please confirm file pathway with 'y' or 'n'.")
        folders = [item for item in input("Enter folders seperated with coma : ").split(", ")] 

#Sorts Files in Provided Directory
def sort_files(cur_dir):
  print('Sorting...')

  files_length = len(os.listdir(cur_dir))
  total_sorted_files = 0
  
  printProgressBar(total_sorted_files, files_length, prefix = 'Progress:', suffix = 'Complete', length = 50)
  
  for f in os.listdir(cur_dir):
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

  print(f'Sorted : {total_sorted_files} files')


print("""
**** Running...f_o ****

Please enter folder pathway. Ex : Users/Documents/sort_folder
""")

current_dir = input("Folder pathway : ")

if len(current_dir) == 0:
  print("Please enter a folder pathway")
  current_dir = input("Folder pathway : ")
else:
  loop = True
  confirm_input = str(input(f'Confirm folder pathway {current_dir} (y/n) '))
  while loop:
    if confirm_input == 'y':
      create_folders(current_dir)
      sort_files(current_dir)
      loop = False
    elif confirm_input == 'n':
      print("Please enter correct file pathway")
      current_dir = input("Folder pathway : ")
      confirm_input = input(f'Confirm folder pathway {current_dir} (y/n) ')
    else:
      print("Please confirm file pathway with 'y' or 'n'.")
      confirm_input = input(f'Confirm folder pathway {current_dir} (y/n) ')

print("""
**** Finished Running...f_o ****
""")
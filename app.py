import os
import shutil


# current_dir = ""
# # current_dir = os.getcwd()
# # os.chdir('')



print("""
**** Running...f_o ****

Please Enter Folder Pathway. Ex Users/Documents/sort_folder
""")

def create_files(cur_dir):
  folders = [item for item in input("Enter Folders seperated with coma : ").split(",")] 
  confirm_folders = input(f'Confirm Folders Created "{folders}" (y/n) ')
  if confirm_folders == 'y':
    gh = folders
    for folder in gh:
      os.mkdir(os.path.join(cur_dir,str(folder)))
      print(f'Created Folder...{folder}')
  else:
    print("Please Enter Required Folder")

def sort_files(cur_dir):
  for f in os.listdir(cur_dir):
    filename, file_ext = os.path.splitext(f)
    print(f)
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

current_dir = input("Folder Pathway: ")

if len(current_dir) == 0:
  print("Please Enter Folder Pathway")
else:
  confirm_input = input(f'Confirm Folder Pathway {current_dir} (y/n) ')
  if confirm_input == 'y':
    create_files(current_dir)
    sort_files(current_dir)
  else:
    print("Please Enter Correct File Pathway")

print("finished")
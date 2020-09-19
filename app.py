import os
import shutil


# current_dir = ""
# # current_dir = os.getcwd()
# # os.chdir('')


print("""
**** Running...f_o ****

Please Enter Folder Pathway. Ex Users/Documents/sort_folder
""")

current_dir = input("Folder Pathway: ")

if len(current_dir) == 0:
  print("Please Enter Folder Pathway")
else:
  confirm_input = input("Are Your Sure? (y/n) ")
  if confirm_input == 'y':
    print("Sorting Files...")
    for f in os.listdir(current_dir):
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
  else:
    print("Please Enter Correct File Pathway")

print("finished")
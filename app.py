import os
import shutil

current_dir = ""
# current_dir = os.getcwd()
# os.chdir('')

for f in os.listdir(current_dir):
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

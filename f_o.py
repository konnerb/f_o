from functions.os_functions import create_folders, sort_files
from functions.utlis import style

print("""
**** Running...f_o ****

Please enter folder pathway. Ex : Users/Documents/sort_folder
""")

run_app = True

while run_app:
  current_dir = input(style.lightcyan + "Folder pathway : " + style.reset)
  if len(current_dir) == 0:
    print(style.error + "Please enter a folder pathway" + style.reset)
  else:
    confirm_input = str(input(style.orange + f'Confirm folder pathway : {current_dir} (y/n) ' + style.reset))
    if confirm_input == 'y':
      create_folders(current_dir)
      sort_files(current_dir)
      run_app = False
    elif confirm_input == 'n':
      print(style.error + "Please enter correct file pathway" + style.reset)
    else:
      print(style.error + "Please confirm file pathway with 'y' or 'n'" + style.reset) 

print("""
**** Finished Running...f_o ****
""")
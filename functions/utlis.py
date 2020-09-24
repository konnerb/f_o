import os

# Colours For Console Text
class Style: 
    reset='\033[0m'
    error='\033[31m'
    lightblue='\033[94m'
    orange='\033[33m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    black='\033[30m'
    green='\033[32m'
    blue='\033[34m'
    purple='\033[35m'
    cyan='\033[36m'
    lightgrey='\033[37m'
    darkgrey='\033[90m'
    lightred='\033[91m'
    lightgreen='\033[92m'
    yellow='\033[93m'
    pink='\033[95m'
    lightcyan='\033[96m'

# Print Functions With Style colours
print_error = lambda text: print(Style.error + text + Style.reset)
print_success = lambda text: print(Style.green + text + Style.reset)
print_primary = lambda text: print(Style.lightcyan + text + Style.reset)
print_secondary = lambda text: print(Style.orange + text + Style.reset)

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
    print(Style.lightcyan + f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd + Style.reset)
    # Print New Line on Complete
    if iteration == total: 
        print()

def validate_path(current_dir, *folder):
  if current_dir and folder:
    return bool(os.path.exists(current_dir + '/' + str(folder)))
  else:
    return bool(os.path.exists(current_dir))


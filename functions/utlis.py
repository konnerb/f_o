import os

# Colours for console text
class Style:
    reset = '\033[0m'
    error = '\033[31m'
    lightblue = '\033[94m'
    lightcyan = '\033[96m'
    green = '\033[32m'
    orange = '\033[33m'
    bold = '\033[01m'
    underline = '\033[04m'
    disable = '\033[02m'
    reverse = '\033[07m'
    purple = '\033[35m'
    cyan = '\033[36m'


# Print functions with Style colours
def print_error(text: str): return print(Style.error + text + Style.reset)
def print_success(text: str): return print(Style.green + text + Style.reset)
def print_primary(text: str): return print(Style.lightcyan + text + Style.reset)
def print_secondary(text: str): return print(Style.orange + text + Style.reset)


def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
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
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(Style.lightcyan +
          f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd + Style.reset)
    # Print new line on complete
    if iteration == total:
        print()


def validate_path(current_dir: str, folder: str = '') -> bool:
    """
    Validates file directories
    @params:
        current_dir  - Required  : current directory path (Str)
        folder       - Optional  : folder path (Str)
    """
    if current_dir and folder:
        return bool(os.path.exists(current_dir + '/' + str(folder)))
    else:
        return bool(os.path.exists(current_dir))

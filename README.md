## f_o

A simple and dynamic file organizer created in Python.

### How it works? 

After entering your desired directory for sorting, f_o will verify if the directory exists and if any files exist. Then, with the given configuration, f_o will check which folders need to be created for the sorted files. After confirming the folders created, f_o will begin sorting all the files in the given directory according to the file extensions. 

### Editing the config

In the config.py file, f_o comes with stock presets for creating new folders and sorting files. You can customize the config file as long as there is more than one key, as in "Images" and more than one file extension value ['.png', ...]. Any files that are not in the config will be automatically sorted into an 'Others' folder.

### Whats next?

In the near future, there will be additional support for sorting files based on given key-words. 

## How to run locally

```bash
git clone https://github.com/konnerb/f_o.git
cd f_o
python3 f_o.py
```
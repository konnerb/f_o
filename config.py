
'''
  For f_o to work, ensure more than one key, as in "Images", and more than one value ['.png', ...] is
  in the config dictionary below. For any files that are not in the config, they'll be automatically
  sorted in an 'Others' folder.
  
  Examples:
    >> 'Images': ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.HEIC'],
    >> 'Documents': ['.pdf', '.doc', '.docx', '.xls', '.odt', '.ps', '.wpd', '.html'],
    >> 'Music': ['.mp3', '.aiff', '.wav', '.acc', '.m4p', '.aa'],
    >> 'Movies': ['.mp4', '.mov', '.flv', '.m4v', '.3gp', '.3gp', 'MTS', '.M2TS', '.TS']

'''

# Edit config here:
config: dict = {
    'Images': ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.HEIC'],
    'Documents': ['.pdf', '.doc', '.docx', '.xls', '.odt', '.ps', '.wpd', '.html'],
    'Music': ['.mp3', '.aiff', '.wav', '.acc', '.m4p', '.aa'],
    'Movies': ['.mp4', '.mov', '.flv', '.m4v', '.3gp', '.3gp', 'MTS', '.M2TS', '.TS']
}

filter_files: dict = {

}

'''
For f_o to work, ensure more than one key, as in 'Music', and more than one value ['.mp4'] or ['Hip-Hop'] is 
in the config dictionary below. Any files that are not in the config will be automatically sorted 
into an 'Others' folder.
  
  Examples:
    
    Sort files by generic file extentions:
      >> 'Images': ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.HEIC'],
      >> 'Documents': ['.pdf', '.doc', '.docx', '.xls', '.odt', '.ps', '.wpd', '.html'],
      >> 'Music': ['.mp3', '.aiff', '.wav', '.acc', '.m4p', '.aa'],
      >> 'Movies': ['.mp4', '.mov', '.flv', '.m4v', '.3gp', '.3gp', 'MTS', '.M2TS', '.TS']
    
    Or sort files by keywords
      >> 'Genre': ['House', 'Hip-Hop', 'Pop'],
      >> 'Cuisine': ['French', 'Jamican', 'Mexican'],

    Or delete files with keywords
      >> 'DELETE': ['House', 'Hip-Hop', 'Pop'],

'''

# Edit config here:
config: dict = {
    'DELETE': ['maps'], # <<<*** CAUTION: ANY FILE WITH VALUES ENTERED HERE WILL BE PERMANENTLY DELETED

    'Images': ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.HEIC'],
    'Documents': ['.pdf', '.doc', '.docx', '.xls', '.odt', '.ps', '.wpd', '.html'],
    'Music': ['.mp3', '.aiff', '.wav', '.acc', '.m4p', '.aa'],
    'Movies': ['.mp4', '.mov', '.flv', '.m4v', '.3gp', '.3gp', 'MTS', '.M2TS', '.TS'],
    'Genre': ['House', 'Hip-Hop', 'Pop'],
}

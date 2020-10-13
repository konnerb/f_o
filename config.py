'''
For f_o to work, ensure more than one key, as in 'Music,' and more than one value ['.mp4', '...'] or 
['Hip-Hop', ['...'] is in the config dictionary below. Values are case-sensitive and all files that 
are not found in the config will be automatically sorted into an 'Others' folder.

You can enable or disable keys/values by commenting them out with # for single line or ''' ''' for multiline.

**** USE THE DELETE KEY WITH CAUTION. ANY VALUE ENTERED WILL DELETE YOUR FILES FOREVER ****
        >>  Consider creating a 'Trash' Folder for files you wish to delete. 
            Then review and discard of the files afterwords.
  
  Examples:

    Delete by keywords or extentions.
    'DELETE': [House', 'Hip-Hop', 'Pop', '.png', '.mp3', '.pdf'],
    
    Or sort files by keywords e.g. 'value'
      >> 'Genre': ['House', 'Hip-Hop', 'Pop'],
      >> 'Cuisine': ['French', 'Jamican', 'Mexican'],
      >> 'Trash': ['random_stuff', 'random', 'stuff']

    Or sort files by generic file extentions:
      >> 'Images': ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.HEIC'],
      >> 'Documents': ['.pdf', '.doc', '.docx', '.xls', '.odt', '.ps', '.wpd', '.html'],
      >> 'Music': ['.mp3', '.aiff', '.wav', '.acc', '.m4p', '.aa'],
      >> 'Movies': ['.mp4', '.mov', '.flv', '.m4v', '.3gp', '.3gp', 'MTS', '.M2TS', '.TS']
      >> 'Trash': ['.mp4', '.png', '.pdf']
    
'''

# Edit config here:
config: dict = {
  
    # Delete by keywords or extentions here:  e.g. 'value' or '.value'
    'DELETE': [], # <<< *** CAUTION: ANY FILE WITH VALUES ENTERED HERE WILL BE PERMANENTLY DELETED

    # Sort by keywords here:  e.g. 'value'
    'Genre': ['House', 'Hip-Hop', 'Pop'],
    'Cuisine': ['French', 'Jamican', 'Mexican'],

    # Sort by file extention here:  e.g. '.value'
    'Images': ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.HEIC'],
    'Documents': ['.pdf', '.doc', '.docx', '.xls', '.odt', '.ps', '.wpd', '.html'],
    'Music': ['.mp3', '.aiff', '.wav', '.acc', '.m4p', '.aa'],
    'Movies': ['.mp4', '.mov', '.flv', '.m4v', '.3gp', '.3gp', 'MTS', '.M2TS', '.TS'],
}

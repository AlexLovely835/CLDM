import random

prefixes = [
    'Honey',
    'Amber',
    'Storm',
    'Dragon',
    'Cri',
    'South',
    'Swift',
    'Wilde',
    'Shroud',
    'Ocean',
    'East',
    'North',
    'West',
    'Fal',
    'Man',
    'Cher',
    'Fall',
    'Oak',
    'Val',
    'Vas', 
    'Alt',
    'Stu', 
    'Els',
    'Shad', 
    'Sword',
    'Black',

]

suffixes = [
    'helm', 
    'brook', 
    'wood', 
    'gard',
    'worth',
    'dale', 
    'haven',
    'ville',
    'heim', 
    'edge', 
    'valley',
    'lake', 
    'on', 
    'grim', 
    'well', 
    'pool',
    'croft'
]

def generateName():
    return random.choice(prefixes) + random.choice(suffixes)
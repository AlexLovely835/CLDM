import random 
from dice import rollDice

def generatePlainsName(town=None)
    prefix = ['Sickly', 'Whispering', 'Lonely', 'Stormy', 'Sacred']
    if town:
        prefix.append(town.name)
    suffix = [' Plains', ' Valley', ' Grasslands', ' Field']
    return random.choice(prefix) + random.choice(suffix)

def generatePlainsDesc(name, climate):
    if climate == 'Temperate':
        grass_colors = ['golden', 'yellow', 'brown', 'green']
        vegetation = ['grass', 'brambles', 'thickets', 'bushes']
        desc_word = ['lush', 'peaceful', 'calm', 'windswept']
    elif climate == 'Tropical':
        grass_colors = ['dark green', 'light green']
        vegetation = ['grass', 'bushes', 'flowering bushes']
        desc_word = ['wild', 'untamed', 'lush']
    elif climate == 'Arid':
        grass_colors = ['golden brown', 'yellow', 'brown']
        vegetation = ['thickets', 'sparse grass']
        desc_word = ['sparse', 'desolate', 'sandy']
    else:
        grass_colors = ['green', 'brown']
        vegetation = ['clumped grass', 'sparse bushes', 'thickets']
        desc_word = ['snowy', 'frosted', 'icy']
    
    desc = random.choice(desc_word)
    return f"The {name} is a {desc} plain that is covered in {random.choice(grass_colors)} {random.choice(vegetation)}.", f"{desc} plains"
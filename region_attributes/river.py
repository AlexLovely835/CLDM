import random 
from dice import rollDice

def generateRiverName(town = None):
    prefix = ['Great', 'Red', 'White', 'Wild']
    if town:
        prefix.append(town.name)
    suffix = [' River']
    return random.choice(prefix) + random.choice(suffix)

def generateRiverDesc(name):
    river_shape = ['straight', 'meandering']
    river_channel = ['single channelled', 'multi-channelled']
    river_bars = ['', ' and is braided', ' with channel bars']
    river_fish = ['bass', 'bream', 'carp', 'catfish', 'crappie', 'guppy', 'perch', 'pike', 'trout', 'salmon', 'tilapia', 'walleye']

    desc_word = random.choice(['swift', 'rushing', 'broad', 'little','shallow', 'muddy', 'clear', 'vast', 'dangerous', 'perilous'])
    return f"The {name} is a {desc_word} river that is {random.choice(river_shape)} and {random.choice(river_channel)}{random.choice(river_bars)}. The river is known for its {random.choice(river_fish)}.", f"{desc_word} river"

def generateSupportedProfessions():
    return {
        'fishing': rollDice('8d6'),
        'foraging': rollDice('2d6'), 
        'farming': rollDice('6d6')
    }
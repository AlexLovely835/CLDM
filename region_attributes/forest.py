import random
from dice import rollDice

def generateForestName(town = None):
    prefix = ['Big', 'Old', 'Dead', 'Shadowy']
    if town:
        prefix.append(town.name)
    suffix = ['wood', ' Forest', ' Woods', ' Timberland', ' Grove', ' Wood', ' Woodland']
    return random.choice(prefix) + random.choice(suffix)

def generateForestDesc(climate, name):
    if climate == 'Temperate':
        tree_types = ['oak', 'beech', 'maple', 'hickory', 'basswood']
        animal_types = ['deer', 'raccoons', 'wolves', 'bears', 'coyotes', 'foxes', 'squirrels', 'rabbits']
    else:
        tree_types = ['pine', 'spruce', 'larch', 'fir', 'birch', 'poplar']
        animal_types = ['bears', 'beavers', 'caribou', 'wolves', 'owls', 'lynx', 'moose', 'wolverines']

    desc_word = random.choice(['dense', 'flourishing', 'overgrown', 'enchanted', 'ominous', 'misty', 'shadowy', 'lush'])
    return f"The {name} is a {desc_word} {climate.lower()} forest that has many {random.choice(tree_types)} trees and a strong population of {random.choice(animal_types)}.", f"{desc_word} forest"

def generateSupportedProfessions():
    return {
        'woodcutting': rollDice('8d6'),
        'foraging': rollDice('4d6'),
        'hunting': rollDice('4d6'), 
        'farming': rollDice('3d6')
    }

    
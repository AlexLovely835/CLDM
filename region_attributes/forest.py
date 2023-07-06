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
        'woodcutting': rollDice('3d6'),
        'foraging': rollDice('2d6'),
        'hunting': rollDice('2d6')
    }

def generateForestResources():
    common_resources = []
    woodcutting = ['lumber']
    foraging = ['mushrooms', 'alchemical herbs', 'flowers', 'nuts', 'berries']
    hunting = ['common game', 'exotic game', 'monster parts']

    common_resources.append(random.choice(woodcutting))
    choice = random.choice(foraging)
    foraging.remove(choice)
    common_resources.append(choice)
    common_resources.append(random.choice(foraging))
    common_resources.append(random.choice(hunting))

    return common_resources
    
import random
from dice import rollDice

def generateMountainName(town = None):
    prefix = ['Stormy', 'Misty', 'Foggy', 'Evil', 'Doom']
    if town:
        prefix.append(town.name)
    preprefix = ['Mount ']
    suffix = [' Mountain', ' Mountains', ' Peaks', ' Peak']
    if random.random() > 0.5:
        return random.choice(preprefix) + random.choice(prefix)
    else:
        return random.choice(prefix) + random.choice(suffix)

def generateMountainDesc(name):
    mountain_type = ['folded', 'volcanic', 'domed', 'blocked']
    mountain_surface = ['snow-peaks', 'sandy rocks', 'gray rocks', 'sparse vegetation', 'thick forests']
    mountain_animals = ['bighorn sheep', 'eagles', 'lynx', 'wolves', 'bears', 'deer', 'snow leopards']

    desc_word = random.choice(['vast', 'towering', 'craggy', 'looming', ])
    return f"The {name} are a {desc_word} {random.choice(mountain_type)} mountain range covered in {random.choice(mountain_surface)}. This mountain range is home to many {random.choice(mountain_animals)}", f"{desc_word} mountains"

def generateSupportedProfessions():
    return {
        'mining': rollDice('3d6'),
        'foraging': rollDice('1d6'),
        'hunting': rollDice('2d6')
    }

def generateMountainResources():
    common_resources = []
    mining = ['iron ore', 'copper ore', 'tin ore', 'coal', 'gemstones', 'gold ore', 'silver ore', 'granite', 'marble', 'stone']
    foraging = ['mushrooms', 'alchemical herbs', 'mountain flowers', 'nuts', 'berries']
    hunting = ['common game', 'exotic game', 'monster parts']

    choice = random.choice(mining)
    mining.remove(choice)
    common_resources.append(choice)
    common_resources.append(random.choice(mining))
    choice = random.choice(foraging)
    foraging.remove(choice)
    common_resources.append(choice)
    common_resources.append(random.choice(foraging))
    common_resources.append(random.choice(hunting))

    return common_resources
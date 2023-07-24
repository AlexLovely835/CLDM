import os

TOWN_TYPES = ['Hamlet', 'Village', 'Town', 'City', 'Metropolis']
TOWN_TYPE_NUM = {
    'Hamlet': 0,
    'Village': 1,
    'Town': 2,
    'City': 2, 
    'Metropolis': 3,
}
CLIMATES = ['Temperate', 'Tropical', 'Arid', 'Polar']
REGION_TYPES = ['Forest', 'River', 'Mountains', 'Plains', 'Hills', 'Swamps', 'Ocean', 'Desert', 'Jungle']
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
COMMODITY_RESOURCES = ['Marble', 'Weapons', 'Armor', 'Tools', 'Shoes', 'Clothes']
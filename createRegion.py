import argparse, random
from dice import rollDice
import region_attributes.generate_region_type as region_gen
import exports.exportRegion as exportRegion
from general_settings import *

class Region():

    def __init__(self, climate_arg, type_arg, town=None, export=False):
        
        if climate_arg:
            if climate_arg in CLIMATES:
                self.climate = climate_arg
            else:
                raise AttributeError('Incorrect climate')
        else:
            roll = rollDice('2d6')
            if roll > 5 and roll < 9:
                self.climate = 'Temperate'
            elif roll >= 9 and roll < 11:
                self.climate = 'Tropical'
            elif roll <= 5 and roll > 2:
                self.climate = 'Arid'
            else:
                self.climate = 'Polar'

        if type_arg:
            if type_arg in REGION_TYPES:
                self.type = type_arg
            else:
                raise AttributeError('Incorrect region type')
        else:
            if self.climate == 'Temperate':
                region_selection = ['Forest', 'River', 'Mountains',] #'Plains', 'Hills', 'Swamps', 'Ocean']
            elif self.climate == 'Tropical':
                region_selection = ['Jungle', 'River', 'Hills', 'Plains', 'Swamps', 'Ocean']

            elif self.climate == 'Arid':
                region_selection = ['River', 'Mountains', 'Desert', 'Plains', 'Ocean']
            else:
                region_selection = ['Forest', 'Mountains', 'Plains', 'Hills', 'Ocean']
            self.type = random.choice(region_selection)

        if town:
            self.town = town
        else:
            self.town = None

        region_gen.generateRegionType(self.type, self, self.town)

        if export:
            exportRegion.exportRegion(self)

    def __str__(self):
        return f'{self.description}'

 
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', dest='type', type=str, help='Choose region type')
    parser.add_argument('-c', dest='climate', type=str, help='Choose region climate.')
    parser.add_argument('-E', dest='export', default=False, action='store_true')
    args = parser.parse_args()
    print(Region(args.climate, args.type, export=args.export))
import random, argparse
from town_attributes.names import generateName
from town_attributes.demographics import generateTownProfessions
from general_settings import *
from dice import rollDice
import createRegion, createNPC
import exports.exportTown as exportTown

class Town():

    def __init__(self, name_arg, size_arg, climate_arg, export=False):
        if name_arg:
            self.name = name_arg
        else:
            self.name = generateName()

        if size_arg:
            if size_arg in TOWN_TYPES:
                self.size = size_arg
            else:
                raise AttributeError('Incorrect village size')
        else:
            self.size = random.choice(TOWN_TYPES)

        self.population = self.getPopulation()

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

        self.generateNearbyRegions(export)

        self.leader = createNPC.NPC(age_arg='adult', profession_arg='Leader', town_arg=self, export=export)

        self.npcs = []
        self.npcs.append(self.leader)

        generateTownProfessions(self)

        if export:
            exportTown.exportTown(self)

    def __str__(self):
        if len(self.regions) == 3:
            region_string = f"{self.name} lies between a {self.regions[0].partial_desc}, a {self.regions[1].partial_desc}, and a {self.regions[2].partial_desc}. "
        elif len(self.regions) == 2:
            region_string = f"{self.name} is placed between a {self.regions[0].partial_desc} and a {self.regions[1].partial_desc}. "
        else:
            region_string = f"{self.name} grew up on a {self.regions[0].partial_desc}. "
        return f"The {self.size} of {self.name} is in a {self.climate.lower()} area. " + region_string + f"\nPopulation: {self.population}"
    
    def getPopulation(self):
        if self.size == 'Hamlet':
            return random.randint(50, 200)
        elif self.size == 'Village':
            return random.randint(200, 1000)
        elif self.size == 'Town':
            return random.randint(1000, 5000)
        elif self.size == 'City':
            return random.randint(5000, 10000)
        elif self.size == 'Metropolis': 
            return random.randint(10000, 30000)
        else:
            return 0
        
    def generateNearbyRegions(self, export):
        self.regions = []
        region_number_roll = rollDice('2d6')
        if region_number_roll > 4 and region_number_roll < 10:
            region_number = 2
        elif region_number_roll >= 10:
            region_number = 3
        else:
            region_number = 1

        if self.climate == 'Temperate':
            region_selection = ['Forest', 'River', 'Mountains'] # 'Plains', 'Hills', 'Swamps', 'Ocean']
        elif self.climate == 'Tropical':
            region_selection = ['Jungle', 'River', 'Hills', 'Plains', 'Swamps', 'Ocean']

        elif self.climate == 'Arid':
            region_selection = ['River', 'Mountains', 'Desert', 'Plains', 'Ocean']
        else:
            region_selection = ['Forest', 'Mountains', 'Plains', 'Hills', 'Ocean']

        for _ in range(region_number):
            region = random.choice(region_selection)
            region_selection.remove(region)
            self.regions.append(createRegion.Region(self.climate, region, town=self, export=export))


    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', dest='name', type=str, help='Choose town name.')
    parser.add_argument('-s', dest='size', type=str, help='Choose town size.')
    parser.add_argument('-c', dest='climate', type=str, help='Choose town climate.')
    parser.add_argument('-E', dest='export', default=False, action='store_true')
    args = parser.parse_args()
    print(Town(args.name, args.size, args.climate, export=args.export))
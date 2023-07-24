import argparse
from general_settings import *
import buildings.tavern.tavern

def Building(type, town=None, export=False):
    if type == "Tavern":
        buildings.tavern.tavern.Tavern()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', dest='type', type=str, help='Choose the type of building.')
    parser.add_argument('-E', dest='export', default=False, action='store_true')
    args = parser.parse_args()
    print(Building(args.type, export=args.export))
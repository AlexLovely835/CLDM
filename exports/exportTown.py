from string import Template
from general_settings import ROOT_DIR
import os

def exportTown(town):
    replacements = {
        'name': town.name,
        'size': town.size,
        'climate': town.climate,
        'leader_name': f'{town.leader.first_name} {town.leader.last_name}'
    }

    if len(town.regions) == 3:
        region_string = f"{town.name} lies between a {town.regions[0].partial_desc}, a {town.regions[1].partial_desc}, and a {town.regions[2].partial_desc}. "
    elif len(town.regions) == 2:
        region_string = f"{town.name} is placed between a {town.regions[0].partial_desc} and a {town.regions[1].partial_desc}. "
    else:
        region_string = f"{town.name} grew up on a {town.regions[0].partial_desc}. "
    replacements['region_string'] = region_string
    
    if town.npcs:
        npc_list = [f'[[{x.first_name} {x.last_name}]]' for x in town.npcs]
        replacements['npcs'] = '\n- '.join(npc_list)
    
    if town.regions:
        region_list = [f'[[{x.name}]]' for x in town.regions]
        replacements['nearby'] = '\n- '.join(region_list)

    with open(os.path.join(ROOT_DIR, 'exports\\templates\\Town.md'), 'r') as file:
        src = Template(file.read())
        result = src.substitute(replacements)
        with open(os.path.join(ROOT_DIR, f'exported_files\\{town.name}.md'), 'w') as file2:
            file2.write(result)
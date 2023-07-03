from string import Template
from general_settings import ROOT_DIR
import os

def exportNPC(npc):
    replacements = {
        'first_name': npc.first_name,
        'last_name': npc.last_name,
        'age_desc': npc.age_desc,
        'race_name': npc.race['race_name'],
        'sex': npc.sex,
        'eye_desc': npc.eye_desc,
        'eye_color': npc.eye_color,
        'skin_color': npc.skin_color,
        'height_desc': npc.height_desc,
        'body_desc': npc.body_desc,
        'age': npc.age,
        'height': npc.height,
        'weight': npc.weight,
        'pronoun0_U': npc.pronouns[0].title(),
        'pronoun1': npc.pronouns[1],
        'pronoun2': npc.pronouns[2]
    }

    hair_string = ""
    beard_string =  ""
    if npc.beard:
        beard_string = f"with {npc.beard}. "
        hair_beard_bridge = " "
    else:
        hair_beard_bridge = ". "
    if npc.hair_style:
        if npc.hair_style == 'bald':
            hair_string = f"{npc.pronouns[0].title()} is bald" 
        elif npc.hair_style == 'balding':
            hair_string = f"{npc.pronouns[0].title()} has {npc.hair_color} hair and is balding"
        else:
            hair_string = f"{npc.pronouns[0].title()} has {npc.hair_color} hair in {npc.hair_style}"
    
    replacements['hair_string'] = hair_string
    replacements['beard_string'] = beard_string
    replacements['hair_beard_bridge'] = hair_beard_bridge

    if npc.town:
        replacements['town'] = f'#{npc.town.name}'
    else:
        replacements['town'] = ''

    if npc.profession == 'Leader':
        replacements['profession'] = f'Leader of [[{npc.town.name}]]'
    else:
        replacements['profession'] = npc.profession

    with open(os.path.join(ROOT_DIR, 'exports\\templates\\NPC.md'), 'r') as file:
        src = Template(file.read())
        result = src.substitute(replacements)
        if not os.path.isdir(os.path.join(ROOT_DIR, 'exported_files')):
            os.mkdir(os.path.join(ROOT_DIR, 'exported_files'))
        with open(os.path.join(ROOT_DIR, f'exported_files\\{npc.first_name} {npc.last_name}.md'), 'w') as file2:
            file2.write(result)


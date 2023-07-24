from string import Template
from general_settings import ROOT_DIR
import os

def exportRegion(region):
    replacements = {
        'name': region.name,
        'description': region.description,
    }

    if region.town:
        replacements['town'] = f'#{region.town.name}'
    else:
        replacements['town'] = ''

    with open(os.path.join(ROOT_DIR, 'exports\\templates\\Region.md'), 'r') as file:
        src = Template(file.read())
        result = src.substitute(replacements)
        if not os.path.isdir(os.path.join(ROOT_DIR, 'exported_files')):
            os.mkdir(os.path.join(ROOT_DIR, 'exported_files'))
        with open(os.path.join(ROOT_DIR, f'exported_files\\{region.name}.md'), 'w') as file2:
            file2.write(result)
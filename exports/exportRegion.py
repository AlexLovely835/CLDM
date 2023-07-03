from string import Template
from general_settings import ROOT_DIR
import os

def exportRegion(region):
    replacements = {
        'name': region.name,
        'description': region.description,
        'resources': '\n- '.join(region.resources),
    }

    if region.town:
        replacements['town'] = f'#{region.town.name}'
    else:
        replacements['town'] = ''

    with open(os.path.join(ROOT_DIR, 'exports\\templates\\Region.md'), 'r') as file:
        src = Template(file.read())
        result = src.substitute(replacements)
        with open(os.path.join(ROOT_DIR, f'exported_files\\{region.name}.md'), 'w') as file2:
            file2.write(result)
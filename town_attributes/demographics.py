
def generateTownProfessions(town):
    town.professions = {
        'mining': 0,
        'farming': 0,
        'fishing': 0,
        'foraging': 0,
        'woodcutting': 0,
        'hunting': 0
    }
    town.resources = []

    for region in town.regions:
        for key, value in region.supported_professions.items():
            town.professions[key] += value
        for resource in region.resources:
            town.resources.append(resource)

    
    
    
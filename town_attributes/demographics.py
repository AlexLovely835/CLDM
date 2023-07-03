
def generateTownProfessions(town):
    town.professions = {
        'mining': 0,
        'farming': 0,
        'fishing': 0,
        'foraging': 0,
        'woodcutting': 0,
        'hunting': 0
    }
    for key, value in town.regions.supported_professions.items():
        town.professions[key] += value
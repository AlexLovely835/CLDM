import region_attributes.forest as forest
import region_attributes.river as river
import region_attributes.mountain as mountain

def generateRegionType(type, region, town):
    if type == 'Forest':
        if town:
            region.name = forest.generateForestName(town)
        else:
            region.name = forest.generateForestName()
        region.description, region.partial_desc = forest.generateForestDesc(region.climate, region.name)
        region.supported_professions = forest.generateSupportedProfessions()    
    elif type == 'River':
        if town:
            region.name = river.generateRiverName(town)
        else:
            region.name = river.generateRiverName()
        region.description, region.partial_desc = river.generateRiverDesc(region.name)
        region.supported_professions = river.generateSupportedProfessions()
    elif type == 'Mountains':
        if town:
            region.name = mountain.generateMountainName(town)
        else:
            region.name = mountain.generateMountainName()
        region.description, region.partial_desc = mountain.generateMountainDesc(region.name)
        region.supported_professions = mountain.generateSupportedProfessions()
    else:
        raise TypeError('Region type', type, 'does not exist.')
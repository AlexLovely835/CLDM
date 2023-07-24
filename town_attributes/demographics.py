from general_settings import *
from town_attributes.professions import professions

def meetsRequirements(town, profession):
    for requirement in profession['requires']:
        if profession['natural_resource'] == True:
            if town.natural_resources[requirement] < 1:
                return False
        else:
            if town.goods[requirement] < 1:
                return False
    return True

def hasAllEssentialBusinesses(town):
    essential = getProfessionsByTag('Essential', professions=getAvailableProfessions(town))
    for profession in essential:
        if town.professions[profession['name']] < 1:
            return False
    return True

def hasEntertainmentVenue(town):
    entertainment = getProfessionsByTag('Entertainment', professions=getAvailableProfessions(town))
    for profession in entertainment:
        if town.professions[profession['name']] < 1:
            return False
    return True

def getAvailableProfessions(town):
    profession_list = []
    town_size = TOWN_TYPE_NUM[town.size]
    for profession in professions:
        if profession['minimum_town'] >= town_size:
            profession_list.append(profession)
    return profession_list

def getProfessionsByTag(tag, professions=professions):
    profession_list = []
    for profession in professions:
        if profession['tag'] == tag:
            profession_list.append(profession)
    return profession_list

def getPrereqProfessions(target, professions=professions):
    profession_list = []
    for profession in professions:
        for resource in profession['resource_production']:
            if resource in target['requires']:
                profession_list.append(profession)
    return profession_list

def getProfessionsByRequirements(requirement, professions=professions):
    profession_list = []
    for profession in professions:
        if requirement in profession['requires']:
            profession_list.append(profession)
    return profession_list

def howCloseToMaxInput(town, profession):
    return (town.professions[profession['name']] *  profession['input_capacity']) - profession['input_count']

def maximumResourceUse(town, profession):
    max_use = float('inf')
    for requirement in profession['requires']:
        max_input = howCloseToMaxInput(town, profession)
        if max_input == 0:
            return 0
        if profession['natural_resource']:
            if town.natural_resources[requirement] >= max_input:
                max_use = max_input
        else:
            if town.goods[requirement] >= max_input:
                if max_use > max_input:
                    max_use = max_input
            else:
                if max_use > town.goods[requirement]:
                    max_use = town.goods[requirement]
    return max_use

def distributeResources(town, resource):
    resource_inputs = getProfessionsByRequirements(resource, getAvailableProfessions(town))
    for profession in resource_inputs:
        if meetsRequirements(town, profession):
            max_use = maximumResourceUse(town, profession)
            if max_use > 0:
                print('Giving', max_use, resource, 'to', profession['name'])
            else:
                print('Need more', profession['name'], 'to use', resource)
            for requirement in profession['requires']:
                town.goods[requirement] -= max_use
            profession['input_count'] += max_use
            for resourc in profession['resource_production']:
                town.goods[resourc] += max_use * profession['export_multiplier']
                distributeResources(town, resourc)

def assignProfession(town, profession):
    town.professions[profession['name']] += 1
    max_use = maximumResourceUse(town, profession)
    for requirement in profession['requires']:
        if profession['natural_resource']:
            town.natural_resources[requirement] -= max_use
        else:
            town.goods[requirement] -= max_use
    profession['input_count'] += max_use
    for resource in profession['resource_production']:
        town.goods[resource] += max_use * profession['export_multiplier']
        distributeResources(town, resource)

def determineProfessionToAssign(town, current_professions):
    print('Finding a profession to assign...')
    for profession in current_professions:
        if meetsRequirements(town, profession):
            print(f"Townperson assigned to {profession['name']}")
            assignProfession(town, profession)
            return False
    return True

def checkPrereqs(town, profession):
    prereq = getPrereqProfessions(profession)
    if len(prereq) == 0:
        return profession
    elif prereq[0]['natural_resource']:
        return profession
    
    elif meetsRequirements(town, prereq[0]):
        return prereq[0]
    else:
        return checkPrereqs(town, prereq[0])  

def beginTradeSequence(town, resource, quantity_needed=1):
    available_professions = getAvailableProfessions(town)
    print(f'Trading for essential resource: {resource}')
    for trade_goods in COMMODITY_RESOURCES:
        for i in range(town.goods[trade_goods]):
            if town.goods['Trade_Units'] == quantity_needed:
                town.goods['Trade_Units'] = 0
                town.goods[resource] = quantity_needed
                if resource not in town.imports:
                    town.imports.append(resource)
                if trade_goods not in town.exports:
                    town.exports.append(trade_goods)
                handleProfessionLoop(town, available_professions)
                return
            else:
                town.goods[trade_goods] -= 1
                town.goods['Trade_Units'] += 1
    
    town.goods[resource] += town.goods['Trade_Units']
    quantity_needed -= town.goods['Trade_Units']
    town.goods['Trade_Units'] = 0

    print('Attempting to produce commodities to trade.')
    current_professions = getProfessionsByTag('Commodity', available_professions)
    for profession in current_professions:
        if town.professions[profession['name']] < 1:
            if meetsRequirements(town, profession):
                determineProfessionToAssign(town, [profession])
                return
            else:
                prereq = checkPrereqs(town, profession)
                if meetsRequirements(town, prereq):
                    determineProfessionToAssign(town, [prereq])
                    return
                else:
                    continue
    
    for profession in available_professions:
        if profession['natural_resource']:
            if meetsRequirements(town, profession):
                determineProfessionToAssign(town, [profession])
                return
            
    unemployed = getProfessionsByTag('Unemployed')
    determineProfessionToAssign(town, unemployed)
    
def handleProfessionLoop(town, available_professions):
    if town.goods['Food'] < town.population:
        print('Food too low:', town.goods['Food'], 'out of', town.population, 'needed.')
        current_professions = getProfessionsByTag('Food', available_professions)
        need_trade = determineProfessionToAssign(town, current_professions)
        if need_trade:
            beginTradeSequence(town, 'Food', (town.population - town.goods['Food']))
    elif not hasAllEssentialBusinesses(town):
        print('Missing essential businesses.')
        current_professions = getProfessionsByTag('Essential', available_professions)
        for profession in current_professions:
            if town.professions[profession['name']] < 1:
                if meetsRequirements(town, profession):
                    determineProfessionToAssign(town, [profession])
                    break
                else:
                    prereq = checkPrereqs(town, profession)
                    if meetsRequirements(town, prereq):
                        determineProfessionToAssign(town, [prereq])
                    else:
                        beginTradeSequence(town, prereq['requires'][0])
                        break
    elif not hasEntertainmentVenue(town):
        print('Missing entertainment businesses.')
        current_professions = getProfessionsByTag('Entertainment', available_professions)
        for profession in current_professions:
            if town.professions[profession['name']] < 1:
                if meetsRequirements(town, profession):
                    determineProfessionToAssign(town, [profession])
                    break
                else:
                    prereq = checkPrereqs(town, profession)
                    if meetsRequirements(town, prereq):
                        determineProfessionToAssign(town, [prereq])
                    else:
                        beginTradeSequence(town, prereq['requires'][0])
                        break
    else:
        print('Using up resources and adding random jobs.')
        current_professions = available_professions
        determineProfessionToAssign(town, current_professions)


def generateTownProfessions(town):
    for profession in professions:
        profession['input_count'] = 0
    town.natural_resources = {
        'mining': 0,
        'farming': 0,
        'fishing': 0,
        'foraging': 0,
        'woodcutting': 0,
        'hunting': 0
    }
    town.goods = {
        'Food': 0,
        'Livestock': 0,
        'Grain': 0,
        'Cotton': 0,
        'Furs': 0,
        'Meats': 0,
        'Fish': 0,
        'Lumber': 0,
        'Herbs': 0,
        'Iron Ore': 0,
        'Gold Ore': 0,
        'Stone': 0,
        'Marble': 0,
        'Hide': 0, 
        'Alcohol': 0, 
        'Smelted Iron': 0,
        'Weapons': 0,
        'Armor': 0,
        'Tools': 0,
        'Leather': 0, 
        'Shoes': 0,
        'Clothes': 0, 
        'Flour': 0,
        'Trade_Units': 0,
    }
    town.imports = []
    town.exports = []
    town.professions = {
        'Farmer': 0, 
        'Hunter': 0, 
        'Fisherman': 0, 
        'Lumberjack': 0,
        'Forager': 0,
        'Miner': 0,
        'Butcher': 0,
        'Fishmonger': 0,
        'Carpenter': 0, 
        'Baker': 0,
        'Innkeeper': 0,
        'Refiner': 0,
        'Blacksmith': 0,
        'Tanner': 0,
        'Cobbler': 0,
        'Furrier': 0,
        'Leatherworker': 0,
        'Clothier': 0,
        'Miller': 0,
        'Shopkeep': 0,
        'Peddler': 0,
        'Midwife': 0,
        'Unemployed': 0,
    }

    print('Defining natural resources...')
    for region in town.regions:
        for key, value in region.supported_professions.items():
            town.natural_resources[key] += value
    for key, value in town.natural_resources.items():
        print(key, value)

    available_professions = getAvailableProfessions(town)

    for _ in range(town.population):
        handleProfessionLoop(town, available_professions)
        if town.goods['Food'] < town.population and town.goods['Meats'] > 0:
            if (town.population - town.goods['Food']) >= town.goods['Meats']:
                town.goods['Food'] += town.goods['Meats']
                town.goods['Meats'] = 0
            else:
                town.goods['Meats'] -= (town.population - town.goods['Food'])
                town.goods['Food'] = town.population

    print('Final demographics:')
    print(town.population)
    for key, value in town.professions.items():
        if value > 0:
            print(key, value)
    print('Food:', town.goods['Food'])
    print('Imports:', town.imports)
    print('Exports:', town.exports)

            
                
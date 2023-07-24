import random

adjectives = ['Ebony', 'Shiny', 'Eternal', 'Fiery', 'Glowing', 'Iron', 'Gold', 'Bronze', 'Silver', 'Golden', 'Black', 'Bold', 'Bright']
nouns = ['Ingot', 'Hammer', 'Anvil', 'Forge', 'Sword', 'Edge',]
family_addition = ['and Sons', 'and Daughter', 'and Co.']
end = ['Blacksmith', 'Armory', 'Ironworks', 'Smithing', 'Metalworks', 'Forging']

def generateBlacksmithName(family_name = None):
    type = random.random()
    if type > 0.6:
        return f'The {random.choice(adjectives)} {random.choice(nouns)} {random.choice(end)}'
    elif type > 0.2:
        return f'The {random.choice(adjectives)} {random.choice(nouns)}'
    else:
        if family_name == None:
            choice1 = random.choice(nouns)
            nouns.remove(choice1)
            return f'The {random.choice(nouns)} and {choice1} {random.choice(end)}'
        else:
            return f'{random.choice(adjectives)} {random.choice(family_addition)}'
    
if __name__ == '__main__':
    print(generateBlacksmithName())
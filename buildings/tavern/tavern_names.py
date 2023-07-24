import random

nouns = ['Titan', 'God', 'Mug', 'Sword', 'Ostrich', 'Badger', 'Cat', 'Dog', 'Bear', 'Goblin', 'Elf', 'Dwarf', 'Dancer', 'Fighter', 'Rose', 'Coin', 'Goblet', 'Hat', 'Helm', 'Axe', 
         'Armor', 'Apple', 'Ogre', 'Giant', 'Griffon', 'Wolf', 'Kobold', 'Dragon', 'Castle', 'Kingdom', 'Cow', 'Chicken', 'Owl', 'Book', 'Scribe', 'King', 'Queen', 'Prince', 
         'Princess', 'Chest', 'Barrel', 'Flame', 'Ghost', 'Vampire', 'Skull', 'Tree', 'Leaf', 'Mountain', 'Ship', 'Flagon', 'Plate', 'Dagger', 'Staff', 'Book', 'Scroll', 'Map',
         'Spoon', 'Fork', 'Greaves', 'Room', 'Bottle', 'Lotus', 'Pirate', 'Bunny', 'Eyes', 'Grin', 'Saint', 'Priest', 'Unicorn', 'Pony', 'Prophet', 'Lover', 'Tinker', 'Gauntlet', 
         'Boot', 'Feather', 'Tome', 'Bat', 'Sprite', 'Bird', 'Eagle', 'Boar', 'Toad', 'Goat', 'Hound', 'Lizard', 'Spear', 'Bow', 'Bandit', 'Rat', 'Mouse', 'Snake', 'Ladle', 'Chalice', 
         'Treasure', 'Shadow', 'Friend', 'Belly']
verbs = ['Dancing', 'Prancing', 'Running', 'Laughing', 'Fighting', 'Crying', 'Talking', 'Shouting', 'Sleeping', 'Flying', 'Complaining', 'Singing', 'Snoring', 'Flaming',
            'Howling', 'Roaring','Stinging', 'Shaking', 'Swinging', 'Swearing']

adjectives = ['Tipsy', 'Royal', 'Crooked', 'Crimson', 'White', 'Gray', 'Black', 'Jolly', 'Happy', 'Wild', 'Mighty', 'Crazy', 'Tired', 'Angry', 'Cold', 'Puzzled', 'Silent', 
                'Graceful', 'Brass', 'Sour', 'Lively', 'Flashy', 'Honorable', 'Dizzy', 'Rusty', 'Dented', 'Wobbly', 'Drunken', 'Silly', 'Greasy', 'Wise', 'Broken', 'Righteous',
                'Green', 'Yellow', 'Blue', 'Red', 'Sad', 'Short', 'Pleasant', 'Quaint', 'Arcane', 'Thirsty', 'Lone', 'Holy', 'Surly', 'Boozy', 'Dead', 'Last', 'Blind', 'Great', 
                'Shiny', 'Scarlet', 'Golden', 'Silver', 'Bronze', 'Old', 'Pale', 'Bitter', 'Dark', 'Bloody', 'Lusty']

def generateTavernName():
    type = random.random()
    if type > 0.7:
        return f'The {random.choice(verbs)} {random.choice(nouns)}'
    elif type > 0.3:
        return f'The {random.choice(adjectives)} {random.choice(nouns)}'
    else:
        return f'The {random.choice(nouns)} and the {random.choice(nouns)}'
    
if __name__ == '__main__':
    print(generateTavernName())
human = {
    'race_name': 'human',
    'neutral_names': ['Sam', 'Jordan'],
    'last_names': ['Smith', 'Jackson'],
    'sex_traits': {
        'female': {
            'names': ['Anna', 'Jade', 'Lana'],
            'pronouns': ['she', 'her', 'hers'],
            'beard_chance': 0,
            'base_weight': 100,
            'weight_roll': '2d4',
            'base_height': 52,
            'height_roll': '2d10',
            'hair_styles': ['a crew cut', 'a buzz cut', 'bald', 'a bob cut', 'a pixie cut', 'a pageboy haircut', 'a bouffant haircut', 'a bun', 'a crown braid', 'a curtained style', 'a long feathered style', 'an afro', 'a french braid', 'a french twist', 'a ponytail'],
        },
        'male': {
            'names': ['Adam', 'Jack', 'Lucas'],
            'pronouns': ['he', 'him', 'his'],
            'beard_chance': 35,
            'base_weight': 110,
            'weight_roll': '2d4',
            'base_height': 56,
            'height_roll': '2d10',
            'hair_styles': ['a crew cut', 'a buzz cut', 'balding', 'a pageboy haircut', 'a bun', 'a comb over', 'a curtained style', 'a mop-top style', 'a slicked-back style', 'an afro', 'a ponytail', 'a pompadour style'],
        },
    },
    'age_traits': {
        'descriptions': {
            90: 'an extremely elderly',
            70: 'an elderly',
            60: 'an old',
            46: 'a middle aged',
            38: 'a settled adult',
            30: 'a prime aged',
            20: 'a young adult',
            18: 'a late teenager',
            15: 'a teenaged',
            13: 'a young teenaged',
            10: 'an adolescent',
            6: 'a young',
            0: 'a very young',
        },
        'elder': {
            'starting_age': 70,
            'max_age': 120,
        },
        'adult': {
            'starting_age': 35,
            'max_age': 69,
        },
        'young_adult': {
            'starting_age': 18,
            'max_age': 34,
        },
        'child': {
            'starting_age': 6,
            'max_age': 17,
        },
    },
    'appearance_traits': {
        'hair': True,
        'eye_descriptions': ['shining', 'dull', 'shifty', 'bright', 'calm', 'droopy', '', 'piercing', 'sharp', 'big'],
        'eye_colors': ['dark brown', 'brown', 'amber', 'hazel', 'green', 'green-hazel', 'blue-hazel', 'gray', 'blue-gray', 'light blue', 'blue-green', 'dark blue'],
        'hair_colors': ['ash blonde', 'blonde', 'golden blonde', 'bleach blonde', 'strawberry blonde', 'butterscotch', 'light brown', 'light golden brown', 'dark brown', 'dark golden brown', 'light auburn', 'medium auburn', 'jet black', 'light blonde', 'chesnut brown', 'red', 'ginger', 'copper', 'medium brown', 'chesnut brown'],
        'elder_hair_colors': ['light gray', 'dark gray', 'white', 'salt and pepper'],
        'skin_colors': ['ivory', 'beige', 'alabaster', 'honey', 'tan', 'caramel', 'bronze', 'mahogany', 'chesnut', 'medium brown', 'pale', 'espresso brown', 'porcelain', 'almond', 'golden', 'pink', 'fair', 'light'],
        'beard': ['a chevron moustache', 'a pyramid moustache', 'a lampshade moustache', 'a goatee', 'a soul patch', 'stubble', 'mutton chops', 'a circle beard', 'sideburns', 'sidewhiskers', 'a bushy beard', 'a full beard', 'a braided beard', 'an unkempt beard'],
        'height_descriptions': {
            76: 'freakishly tall',
            72: 'very tall',
            69: 'tall',
            65: 'of average height',
            62: 'mildly short',
            59: 'short',
            54: 'very short',
        }
    }
}

races = [human]
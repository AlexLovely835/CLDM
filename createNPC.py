import argparse, random
import npc_attributes.races as races
import exports.exportNPC as NPCExport
from dice import rollDice

class NPC():

    def __init__(self, race_arg=None, sex_arg=None, age_arg=None, profession_arg=None, town_arg=None, export=False):
        if not race_arg:
            self.race = random.choice(races.races)
        else:
            self.race = self.getRace(args.race)

        if not sex_arg:
            self.sex = random.choice(['male', 'female'])
        else:
            if sex_arg in ['male', 'female']:
                self.sex = sex_arg
            else:
                raise AttributeError('Given attribute for sex is not acceptable.')
        
        self.pronouns = self.race['sex_traits'][self.sex]['pronouns']
    
        self.first_name, self.last_name = self.getName()

        if not age_arg:
            self.age = random.randint(0, 100)
        else:
            self.age = random.randint(self.race['age_traits'][age_arg]['starting_age'], self.race['age_traits'][age_arg]['max_age'])

        self.age_desc = self.getAgeDesc()

        if not profession_arg:
            self.profession = 'Peasant'
        else:
            self.profession = profession_arg

        if town_arg:
            self.town = town_arg
        else:
            self.town = None

        self.eye_color = random.choice(self.race['appearance_traits']['eye_colors'])
        self.eye_desc = random.choice(self.race['appearance_traits']['eye_descriptions'])
        self.skin_color = random.choice(self.race['appearance_traits']['skin_colors'])

        height_mod = rollDice(self.race['sex_traits'][self.sex]['height_roll'])
        self.height = self.race['sex_traits'][self.sex]['base_height'] + height_mod
        weight_mod = rollDice(self.race['sex_traits'][self.sex]['weight_roll'])
        self.weight = self.race['sex_traits'][self.sex]['base_weight'] + (height_mod * weight_mod)

        self.strength = rollDice('3d6')

        self.height_desc = self.getHeightDesc()
        self.body_desc = self.getBodyDesc(weight_mod * height_mod)

        if self.race['appearance_traits']['hair']:
            if self.age >= self.race['age_traits']['elder']['starting_age']:
                if random.random() >= 0.3:
                    self.hair_color = random.choice(self.race['appearance_traits']['elder_hair_colors'])
                else:
                    self.hair_color  = random.choice(self.race['appearance_traits']['hair_colors'])
            else:
                self.hair_color  = random.choice(self.race['appearance_traits']['hair_colors'])

            self.hair_style = random.choice(self.race['sex_traits'][self.sex]['hair_styles'])
        else:
            self.hair_color  = None
            self.hair_style = None
        
        if self.race['sex_traits'][self.sex]['beard_chance'] >= random.randint(1, 100) and self.age > self.race['age_traits']['child']['max_age']:
            self.beard = random.choice(self.race['appearance_traits']['beard'])
        else:
            self.beard = None
        
        if export:
            NPCExport.exportNPC(self)

    def __str__(self):
        hair_string = ""
        beard_string =  ""
        if self.beard:
            beard_string = f"with {self.beard}. "
            hair_beard_bridge = " "
        else:
            hair_beard_bridge = ". "
        if self.hair_style:
            if self.hair_style == 'bald':
                hair_string = f"{self.pronouns[0].title()} is bald" 
            elif self.hair_style == 'balding':
                hair_string = f"{self.pronouns[0].title()} has {self.hair_color} hair and is balding"
            else:
                hair_string = f"{self.pronouns[0].title()} has {self.hair_color} hair in {self.hair_style}"
        
        return f"{self.first_name} {self.last_name} is {self.age_desc} {self.race['race_name']} {self.sex} that has {self.eye_desc} {self.eye_color} eyes and {self.skin_color} skin. {self.pronouns[0].title()} is {self.height_desc} and has {self.body_desc} build. " + hair_string + hair_beard_bridge + beard_string + f"\nAge: {self.age}" + f"\nHeight: {self.height} inches" + f"\nWeight: {self.weight} pounds"
    
    def getRace(self, race):
        for object in races.races:
            if object['race_name'] == race:
                return object

    def getName(self):
        first_name = random.choice(self.race['sex_traits'][self.sex]['names'] + self.race['neutral_names'])
        last_name = random.choice(self.race['last_names'])
        return first_name, last_name

    def getAgeDesc(self):
        for age_milestone, description in self.race['age_traits']['descriptions'].items():
            if self.age >= age_milestone:
                return description
            
    def getHeightDesc(self):
        for height, description in self.race['appearance_traits']['height_descriptions'].items():
            if self.height >= height:
                return description
            
    def getBodyDesc(self, weight_bonus):
        if self.strength > 13:
            if weight_bonus > 120:
                return random.choice(['a bulky', 'a beefy'])
            elif weight_bonus > 80:
                return random.choice(['a durable'])
            elif weight_bonus > 41:
                return random.choice(['a ripped'])
            else:
                return random.choice(['a toned', 'a lean'])
        elif self.strength > 8:
            if weight_bonus > 120:
                return random.choice(['a sturdy'])
            elif weight_bonus > 80:
                return random.choice(['a stout'])
            elif weight_bonus > 41:
                return random.choice(['an average'])
            else:
                return random.choice(['a slim', 'a wiry'])
        else:
            if weight_bonus > 120:
                return random.choice(['a heavy-set'])
            elif weight_bonus > 80:
                return random.choice(['a pudgy'])
            elif weight_bonus > 41:
                return random.choice(['a skinny', 'a dainty'])
            else:
                return random.choice(['a slender', 'a skinny', 'lanky'])
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', dest='race', type=str, help='Choose character race.')
    parser.add_argument('-s', dest='sex', type=str, help='Choose character sex.')
    parser.add_argument('-a', dest='age', type=str, help='Choose character age.')
    parser.add_argument('-p', dest='profession', type=str, help='Choose character profession')
    parser.add_argument('-E', dest='export', default=False, action='store_true')
    args = parser.parse_args()
    print(NPC(race_arg=args.race, sex_arg=args.sex, age_arg=args.age, profession_arg=args.profession, export=args.export))
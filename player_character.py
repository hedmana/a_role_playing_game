import random


class PlayerCharacter:

    ABILITIES = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

    SKILLS_TO_ABILITIES = {"Acrobatics" : "Dexterity", "Animal Handling" : "Wisdom", "Arcana" : "Intelligence",
                           "Athletics" : "Strength", "Deception" : "Charisma", "History" : "Intelligence",
                           "Insight" : "Wisdom", "Intimidation" : "Charisma", "Investigation" : "Intelligence",
                           "Medicine" : "Wisdom", "Nature" : "Intelligence", "Perception" : "Wisdom",
                           "Performance" : "Charisma", "Persuasion" : "Charisma", "Religion" : "Intelligence",
                           "Sleight of Hand" : "Dexterity", "Stealth" : "Dexterity", "Survival" : "Wisdom"}

    ABILITY_SCORES_TO_MODIFIERS = {1 : -5, 2 : -4, 3 : -4, 4 : -3, 5 : -3, 6 : -2, 7 : -2, 8 : -1, 9 : -1, 10 : 0,
                                   11 : 0, 12 : 1, 13 : 1, 14 : 2, 15 : 2, 16 : 3, 17 : 3, 18 : 4, 19 : 4, 20 : 5}

    def __init__(self, character_name, race, character_class, hit_die, armor_class):
        self.__name = character_name
        self.__race = race
        self.__class = character_class
        self.__hit_die = hit_die
        self.__armor_class = armor_class
        self.__level = 1
        self.__ability_scores = {}
        for i in PlayerCharacter.ABILITIES:
            self.__ability_scores[i] = PlayerCharacter.roll_ability_score()
        modifier = self.__ability_scores["Constitution"]
        self.__max_hp = PlayerCharacter.ABILITY_SCORES_TO_MODIFIERS[modifier] + self.__hit_die
        self.__hp = PlayerCharacter.ABILITY_SCORES_TO_MODIFIERS[modifier] + self.__hit_die

    def get_name(self):
        return self.__name

    def get_race(self):
        return self.__race

    def get_class(self):
        return self.__class

    def get_level(self):
        return self.__level

    def is_downed(self):
        if self.__hp == 0:
            return True
        else:
            return False

    def get_ability_modifier(self, ability):
        if ability in self.__ability_scores:
            score = self.__ability_scores[ability]
            modifier = PlayerCharacter.ABILITY_SCORES_TO_MODIFIERS[score]
            return modifier
        else:
            return None

    def get_skill_level(self, skill):
        if skill in PlayerCharacter.SKILLS_TO_ABILITIES:
            ability = PlayerCharacter.SKILLS_TO_ABILITIES[skill]
            skill_lvl = PlayerCharacter.get_ability_modifier(self, ability)
            return skill_lvl
        else:
            return None

    def skill_check(self, skill, result_to_pass):
        if skill in PlayerCharacter.SKILLS_TO_ABILITIES:
            die_score = PlayerCharacter.roll_die(20)
            skill_lvl = PlayerCharacter.get_skill_level(self, skill)
            check = die_score + skill_lvl
            if check >= result_to_pass:
                return True
            else:
                return False
        else:
            return None

    def level_up(self):
        die_score = PlayerCharacter.roll_die(self.__hit_die)
        self.__hp += die_score
        self.__max_hp += die_score
        self.__level += 1
        return die_score

    def attack(self, other_character):
        die_score = PlayerCharacter.roll_die(20)
        damage = 0
        if die_score >= other_character.__armor_class:
            roll = 0
            if self.__class == "Fighter":
                roll = 6
            elif self.__class == "Ranger":
                roll = 8
            elif self.__class == "Wizard":
                roll = 10
            elif self.__class == "Rogue":
                roll = 4

            damage = PlayerCharacter.roll_die(roll)
            if other_character.__hp < damage:
                damage = other_character.__hp
                other_character.__hp = 0
            else:
                other_character.__hp -= damage
        return damage

    def heal(self):
        heal = random.randint(1, 5)
        if self.__hp + heal > self.__max_hp:
            heal1 = heal - ((self.__hp + heal) - self.__max_hp)
            self.__hp += heal1
            return heal1
        else:
            self.__hp += heal
            return heal

    def __str__(self):
        string = "{:s}, a level {:d} {:s} {:s}\nHP: {:d}/{:d}\n".format(self.__name, self.__level, self.__race, self.__class, self.__hp, self.__max_hp)
        for i in PlayerCharacter.ABILITIES:
            s = i[0:3]
            s = s.upper()
            add = "{:s}:{:>3}   ".format(s, self.__ability_scores[i])
            string += add
        return string

    @staticmethod
    def roll_die(die_sides):
        return random.randint(1, die_sides)

    @staticmethod
    def roll_ability_score():
        roll_results = [PlayerCharacter.roll_die(6) for i in range(4)]  # throwing 4 6-sided dies
        smallest = 1000  # just some very large value
        for result in roll_results:  # choosing 3 largest results
            if result < smallest:
                smallest = result
        roll_results.remove(smallest)  # removing smallest result
        roll_sum = sum(roll_results)  # adding 3 largest results
        return roll_sum

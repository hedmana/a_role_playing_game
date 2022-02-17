from player_character import PlayerCharacter
import random


def input_int(text, low_lim, high_lim):
    number = low_lim - 1
    while not low_lim <= number <= high_lim:
        try:
            number = int(input(text))
        except ValueError:
            print("Enter an integer between {:d} - {:d}!".format(low_lim, high_lim))
    return number


class DungeonsAndDragonsTestingProgram:

    def __init__(self):
        self.__characters = []

    def choose_character(self):
        char_list = self.__characters
        for i in range(len(char_list)):
            print("{:d}. {:s}, a level {:d} {:s} {:s}".format(i + 1, char_list[i].get_name(), char_list[i].get_level(),
                                                              char_list[i].get_race(), char_list[i].get_class()))
        choice = input_int("Choose character number: ", 1, len(char_list))
        return self.__characters[choice - 1]

    def add_unit(self):
        print("Creating a new character.")
        char_name = input("Name: ")
        char_race = input("Race: ")
        char_class = input("Class: ")
        hit_die = input_int("Hit die: ", 4, 10)
        armor_class = input_int("Armor class: ", 1, 20)
        new_char = PlayerCharacter(char_name, char_race, char_class, hit_die, armor_class)
        self.__characters.append(new_char)
        print("New character created.")

    def skill_check(self):
        print("Choose a character to perform the skill check with:")
        character = self.choose_character()
        skill = input("Enter a skill to perform the skill check with: ")
        result_to_pass = input_int("Enter a result to pass: ", 1, 20)
        success = character.skill_check(skill, result_to_pass)
        if success is None:
            print("No such skill as '{:s}'.".format(skill))
        else:
            if success:
                print("{:s} passes the skill check.".format(character.get_name()))
            else:
                print("{:s} fails the skill check.".format(character.get_name()))

    def attack(self):
        print("Choose the character to attack:")
        character_attacking = self.choose_character()
        print("Choose the character to be attacked:")
        character_attacked = self.choose_character()
        damage = character_attacking.attack(character_attacked)
        if damage > 0:
            print("{:s} hits and does {:d} damage.".format(character_attacking.get_name(), damage))
        else:
            print("{:s} misses.".format(character_attacking.get_name()))

    def heal(self):
        print("Choose the character to heal:")
        character_to_heal = self.choose_character()
        healed = character_to_heal.heal()
        print("{:s} healed for {:d} hit points.".format(character_to_heal.get_name(), healed))

    def level_up(self):
        print("Choose the character to level up:")
        character = self.choose_character()
        character.level_up()
        print("Character leveled up.")

    def print_statuses(self):
        for character in self.__characters:
            print(character)
            print()

    def print_object_fields_and_skills(self):
        print("Choose a character:")
        character = self.choose_character()
        fields_dict = character.__dict__
        for field in fields_dict:
            print("{:40}: {}".format(field, fields_dict[field]))


def main():
    print("This is a testing program to test and debug your class.")
    seed = int(input("Enter a seed for the random generator:\n"))
    random.seed(seed)
    tester = DungeonsAndDragonsTestingProgram()
    actions = {"N" : tester.add_unit,
               "S" : tester.skill_check,
               "A" : tester.attack,
               "H" : tester.heal,
               "L" : tester.level_up,
               "P" : tester.print_statuses,
               "X" : tester.print_object_fields_and_skills
               }
    cont = True
    while cont:
        print()
        print("Actions:\n"
              "N - Create a new character\n"
              "S - Skill check\n"
              "A - Attack against another character\n"
              "H - Heal\n"
              "L - Level up\n"
              "P - Print character statuses\n"
              "Debugging:\n"
              "X - Print object fields and skill levels in raw data form\n"
              "Other:\n"
              "Q - Quit")
        choice = input().upper()
        if choice == "Q":
            cont = False
            print("Quitting program.")
        else:
            try:
                actions[choice]()
            except KeyError:
                print("Invalid choice, try again.")


main()

import random
from player_character import PlayerCharacter


def main():
    random.seed(311)
    ranger = PlayerCharacter("Indis Amakiir", "Elf", "Ranger", 10, 12)
    wizard = PlayerCharacter("Vyncent", "Human", "Wizard", 6, 10)
    rogue = PlayerCharacter("Ellen Merdaye", "Halfling", "Rogue", 8, 11)
    print("Three adventurers enter a tavern. Press enter to continue the story.")
    input()
    print("Initial situation:")
    print(ranger)
    print()
    print(wizard)
    print()
    print(rogue)
    input()
    print("{:s} and {:s} go and grab drinks."
          .format(ranger.get_name(), wizard.get_name()))
    print("{:s} sees a stranger with a deck of cards and asks to play a game with him.".format(rogue.get_name()))
    fighter = PlayerCharacter("Akchar", "Tiefling", "Fighter", 10, 14)
    print("{:s} the {:s} accepts the request.".format(fighter.get_name(), fighter.get_race()))

    print("Since {:s} is a {:s}, she tries a Deception check to fool the stranger."
          .format(rogue.get_name(), rogue.get_class()))
    input()
    success = rogue.skill_check("Deception", 12)
    if success:
        print("It succeeds! The stranger notices nothing while {:s} arranges the playing cards a little more to her "
              "favour.".format(rogue.get_name()))
        print("However, as {:s} is leaving the table, {:s} notices something is wrong!"
              .format(rogue.get_name(), fighter.get_name()))
    else:
        print("It fails. The stranger notices {:s}'s attempt at deceiving him and loses him temper."
              .format(rogue.get_name()))

    input()
    print("{:s} and {:s} hear a commotion and see the stranger telling their friend off."
          .format(ranger.get_name(), wizard.get_name()))

    print("{:s} decides to talk to the stranger to calm him down. In order to do this, he tries a Persuasion check."
          .format(wizard.get_name()))
    success = wizard.skill_check("Persuasion", 18)
    input()
    if success:
        print("It succeeds! {:s} calms down.".format(fighter.get_name()))
    else:
        print("It fails. {:s} is not interested in {:s}'s words at all. Instead, he takes out his weapon, "
              "a sharp shortsword.".format(fighter.get_name(), wizard.get_name()))

        input()
        print("{:s} acts quickly. Her hands find the arrow in her quiver and draw her bow before anyone else "
              "realizes what is going on.".format(ranger.get_name()))
        damage = ranger.attack(fighter)
        if damage > 0:
            print("She does {:d} points of damage to {:s}, who looks shaken by the quick attack."
                  .format(damage, fighter.get_name()))
        else:
            print("Her arrow misses and hits the wall behind {:s}!".format(fighter.get_name()))
        if fighter.is_downed():
            print("{:s} the {:s} falls to the ground unconscious.".format(fighter.get_name(), fighter.get_race()))

        else:
            input()
            print("{:s} realizes too that this situation cannot be resolved with words, "
                  "and prepares a fireball to attack.".format(wizard.get_name()))
            damage = wizard.attack(fighter)
            if damage > 0:
                print("The fireball finds its target, doing {:d} points of damage.".format(damage))
            else:
                print("The fireball misses and and lits a table on fire!")
            if fighter.is_downed():
                print("{:s} the {:s} falls to the ground unconscious.".format(fighter.get_name(), fighter.get_race()))

            else:
                input()
                print("{:s} is furious and targets {:s} with his sword!".format(fighter.get_name(), rogue.get_name()))
                damage = fighter.attack(rogue)
                if damage > 0:
                    print("{:s} hits {:s} with the sword, doing {:d} points of damage."
                          .format(fighter.get_name(), rogue.get_name(), damage))
                else:
                    print("Luckily, he misses.")
                if rogue.is_downed():
                    print("{:s} falls to the ground unconscious.".format(rogue.get_name()))

                else:
                    input()
                    print("{:s} attacks back, drawing her dagger!".format(rogue.get_name()))
                    damage = rogue.attack(fighter)
                    if damage > 0:
                        print("{:s}'s dagger finds its target, doing {:d} points of damage."
                              .format(rogue.get_name(), damage))
                    else:
                        print("{:s} misses {:s} just slightly!".format(rogue.get_name(), fighter.get_name()))
                    if fighter.is_downed():
                        print("{:s} finally falls to the ground unconscious.".format(fighter.get_name()))

                    input()
                    print("The crowd is stirring and the three adventurers understand it would be best to "
                          "just leave the tavern as soon as possible.")
                    input()
                    print("{:s} tries to block the crowd by throwing some tables at them. "
                          "She does an Athletics check to do so.".format(ranger.get_name()))
                    success = ranger.skill_check("Athletics", 8)
                    if success:
                        print("It succeeds! The tables move easily and the crowd is slowed down a little by "
                              "{:s}'s actions.".format(ranger.get_name()))
                    else:
                        print("It fails. The tables won't budge and {:s} abandons the idea quickly."
                              .format(ranger.get_name()))

                    input()
                    print("The adventurers run fast away from the tavern.")
                    input()
                    print("When they think they have reached safety, {:s} takes a look at {:s}'s wounds and tries "
                          "a Medicine check to heal her.".format(wizard.get_name(), rogue.get_name()))
                    success = wizard.skill_check("Medicine", 10)
                    input()
                    if success:
                        healed_hp = rogue.heal()
                        print("It succeeds! {:s} feels a little better and heals for {:d} hit points."
                              .format(rogue.get_name(), healed_hp))
                    else:
                        print("It fails. {:s} is still shocked by the incident and he is unable to heal {:s}."
                              .format(wizard.get_name(), rogue.get_name()))

                    input()
                    wizard.level_up()
                    print("{:s} leveled up to level {:d}!".format(wizard.get_name(), wizard.get_level()))

                    input()
                    print("The three adventures continue their journey to the great unknown.")
                    print()
                    print("Final situation:")
                    print(ranger)
                    print()
                    print(wizard)
                    print()
                    print(rogue)


main()

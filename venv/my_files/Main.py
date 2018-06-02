from my_files.enemies import *
from my_files.heroes import *

#turning up the diffmod will make the game easier. Lowering it will make the game harder.


def statsOrContinue(hero):
    nextstep = input("Great Job ! You can now check out your [S]tats now if you want, or you can [C]ontinue :").upper()

    if nextstep not in "SC" or len(nextstep) != 1:
        print("Don't be silly.Really, its becoming tiring")
    elif nextstep == 'S':
        hero.listStats()
    elif nextstep == 'C':
        return






# THIS IS THE MAIN COMBAT LOOP

class Combat :
        def __init__(self):

            self.turn = 0


        def combatLoop(self, hero, enemy):
           while hero.alive and enemy.alive :
            hero.regenAll()
            pchoice = hero.chooseAttack()
            if pchoice == 'S':
                print("You have attacked the ",enemy.name, " with Sorcery for ", enemy.takeDamage(hero.sorceryAttack()), " damage !")
            elif pchoice == 'R':
                print("You have attacked the ", enemy.name, " at Range for ", enemy.takeDamage(hero.rangedAttack()), " damage !")
            elif pchoice == 'M':
                print("You have attacked the ", enemy.name, " with a Melee hit for ", enemy.takeDamage(hero.meleeAttack()), " damage !")
            elif pchoice == 'H':
                print("You have casted Heal, healing yourself for ", hero.healingAttack(), " health !")
            if enemy.health <= 0:
                hero.experiencePoints += enemy.expvalue
                print("Yes ! You've defeated the pesky ", enemy.name, ". Great work !")
                hero.checkExpForLevel()
                return



            print("The ", enemy.name, " has ",enemy.health, " health remaining.")
            print("The enemy ",enemy.name, " has attacked you!")
            hero.takingDamage(enemy.attackDamage)
            if hero_guy.alive == False:
                print("Oh no ! You have died...")
                exit()





print("On this journey you will be faced with many trials. Are you ready to tempt fate and see what lies ahead ?")
while True:
    action = input("Continue ? Y / N").upper()
    if action not in "YNP" or len(action) !=1:

        print("Don't be silly.")
        continue

    if action == 'Y':
            print("You have chose a dangerous path, but only those w"
                    "ho are willing to risk it all will bask in the glory of the rewards")

            hero_guy = Player()
            hero_guy.abilityPoints += 8
            print ("Amazing !")
            while hero_guy.abilityPoints > 0:
                statSelect = input("You now have {} ability points to spend. You "
                              "can choose from [S]Sorcery, [R]anged, [M]elee, [D]efense, or [H]ealing".format(hero_guy.abilityPoints)).upper()
                if statSelect not in "SMRHD" or len(statSelect) != 1:
                    print("Don't be silly.")
                else:
                    hero_guy.statChooser(statSelect)

            while hero_guy.alive:

                    statsOrContinue(hero_guy)
                    new_croc = Crocodile()
                    new_combat = Combat()

                    print("In an instant, the mysterious voice echoes away to a barely heard whisper.")
                    print("You hear a low rumble and turn around to see a fully grown crocodile coming straight out you from the water. ")
                    print("The Croc approaches - how will you attack it ? ")
                    new_combat.combatLoop(hero_guy,new_croc)
                    del new_croc
                    del new_combat


                    statsOrContinue(hero_guy)
                    print("What a fight !  The croc didn't stand a chance. Just as his corpse lifelessly hits the ground, you hear a"
                          "chilling sound and feel a cold breeze on your arm. You can't believe it , but floating in front of you is a spooky "
                          "ghost !")
                    new_ghost = Ghost()
                    new_combat = Combat()
                    new_combat.combatLoop(hero_guy,new_ghost)




    elif action == 'P':
            print("This is a Hidden Option that serves no purpose")



    elif action == 'N':
            print("That is too bad. Your cowardice belies your true fate, however, "
                      "as that which can be gained may only be done so through sacrifice. ")
    exit()



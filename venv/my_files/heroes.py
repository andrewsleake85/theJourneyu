diffmod = 0

class Player:
    def __init__(self):

        #some globals
        self.alive = True


        #player stats start at zero
        self.sorcery = 0
        self.ranged = 0
        self.melee = 0
        self.defense = 0
        self.healing = 0

        #lets give him so combat stats too
        self.health = 150 + (diffmod * 5)
        self.mana = 100 + (diffmod *2 )
        self.energy = 100 + (diffmod *3)
        self.baseDamage = 5 + diffmod

        #for leveling and getting points
        self.abilityPoints = 0
        self.experiencePoints = 0
        self.overallLevel = 1



    def checkExpForLevel(self):
        if self.experiencePoints >=  50 + (self.overallLevel ** 1.2):
            self.experiencePoints -=  50 + (self.overallLevel ** 1.2)
            self.overallLevel += 1
            self.abilityPoints += 4
            print("Congratulations, you have gained a level !")
            print("You are now Level ",self.overallLevel, " and have ",self.abilityPoints, " ability points to spend")
            while self.abilityPoints > 0:
                statSelect = input("You now have {} ability points to spend. You "
                                   "can choose from [S]Sorcery, [R]anged, [M]elee, [D]efense, or [H]ealing".format(
                    self.abilityPoints)).upper()
                if statSelect not in "SMRHD" or len(statSelect) != 1:
                    print("Don't be silly.")
                else:
                    self.statChooser(statSelect)



    def regenAll(self):
        if self.health <= 149:
            self.health += 1
        if self.mana <= 95:
            self.mana += 5
        if self.energy <=95:
            self.energy +=5
        print("You have regenerated 1 HP, 5 Mana, and 5 Energy")

# leveling stats

    def levelSorcery(self):
        self.sorcery +=1
        self.abilityPoints -=1

    def levelRanged(self):
        self.ranged += 1
        self.abilityPoints -= 1

    def levelMelee(self):
        self.melee += 1
        self.abilityPoints -= 1

    def levelDefense(self):
        self.defense += 1
        self.abilityPoints -= 1

    def levelHealing(self):
        self.healing += 1
        self.abilityPoints -= 1

    def statChooser(self, choice):
        if choice == 'M':
            self.levelMelee()
        elif choice == 'S':
            self.levelSorcery()
        elif choice == 'D':
            self.levelDefense()
        elif choice == 'R':
            self.levelRanged()
        elif choice == 'H':
            self.levelHealing()

# list current stats

    def listStats(self):
        print("")
        print("--------------- ")
        print("Health : ", self.health)
        print("Mana   : ", self.mana)
        print("Energy : ", self.energy)
        print("----------------")
        print("Sorcery : ", self.sorcery)
        print("Ranged  : ", self.ranged)
        print("Melee   : ", self.melee)
        print("Defense : ", self.defense)
        print("Healing : ", self.healing)
        print("----------------")
        print("")

# basic attacks
    # shows attacks, stats, and checks to make sure you can do that attack
    #then returns the type of attack the player chooses
    def chooseAttack(self):

        while True:
            print("")
            print("----------------------------------------------")
            print("Pick your Next Attack")
            print("Sorcery: Cost 20 Mana         Health : ", self.health)
            print("Ranged : Cost 10 Energy       Mana   : ", self.mana)
            print("Melee  : Cost 15 Energy       Energy : ", self.energy)
            print("Heal   : Cost 20 Mana")
            print("----------------------------------------------")
            print(" ")
            select = input(">>>>>>>>>>>>>>>>>>>>>>>").upper()
            print(" ")


            if select not in "SMRH" or len(select) != 1:
                print("Don't be silly. Pick an Attack !")
            elif select == 'S':
                if self.mana < 20:
                    print("")
                    print("-----------------------------------------")
                    print("You do not have enough mana to cast this!")
                    print("-----------------------------------------")
                    print("")
                    continue
                else :
                    return 'S'

            elif select == 'H':
                if self.mana < 20:
                    print("")
                    print("-----------------------------------------")
                    print("You do not have enough mana to cast this!")
                    print("-----------------------------------------")
                    print("")
                    continue
                else:
                    return 'H'

            elif select == 'R':
                if self.energy < 10:
                    print("")
                    print("-------------------------------------------------")
                    print("You do not have enough energy to use this attack!")
                    print("-------------------------------------------------")
                    print("")
                    continue
                else :
                    return 'R'

            elif select == 'M':
                if self.energy <15:
                    print("")
                    print("--------------------------------------------------")
                    print("You do not have enough energy to use this attack !")
                    print("--------------------------------------------------")
                    print("")
                    continue
                else :
                    return 'M'




    def sorceryAttack(self):
        self.mana -= 20
        return self.baseDamage + (self.sorcery * 2)

    def rangedAttack(self):
        self.energy -= 10
        return self.baseDamage + self.ranged

    def meleeAttack(self):
        self.energy -=15
        return self.baseDamage + (self.melee * 1.5)

    def healingAttack(self):
        self.mana -= 20
        self.health += self.healing
        return self.healing

    #taking damage

    def takingDamage(self, amount):

        simple = amount - self.defense

        if simple < 1:
             print("You've Deflected all of the damage!")
        else:
            self.health -= simple
            if self.health < 0:
                self.alive = False
            else:
                print("You've taken ", simple, " damage ! Your health is at ", self.health, ".")




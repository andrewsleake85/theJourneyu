class enemyTest:
    def __init__(self):
        self.value = 80



    def printTest(self):
        print("Value:",self.value)



 # this is an enemy

class Crocodile:
    def __init__(self):

        self.attackDamage = 75
        self.health = 30
        self.armor = 1

        self.alive = True
        self.name = "Crocodile"
        self.expvalue = 20




    def takeDamage(self, amount):

        simple = amount - self.armor
        self.health -= simple

        if self.health < 0:
            self.alive = False
            return simple
        else:
            return simple

class Ghost:
    def __init__(self):


        self.attackDamage = 10
        self.health = 35
        self.armor = 1

        self.alive = True
        self.name = "Ghost"
        self.expvalue = 25


    def takeDamage(self, amount):

        simple = amount - self.armor
        self.health -= simple

        if self.health < 0:
            self.alive = False
            return simple
        else:
            return simple
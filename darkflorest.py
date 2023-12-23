#DARK FLOREST
import random
import pyfiglet
import time
import sys
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# display
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.002)

#MAP
rooms = {
    "Campfire": {"East": "Woods1"},
    "Woods1": {"North": "Woods2", "South": "Cave1", "West": "Campfire",},
    "Woods2": {"North": "Lake", "East": "Easteregg", "South": "Woods1"},
    "Lake": {"South": "Woods2"},
    "Easteregg": {"West": "Woods2"},
    "Cave1": {"North": "Woods1", "East": "Cave2"},
    "Cave2": {"North": "Altar", "West": "Cave1"},
    "Altar": {"South": "Cave2"}
}

# Track player
current_room = "Campfire"

#variable of the result of the last move
last_move = ""

#CHARaCTERS
class character:
    def __init__(self, name, hitpoints, attack, defence, agillity):
        self.name = name
        self.hitpoints = hitpoints
        self.attack = attack
        self.defence =  defence 
        self.agillity = agillity 
        self.max_hp = hitpoints
    
    def move(self, enemy):
        damage = (random.randint(1, 3)) * self.attack 
        damage -= enemy.defence
        if damage < 0:
            damage = 0
        print("{name} has done {damage} of damage to {enemy.name} ".format(name=self.name, damage=damage, enemy=enemy))
        enemy.hitpoints -= damage


def battle(enemy1, enemy2):
    while enemy1.hitpoints > 0 and enemy2.hitpoints > 0:
        if enemy1.agillity * (random.randint(1, 3)) >= enemy2.agillity * (random.randint(1, 3)):
            enemy1.move(enemy2)

            if enemy2.hitpoints > 0:
                enemy2.move(enemy1)
        elif enemy1.agillity * (random.randint(1, 3)) < enemy2.agillity * (random.randint(1, 3)):
            enemy2.move(enemy1)

            if enemy1.hitpoints > 0:
                enemy1.move(enemy2)

        if enemy1.hitpoints <= 0:
            print("{enemy1.name} has died".format(enemy1=enemy1))
            return enemy2

        elif enemy2.hitpoints <= 0:
            print("{enemy2.name} has died".format(enemy2=enemy2))
            return enemy1

        else:
            print("\n")
            print("{enemy1.name} has {enemy1.hitpoints} hitpoints left".format(enemy1=enemy1))
            print("{enemy2.name} has {enemy2.hitpoints} hitpoints left".format(enemy2=enemy2))

    return

#enemys
enemy_goblin = character("Goblin", 30, 3, 3, 3)
enemy_bat1 = character("Bat", 25 , 3, 2, 5)
enemy_vampire = character("Vampire", 40, 4, 3, 6)
enemy_bat2 = character("Bat", 25 , 3, 2, 5)

#begning
delay_print(pyfiglet.figlet_format("Welcome to Dark Florest..  ", justify="center"))
delay_print("You have just woke up on a dark strange place.. youn dont have any recolection of how you end up here.. You are in a dense florest, the only thing that you see is a campfire with a track leading to the east..")
delay_print("The only memorie that you have is that your name is..")

#enter name of hero
heroname = input(" ")

#chosse class
delay_print("... and that there are three classes: Rogue, Warrior or Mage..  ")
classchosen = input ("Wich is your class?  ")

while classchosen != "Rogue" and classchosen != "Warrior" and classchosen != "Mage":
    classchosen = input("There is no such a class.. try again:  ")

if classchosen == "Mage":
    print("For those whom seeak knolagie I salute you.. A book worm with turst for the screets of magic.")
    hero = character(heroname, 50, 7, 3, 3)
    print("  You are a " + classchosen + ", so, your`s stats are, Attack:7, Defense:3, Agill1ity:3, Hitpoints:50")
   
elif classchosen == "Rogue":
    print("You won`t see me coming.. or leving for that matter.. Sneak bastard, raise by the darkness but a good company when drinking")
    hero = character(heroname, 60, 3, 3, 7)
    print("  You are a " + classchosen + ", so, your`s stats are, Attack:3, Defense:3, Agill1ity:7, Hitpoints:70")
   
elif classchosen == "Warrior":
    print("Me? not smart! But I smash things.. Loud and ruthless, with a might strength.")
    hero = character(heroname, 70, 3, 5, 3)
    print("  You are a " + classchosen + ", so, your`s stats are, Attack:3, Defense:7, Agill1ity:3, Hitpoints:70")

#map desc
def descrip():
    if current_room == "Campfire":
        print("It`s warm.. but the darkest of the florest around you still chill your spine.")
    elif current_room == "Woods1":
        print("The track lad you to an opening in the florest, you can see a glimpsi of the moon, but it barly lights up the place.")
    elif current_room == "Woods2":
        print("Another opening.. hope there isn`t another bat here.")
    elif current_room == "Cave1":
        print("Oh, a Cave.. I`m certain that this is way to escape, trhough a cave.")
    elif current_room == "Lake":
        print("What? There are more than bats in this game?! Hope it`s worth it!! Time to slay a floor factory worker.")
    elif current_room == "Easteregg":
        print("You find Leo Dies shrine! All pray and haill ディアス神(Diasu Kami).")
        print("Leo blessed you whit full health!")
        while hero.hitpoints <= hero.max_hp:
            hero.hitpoints += 1
    elif current_room == "Cave2":
        print( "Looks like people used to mine here, the mine trail go alll the way to there!")
    elif current_room == "Altar":
        print("Your last challenge.. it`s thee!! Hellsing!! i shall bring grace upon this word by freeing of thou!! Glad I`m one quarter chinese.")

#if map has enemy
def encounter():
            if current_room == 'Woods1':
                #First Battle
                if enemy_bat1.hitpoints == 0:
                    return
                else:
                    print("Holy BatMan, a big Bat appers HERO HP:{hero.hitpoints}   BAT HP:".format(hero=hero) + str(enemy_bat1.hitpoints))
                    battle(hero, enemy_bat1)
            elif current_room == 'Lake':
                print("Holy Goblin, a big Goblin appers  HERO HP:{hero.hitpoints}   Goblin HP:".format(hero=hero) + str(enemy_goblin.hitpoints))
                battle(hero, enemy_goblin)
            elif current_room == "Cave2":
                print("You see a big bat flying towards you. There are a whole lot of bats in this game. I wonder if it might mean something")
                battle(hero, enemy_bat2)
            elif current_room == 'Altar':
                print("Holy Vampire, a big vampire appers   HERO HP:{hitpoints}   Vampire HP:".format(hitpoints=hero.hitpoints) + str(enemy_vampire.hitpoints))
                battle(hero, enemy_vampire)
            else:
                return

#adventure loop
while True:

    clear()
     # if you died
    if hero.hitpoints <= 0:
        clear()
        delay_print(pyfiglet.figlet_format("YOU ARE DEAD!!!", justify="center"))
        break

    #display info
    print(".........Dark Florest.........")
    print("\n")
    print("{name} is by the {room}     HP:{hp}".format(room=current_room, name = heroname, hp = str(hero.hitpoints))) 
    descrip()
    print("\n")
    

    #if vampire dies
    if enemy_vampire.hitpoints <= 0:
        clear()
        delay_print(pyfiglet.figlet_format("    winner!!!    ", justify="center"))
        break

    #display last move
    print(last_move)

    #encounter
    encounter()
       
     # Accepts player's move as input
    user_input = input("Enter your move:\n")

    # Splits move into words
    next_move = user_input.split(' ')

    # First word is action
    action = next_move[0].title()

    # Reset direction
    direction = "null"


    # Second word is object or direction
    if len(next_move) > 1:
        direction = next_move[1].title()

    # Moving between rooms
    if action == "Go":

        try:
            current_room = rooms[current_room][direction]
            last_move = f"You travel {direction}"

        except:
            last_move = "You can't go that way."

         # Exit program
    elif action == "Exit":
        break
    
     # Any other commands invalid
    else:
        last_move = "Invalid command"
        
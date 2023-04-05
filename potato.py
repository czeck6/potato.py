import random
from time import sleep
import os

# Grass and Mud...(Roll a D6)
d3_txt = "The world becomes a darker, more \n" \
          "dangerous place. From now on, \n" \
          "removing ORC costs an additional \n" \
          "POTATO (this is cumulative)"

destiny = 0
potatoes = 0
orcs = 0
dark_square = " "  # "\u2B1A"
lite_square = "X"  # "\u25A3"
cost_adjustment = 0
global turns
turns = 0


def show_score():
    print("potatoes = ", (potatoes * lite_square) + ((10 - potatoes) * dark_square))
    print("orcs     = ", (orcs * lite_square) + ((10 - orcs) * dark_square))
    print("destiny  = ", (destiny * lite_square) + ((10 - destiny) * dark_square))


def garden_roll():
    roll = random.randint(1, 6)
    global orcs, potatoes, destiny, cost_adjustment
    print("You're In the Garden..." + "\n")
    if roll == 1:
        potatoes += 1
        if potatoes < 0:
            potatoes = 0
        print("You happily root about all day in your garden")
    elif roll == 2:
        potatoes += 1
        if potatoes < 0:
            potatoes = 0
        destiny += 1
        if destiny < 0:
            destiny = 0
        print("You narrowly avoid a visitor by hiding in a potato sack.")
    elif roll == 3:
        destiny += 1
        if destiny < 0:
            destiny = 0
        orcs += 1
        if orcs < 0:
            orcs = 0
        print("A hooded stranger lingers outside your farm.")
    elif roll == 4:
        orcs += 1
        if orcs < 0:
            orcs = 0
        potatoes -= 1
        if potatoes < 0:
            potatoes = 0
        print("Your field is ravaged in the night by unseen enemies")
    elif roll == 5:
        potatoes -= 1
        if potatoes < 0:
            potatoes = 0
        print("You trade potatoes for other delicious foodstuffs.")
    elif roll == 6:
        potatoes += 2
        if potatoes < 0:
            potatoes = 0
        print("You burrow into a bumper crop of potatoes. Do you cry with joy? Possibly.")


def knock_roll():
    roll = random.randint(1, 6)
    global orcs, potatoes, destiny, cost_adjustment
    print("You hear a knock at the door..." + "\n")
    if roll == 1:
        orcs += 1
        if orcs < 0:
            orcs = 0
        print("A distant cousin. They are after your potatoes. They may snitch on you")
    elif roll == 2:
        destiny += 1
        if destiny < 0:
            destiny = 0
        print("A dwarven stranger. You refuse them entry. Ghastly creatures.")
    elif roll == 3:
        destiny += 1
        if destiny < 0:
            destiny = 0
        orcs += 1
        if orcs < 0:
            orcs = 0
        print("A wizard strolls by. You pointedly draw the curtains..")
    elif roll == 4:
        orcs += 1
        if orcs < 0:
            orcs = 0
        potatoes -= 1
        if potatoes < 0:
            potatoes = 0
        print("There are rumours of war in the reaches. You eat some potatoes.")
    elif roll == 5:
        destiny -= 1
        if destiny < 0:
            destiny = 0
        print("It's an elf. They are not serious people")
    elif roll == 6:
        potatoes += 2
        if potatoes < 0:
            potatoes = 0
        print("It's a sack of potatoes from a generous neighbour. "
              "You really must remember to pay them a visit one of these years..")


while orcs < 10 and potatoes < 10 and destiny < 10:
    turns += 1
    if orcs > 0 and potatoes > 1 + cost_adjustment:
        cost = str(cost_adjustment + 1)
        remove_orc = input("Do you want to spend " + cost + " potatoes to remove an orc? (y/n): ")
        while remove_orc == 'y' and potatoes > 1 + cost_adjustment:
            potatoes -= 1 + cost_adjustment
            orcs -= 1
            print("One orc has been removed.")
            if orcs == 0:
                break

    if potatoes < 10 or destiny < 10:
        os.system('cls')
        d3 = random.randint(1, 3)
        if d3 == 1:
            cost_adjustment += 1
            garden_roll()
            show_score()
            sleep(0.01)
        elif d3 == 2:
            knock_roll()
            show_score()
            sleep(0.01)
        elif d3 == 3:
            print(d3_txt)
            show_score()
    else:
        break

if orcs > 9:
    print("The orcs finally found your farm.")
    print("You Lose!")

if potatoes > 9:
    print("You Won!  You have enough potatoes to wait out the danger.")

if destiny > 9:
    print("You Won! An interfering bard or wizard turns up at your doorstep and whisks you off on an adventure.")

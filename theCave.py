import random
import time


def intro():
    print('You are adventuring in a far off land.')
    time.sleep(2)
    print('Your journey has brought you to a deep, dark cave.')
    time.sleep(2)
    print('There is a ' + instanceEnemy + ' in front of you, do you want to fight or run?')


def fight(choice):
    print('Your attack is: ' + str(int(attack)) + '. The ' + instanceEnemy + '\'s defense is: ' + str(int(defense)) + '.')
    time.sleep(2)
    if int(attack) >= int(defense): # victory conditions: your attack needs to be higher than or equal to the enemy defense
        print('After a brutal fight, your sword...')
        time.sleep(2)
        print('...cuts off the ' + instanceEnemy + '\'s head. You emerge victorious!')
        time.sleep(2)
        print('CONGRATULATIONS. YOU WIN. GAME OVER.')
    else:
        print('Your attempt to fight fails.') # failure is your attack being less than the enemy defense
        time.sleep(2)
        print('Your sword glances off the ' + instanceEnemy + '\'s skin and he eats you for dinner.')
        time.sleep(2)
        print('YOU DIED. GAME OVER')
def run(choice):
    print('Your speed is: ' + str(int(runVal)) + '. The ' + instanceEnemy + '\'s speed is: ' + str(int(escapeVal)) + '.')
    time.sleep(2)
    if int(runVal) >= int(escapeVal): # in order to succeed in running away, you need to be faster than the enemy
        print('You are too fast for the ' + instanceEnemy + '. You escape death...for now.')
        print('CONGRATULATIONS. YOU WIN. GAME OVER.')
    else: # if you are too slow, you are defeated by the enemy
        print('You are too slow for the surprisingly agile ' + instanceEnemy + '.')
        time.sleep(2)
        print('He plucks you off the ground and eats you in one bite.')
        time.sleep(2)
        print('YOU DIED. GAME OVER')

# How we get the name of the enemy
enemy = ['troll', 'goblin', 'orc', 'dragon', 'mutant',]
descriptor = ['ugly', 'large', 'nasty', 'smelly', 'gross']
instanceEnemy = random.choice(descriptor) + ' ' + random.choice(enemy)

# How we get the values for each choice
roll = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
attack = int(random.choice(roll))
defense = int(random.choice(roll))
runVal = int(random.choice(roll))
escapeVal = int(random.choice(roll))

playAgain = 'yes'
while playAgain == 'yes':
    intro()
    choice = input()
    if choice == 'fight':
        print('You swing your sword at the ' + instanceEnemy + '.')
        time.sleep(2)
        fight(choice)
    elif choice == 'run':
        print('You attempt to turn and run away from the ' + instanceEnemy + '.')
        time.sleep(2)
        run(choice)
    print('Do you want to play again?')
    playAgain = input()
    if playAgain == 'no':
        print('Thank you for playing!')
      

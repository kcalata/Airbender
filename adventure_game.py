# Avatar: The Last Airbender was my inspiration for this

import time
import random


def print_pause(message):
    print(message)
    time.sleep(1)


def intro():
    print_pause('You feel a gust of wind.')
    print_pause('It refreshes you and you open your eyes.')
    print_pause('In front of you are thousands of toys '
                'but you have chosen your favorite 8.')
    print_pause('"You must choose 4 of these 8, young one."')


def choice_2(potential):
    potential.append(0)
    potential.append(0)
    print_pause('You feel a sense of relief.')


def toy_1(potential):
    print_pause('Choose one.\n1. Clay Turtle\n2. Metal Dragon')
    choice = input('Please enter 1 or 2\n')
    if choice == '1':
        potential.append(1)
        print_pause('You feel a gust of wind.')
    elif choice == '2':
        choice_2(potential)
    else:
        toy_1(potential)


def toy_2(potential):
    print_pause('Choose one.\n1. Pull-String Propeller\n'
                '2. Automatic Propeller')
    choice = input('Please enter 1 or 2\n')
    if choice == '1':
        potential.append(1)
        print_pause('A drop of water hits your cheek.')
    elif choice == '2':
        choice_2(potential)
    else:
        toy_2(potential)


def toy_3(potential):
    print_pause('Choose one.\n1. Wooden Hog Monkey\n2. Plastic Fairy Ostrich')
    choice = input('Please enter 1 or 2\n')
    if choice == '1':
        potential.append(1)
        print_pause('The ground shakes.')
    elif choice == '2':
        choice_2(potential)
    else:
        toy_3(potential)


def toy_4(potential):
    print_pause('Choose one.\n1. Wooden Hand Drum\n2. Earthy Guitar')
    choice = input('Please enter 1 or 2\n')
    if choice == '1':
        potential.append(1)
        print_pause('You feel a wave of heat.')
    elif choice == '2':
        choice_2(potential)
    else:
        toy_4(potential)


def avatar():
    print_pause('Congratulations! You are the avatar, '
                'master all of four elements.')
    print_pause('You feel overwhelmed. Should you run '
                'away or stay and grab a hold of your destiny?')
    while True:
        print_pause('Choose one.\n1. Run away.\n'
                    '2. Grab a hold of your destiny.')
        choice = input('Please enter 1 or 2\n')
        if choice == '1':
            print_pause('There is no shame in running away.')
            print_pause('You are but a child.')
            print_pause('You run out of the room and '
                        'jump onto your loyal steed.')
            print_pause('You blaze past all of the people you grew up with.')
            print_pause('You get out of town.')
            print_pause('A torrential storm starts.')
            print_pause('You and your steed can barely see anything.')
            print_pause('You lose your footing.')
            print_pause('You plummet down to the dark abyss of the ocean.')
            print_pause('Everything goes black.')
            print_pause('THUD WHACK CRACK')
            print_pause('To be continued...')
            break
        elif choice == '2':
            print_pause('Everyone rejoices.')
            print_pause('The new avatar has come.')
            print_pause('THWACK')
            print_pause('Your masters around you fall to the floor.')
            print_pause('A flaming arrow is in their backs.')
            print_pause('You run outside in terror.')
            print_pause('You run throat first into the arm of an unknown man.')
            print_pause('You\'ve seen this man before.')
            print_pause('You recognize the blazing red robes he wears.')
            print_pause('The golden crown that takes the '
                        'shape of a fireball on his head.')
            print_pause('It\'s the fire-lord.')
            print_pause('He grabs you with a swift motion and '
                        'his hand engulfs your face.')
            print_pause('A flame comes out of his hand as '
                        'quickly as your face and life turns to ashes.')
            print_pause('The fire-lord bellows, "The time '
                        'of the avatar is done."')
            print_pause('Game over.')
            break


def ordinary():
    print_pause('Congratulations!')
    print_pause('You get to live an ordinary life full of ordinary events.')
    print_pause('THWACK')
    print_pause('Just kidding.')
    print_pause('Your town has been burned down by '
                'fire-benders looking for the next avatar.')
    print_pause('Game over.')


def replay():
    print_pause('Would you like to play again?')
    choice = input('Yes or no?\n').lower()
    if choice == 'yes':
        destiny()
    elif choice != 'no':
        replay()


def destiny():
    potential = []
    intro()
    print_pause('Choose one from each of the following pairs.')
    toy_1(potential)
    toy_2(potential)
    toy_3(potential)
    toy_4(potential)
    if random.choice(potential) == 1:
        avatar()
    elif random.choice(potential) == 0:
        ordinary()
    replay()


destiny()

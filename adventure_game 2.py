import time
import random


def print_pause(string):
    print(string)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        user_input = input(f"{prompt}\n\n1. {option1} \n2. {option2}\n\nYour "
                           "pick: ")

        if user_input == "1" or user_input == "2":
            break
        else:
            print("\nSorry, didn't get that... choose either option 1 or 2.\n")
    return user_input


def character():
    characters = ["neighbor", "flatmate", "ex"]
    attacks = ["coughs", "sneezes", "spits"]
    return random.choice(characters), random.choice(attacks)


def intro():
    print("""
INFECTION
    """)
    print_pause("THE GAME...\n\n")
    print_pause("You have just woken up...")
    print_pause("It's saturday, 10:00am, you are alone at your place, "
                "having breakfast and watching the news in the kitchen...")
    print_pause("You suddenly realise you are in a very unusual situation:")
    print_pause("""
    __________________________________________________________________________
   |BREAKING NEWS: There's a worldwide pandemic and the entire world is about |
   |               to go on lockdown. Citizens will be safe if they stay home |
   |               for the next 14 to 45 days.                                |
   |__________________________________________________________________________|
                """)
    print_pause("You think to yourself:")
    print_pause(" - Oh my god! We have no supplies at home!")
    print_pause(" - No worries, nothing to be completely terrified, just "
                "yet... ")
    print_pause(" - I just have to go to the nearest supermarket and get "
                "what I need for the coming weeks...\n")


def living_room(items, infected):
    response = valid_input("You are in your living room and you can either "
                           "head out to the supermarket straight ahead "
                           "or call your flatmates to see where they are...",
                           "Head out",
                           "Call your flatmates")

    if response == "1":
        print_pause("You are about to open the door to head out "
                    "and hear a weird sound out in the hall. ")
        print_pause(f"Hm, strange... your {character()[0]} is there! "
                    f"you guys start talking and she {character()[1]} "
                    f"on your face!!!")
        print_pause("You act like it didn't happen bu you can't help it... "
                    "You have to get out of there!\n...\n")
        supermarket(items, infected)

    elif response == "2":
        print_pause("One of your flatmates, who works as a nurse answers "
                    "the phone and says "
                    "he went for a run and he'll be back home soon.")
        print_pause("He tells you there's gloves, a full face mask and "
                    "disinfectant in his room "
                    "and that you can take what you need.\n")
        items.append("Lysol")
        print_pause("You are now wearing PPE and equipped with Lysol.")
        print_pause("You are about to open the door to head out "
                    "and hear a weird sound out in the  hall. ")
        print_pause(f"As soon as you open the door your {character()[0]} "
                    f"comes inside your "
                    f"flat and tries to {character()[1]} on your face!!!")
        print_pause("Hopefully you were wearing PPE... Phew...")
        supermarket(items, infected)


def supermarket(items, infected):
    response = valid_input("You have finally arrived at the supermarket, "
                           "there is a line of about 200 people... "
                           "Turns out you were not the only genius with your "
                           "idea. You see that down to the first "
                           "place of the line and there's your friend!",
                           "Cheat the line and go in the supermarket with "
                           "the person you know",
                           "Stay in the line")

    if response == "1":
        print_pause("You go and start talking with the person you know "
                    "first on the line...")
        print_pause("When people realise what you are trying to do they "
                    "start to get angry and raise their voices at you...")
        print_pause("They soon start getting closer and closer to you...")
        print_pause("One of them is actually close enough to take your PPE!!")
        print_pause(f"Even your friend is angry! He comes and "
                    f"{character()[1]} on your face!")
        infected = True
        game_over(infected)

    elif response == "2":
        if "Lysol" in items:
            print_pause("You wait 3 hours in line but there's enough "
                        "supplies for everyone...")
            print_pause("You take what you need and even get your"
                        " flatmates some ice cream and popcorn")
            print_pause("Of course you took only what you needed...")
            print_pause("Yeah, that's including toilet paper!!")
            print_pause("Happy Quarantine!")
            game_over(infected)
        else:
            print_pause("You waited in line for 3 hours and when you "
                        "were about to enter "
                        "the supermarket but they say you need PPE to "
                        "go in... "
                        "Come back when you get some...")
            print_pause("You go back to your house...")
            living_room(items, infected)


def game_over(infected):
    if infected is True:
        print_pause("""
GAME OVER
YOU HAVE BEEN INFECTED...
        """)
        play_again()
    else:
        print_pause("""
CONGRATS!
YOU SURVIVED!!
        """)
        play_again()


def play_again():
    response = valid_input("\n\nWould you like to play again?", "Yes", "No")
    if response == "1":
        infection()
    elif response == "2":
        print("Ok, Goodbye!")


def infection():
    infected = False
    items = []
    intro()
    living_room(items, infected)


if __name__ == "__main__":
    infection()

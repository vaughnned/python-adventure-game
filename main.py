from elia import Elia
from vaughn import Vaughn
from jay import Jay
from help import Directory


text = (
    "Welcome to the Time Adventure Game!"
    "You are a lonely scientist,"
    "who has stumbled upon the solution to time travel."
    "You must now decide where your first adventure shall take you!"
    "Type START, to start the game or HELP for help."
    "Type QUIT to end the game at anytime."
)
print(text)
player_input = ""


def play_elia():
    elia = Elia()
    return elia.past()


def play_vaughn():
    vaughn = Vaughn()
    return vaughn.present()


def play_jay():
    jay = Jay()
    return jay.future()


def play_help():
    help_dir = Directory()
    help_dir.display_help()


# class Prompt:
#     def __init__(self, opt1, opt2, opt3):
#         self.opt1 = opt1
#         self.opt2 = opt2
#         self.opt3 = opt3


def play(player_input):
    while player_input.upper() != "QUIT":
        # print()
        player_input = input(
            "You enter your time machine and it asks you for a destination: PAST, PRESENT or FUTURE. > "
        )
        if player_input.upper() == "PAST":
            print("PAST")
            return play_elia()
        elif player_input.upper() == "PRESENT":
            print("PRESENT")
            return play_vaughn()
        elif player_input.upper() == "FUTURE":
            print("FUTURE")
        elif player_input.upper() == "HELP":
            print("HELP")


play(player_input)

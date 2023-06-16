player_input = ""

class Vaughn:
    
    def __init__(self):
        pass

    def enter(self):
        quit = False
        while not quit:
            player_input = input("What will you arm yourself with: (a big ROCK you found by your feet), (widdle a STICK into a spear) or (your not afraid of some stupid little bear (FISTS)) > ")
            if player_input.upper() == "ROCK":
                print()
                print(" ")
                print(" ")
                print()
            elif player_input.upper() == "STICK":
                print()
                print(" ")
                print()
            elif player_input.upper() == "FISTS":
                print()
                print(" ")
                print()
            elif player_input.upper() == "QUIT":
                quit = True
    
    def yell(self):
        quit = False
        while not quit:
            player_input = input("Would you like to: (make a RUN for the cave) or (try to back up slowly and HIDE in your time machine) > ")
            if player_input.upper() == "RUN":
                print()
                print(" ")
                print(" ")
                print()
            elif player_input.upper() == "HIDE":
                print()
                print(" ")
                print()
            elif player_input.upper() == "QUIT":
                quit = True

    def search(self):
        quit = False
        while not quit:
            player_input = input("Would you like to: (pull up your big boy pants and ENTER the cave) or (CHICKEN out and stay in the forest for now) > ")
            if player_input.upper() == "ENTER":
                print()
                print("You are determined to get this power core no matter the cost. ")
                print("You should probably arm yourself for the worst case scenario where you run into this bear on your search. ")
                print()
            elif player_input.upper() == "CHICKEN":
                print()
                print(" ")
                print()
            elif player_input.upper() == "QUIT":
                quit = True
        
    def look(self):
        quit = False
        while not quit:
            player_input = input("Would you like to: (SEARCH the surrounding area) or (YELL for help and hope someone hears your cries) > ")
            if player_input.upper() == "SEARCH":
                print()
                print("You search your surrounding area in hopes that you will stumble upon your power core. ")
                print("Instead you find what appear to be bear tracks in the mud with a streak of oil on the ground leading up to the entrance of a cave... ")
                print()
                return self.search()
            elif player_input.upper() == "YELL":
                print()
                print("You decide to try your luck with yelling and hoping someone is also deep in this random forest with you for some reason. ")
                print("After a few minutes of yelling, you realize this was bad idea when you lock eyes with a pair of glowing eyes in a bush followed by a deep growl. ")
                print()
            elif player_input.upper() == "QUIT":
                quit = True

    def present(self):
        quit = False
        print()
        print("ERROR ERROR! Your time machine starts making loud noises and shaking intensely. ")
        print("After a few moments of chaos everything goes black... ")
        print("You wake up in a forest surrounded by vines, foliage and trees for as far as you can see." )
        print()
        while not quit:
            player_input = input("What would you like to do: (LOOK around) or (SLEEP and hope it's all a dream) > ")

            if player_input.upper() == "SLEEP":
                print()
                print("You decide to take a nap and hope you wake up at home safe and sound.")
                print("You wake up... still in the forest... Did you really think that was gonna work?")
                print()
            elif player_input.upper() == "LOOK":
                print()
                print("You look around and see your time machine somehow still intact except you notice that one of the power cores is missing!")
                print("Without that power core you won't be able to use your time machine to leave the forest.")
                print()
                return self.look()
            elif player_input.upper() == "QUIT":
                quit = True



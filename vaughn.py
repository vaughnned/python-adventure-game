player_input = ""

class Vaughn:
    
    def __init__(self):
        pass

    def enter(self):
        quit = False
        while not quit:
            player_input = input("Keeping the bear tracks in mind, what will you arm yourself with, should you encounter this bear?: (a big ROCK you found by your feet), (widdle a STICK into a spear) or (your not afraid of some stupid little bear (FISTS)) > ")
            if player_input.upper() == "ROCK":
                print()
                print("You find a decently sized rock by your feet and decide it's your best option in case of a fight. ")
                print("After a few minutes of wandering you see your power core! But.... Remember that bear you were worried about? It's playing with your power core... ")
                print("You decide to use your brain for once and avoid the fight entirely. ")
                print("After sneakily approaching as close as you can get to the bear without alerting it, you throw the rock far away to draw the bear towards the sound. ")
                print("You manage to quickly grab the power core and make it out of the cave. You Win!")
                print()
                quit = True
            elif player_input.upper() == "STICK":
                print()
                print("Using a long stick you found nearby, you spend a few minutes widdling the end into a sharp point, turning it into a spear. ")
                print("After a few minutes of wandering you see your power core! But.... Remember that bear you were worried about? It's playing with your power core... ")
                print("You approach the bear while still keeping your distance. ")
                print("As the bear starts to get angry and attacks you carfully dance around it while getting quick jabs at it's side with your makeshift spear. ")
                print("You've managed to poke the bear enough, without getting injured yourself, to scare the bear away! ")
                print("As you watch the bear scamper away, you grab your power core and prepare to head home. You Win!")
                print()
                quit = True
            elif player_input.upper() == "FISTS":
                print()
                print("You have this sudden rush of foolish bravery and venture into the cave with lots of brawn and very little brain. ")
                print("After a few minutes of wandering you see your power core! But.... Remember that bear you were worried about? It's playing with your power core... ")
                print("But no need to fear! You have two canons for arms that you've brought to protect your self!")
                print("The bear VERY easily wins the fight... You are dead.")
                print()
                quit = True
            elif player_input.upper() == "QUIT":
                quit = True
    
    def yell(self):
        quit = False
        while not quit:
            player_input = input("Would you like to: (make a RUN for the cave) or (try to back up slowly and HIDE in your time machine) > ")
            if player_input.upper() == "RUN":
                print()
                print("You make a run for the cave that you saw earlier. You hear the loud thudding of something chasing you as you sprint for the dark entrance of the cave. ")
                print("As soon as you enter the cave you realize that you no longer hear the thing chasing you. It must be scared of the cave for some reason. ")
                print()
                return self.enter()
            elif player_input.upper() == "HIDE":
                print()
                print("You slowly back away from the creature, once you get close enough you quickly climb into your time machine and slam the door shut just before the creature lunges at you. ")
                print("After an hour or so you finally get the courage to step outside again. Unfortunatley the creature was more patient than you. ")
                print("The creature lunges at you as soon as you step out. You are dead. ")
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
                return self.enter()
            elif player_input.upper() == "CHICKEN":
                print()
                print("You decide to try your luck with the forest once again. You only take a few steps away from the cave before being met with a pair of glowing eyes in the bushes. ")
                print("Your only option is to enter the cave. ")
                print()
                return self.enter()
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
                return self.yell()
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



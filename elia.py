class Elia:
    def __init__(self):
        pass
    def eat(self):
        quit = False
        while not quit:
            player_input = input(
                "You enter the cottage and you see fresh fruit on a table. It looks delicious and you can hear your stomach churning from hunger."
                "Do you EAT an apple or PASS on the fruit?"
            )
            if player_input.upper() == "EAT":
                print()
                print("The apple is laced with Arsenic. You die!")
                print()
                return
            elif player_input.upper() == "PASS":
                print()
                print(
                    "As you explore the cottage you see various useful things to help you survive the next few days."
                )
                print()
                return self.cont()
            elif player_input.upper() == "QUIT":
                quit = True

    def past(self):
        quit = False
        print("You have chosen the PAST and find yourself in the Dark Ages. ")
        while not quit:
            player_input = input(
                "You see a horse in the alley way where you have landed in your time machine. "
                "Do you want to take the HORSE or WALK to start your journey through the PAST? "
            )
            if player_input.upper() == "WALK":
                print(
                    "As you walk down a secluded path, you are led to a gloomy, dark forest. "
                    "You see a small, lonely cottage in the middle of the forest. "
                    "You are hungry and thirsty."
                )
                return self.enter()
            elif player_input.upper() == "HORSE":
                print()
                print(
                    "You climb up on the horse and start your way down the path. The horse takes you towards the town. "
                    "As you reach the outskirts of the town, you stumble upon a joust."
                )
                print()
                return self.fight()
            elif player_input.upper() == "QUIT":
                quit = True

    def fight(self):
        quit = False
        while not quit:
            player_input = input(
                "A brave knight sees you and "
                "challenges you to a fight."
                "Do you choose to FIGHT or REFUSE? "
            )
            if player_input.upper() == "FIGHT":
                print(
                    "You get defeated by the skilled knight and you die from your wounds."
                )
                return
            elif player_input.upper() == "REFUSE":
                print(
                    "You wander into a dark and gloomy forest. You see a small cottage ahead. You are hungry and thirsty"
                )
                return self.enter()
            elif player_input.upper() == "QUIT":
                quit = True

    def enter(self):
        quit = False
        while not quit:
            player_input = input(
                "Do you want to ENTER the cottage or CONT on your journey?"
            )
            if player_input.upper() == "ENTER":
                return self.eat()
            elif player_input.upper() == "CONT":
                return self.take()

    def cont(self):
        quit = False
        while not quit:
            player_input = input(
                "You find a bow and arrow. Do you TAKE the weapon or IGNORE it?"
            )
            if player_input.upper() == "TAKE":
                return self.take()

            elif player_input.upper() == "IGNORE":
                print()
                print(
                    "You end up going days without food or water. You die of starvation."
                )
                print()
                return
            elif player_input.upper() == "QUIT":
                quit = True

    def take(self):
        quit = False
        while not quit:
            player_input = input(
                "You leave the cottage and see a small doe. Do you KILL it or let it LIVE?"
            )
            if player_input.upper() == "KILL":
                print()
                print(
                    "The doe you killed altered the time warp forever. You and the rest of humanity are destroyed."
                )
                return
            elif player_input.upper() == "LIVE":
                print()
                print(
                    "The small doe speaks to you and tells you the secret to immortality."
                    "It has been waiting for you to travel to the past."
                    "You WIN!"
                )
                return
            elif player_input.upper() == "QUIT":
                quit = True

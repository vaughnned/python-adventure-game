class Jay:
        def __init__(self):
            pass
        def future(self):
            print("You have chosen the FUTURE and find yourself in the same lab as before,"
                "only you look at the clock to see only 12 minutes have passed. You look around and see"
                "that a trail of muddy footprints lead from the front of your time machine to right behind it."
                "Do you LOOK closer at the footprints or go ahead and FOLLOW them?")
        def look(self):
            print("You take a closer look at the footprints. Curiously, you place your own foot"
                  "right next to one and confirm your chilling suspicion-- they match your own."
                  "You hear something move in the distance of your lab but are unsure from where."
                  "Do you investigate the NOISE or FOLLOW the footprints?")
        def noise(self):
            print("Cautiously, you look around. You notice the cameras next to your desk on the right"
                  "and the closet door slightly ajar on your left."
                  "Do you go to the CLOSET or take a look at the CAMERAS?")
        def closet(self):
            print("You approach the closet and slowly open the door to find... nothing?"
                  "Well, more than nothing, it seems to be an infinite void and just as you"
                  "start to wonder how a void got in your broom closet, a foot kicks you and you fall"
                  "into the abyss, eternally") #then died
        def cameras(self):
            print("You take a look at the cameras, rewinding until you see someone--yourself, of course." 
                  "You watch as you see yourself pace around then head behind the time machine, and then"
                  "exit out of the time machine. However, there is no entrance to from behind the machine,"
                  "only the core is there... As you begin to realize that there is another you roaming around,"
                  "you hear a scream and are suddenly tackled."
                  "Do you FIGHT blindly or try to ESCAPE?")
        def follow(self):
            print("You follow the footprints behind you time machine, only to discover that the"
                  "plate has been pried off and a knife has been stabbed in the core of the machine."
                  "Your hard work has been sabotaged... but who did it? And why?"
                  "Do you look for CLUES or return to the LAB?")
        def lab(self):
            print("You return to the lab.") ##then noise
        def clues(self):
            print("You look closer at the knife and discover that it's handle is oddly familiar,"
                  "too familiar. Do you get even CLOSER to take a better look or do you simply TAKE the knife?")
        def take(self):
            print("As you reach out to grab the knife you are suddenly tackled and drop it on the floor.") # fight
        def closer(self):
            print("You move to take a closer look. As you squint you notice your initials engraved on the handle."
                  "As you realize that this is in fact your own knife you hear a scream and are tackled to the ground from the side."
                  "Do you FIGHT blindly or try to ESCAPE?")
        def escape(self):
            print("You do your best to escape from you mystery adversary, however it seems you have met your match."
                  "They put you in a headlock and as you struggle to breathe, you catch a glance behind you in the reflection"
                  "of the metal plate on the floor and see your own angry, red face, covered in anguish."
                  "'It's your fault, MY own fault,' you hear yourself say. 'I had to do it to stop it from happening...'" 
                  "you hear as you take your last breath.") #then died
        def fight(self):
            print("You manage to catch your balance. You kick back and manage to hit your adversary right in the knee, making them fall back."
                  "You turn around only to see-- yourself?! But no time to think as they--you?--are starting to get back up."
                  "Do you try to pin them down and make them EXPLAIN themself, or do you RUN?")
        def run(self):
            print("You run. Your run past the lab door, scrambled up the stairs, and burst the door to outside open"
                  "only to see a giant tear the in the sky sucking up everything from the ground up into it.") #survived
        def explain(self):
            print("You pin the doppelganger down, grabbing the knife near you and holding it below their chin."
                  "'Who are you? You have 60 seconds to explain yourself.' You say."
                  "'I'm you, from 3 days from now. *You* had the grand idea to start this whole thing by time traveling, and"
                  "now you've ripped the fabric of our very own reality. There's not much time left, I came back to stop you from traveling"
                  "to where I landed, but every second we keep speaking, the tear grows larger. My chance is gone, it's your turn now."
                  "They grab your hand holding the knife and thats it--you see the life drain from their eyes as you hear"
                  "your heart pounding in your ears. ")

        def died(self):
            print("YOU DIED.")
        def survived(self):
            print("YOU SURVIVED, but at what cost?")

        def play_future(self):
            done = False
            self.future()
            player_input = ""
            while player_input != quit and not done:
                player_input = input(">>")
                if player_input.lower() == "look":
                    self.look()
                elif player_input.lower() == "noise":
                    self.noise()
                elif player_input.lower() == "closet":
                    self.closet()
                    self.died()
                    done = True
                elif player_input.lower() == "cameras":
                    self.cameras()
                elif player_input.lower() == "follow":
                    self.follow()
                elif player_input.lower() == "lab":
                    self.lab()
                    self.noise()
                elif player_input.lower() == "clues":
                    self.clues()
                elif player_input.lower() == "closer":
                    self.closer()
                elif player_input.lower() == "take":
                    self.take()
                    self.fight()
                elif player_input.lower() == "fight":
                    self.fight()
                elif player_input.lower() == "escape":
                    self.escape()
                    self.died()
                    done = True
                elif player_input.lower() == "explain":
                    self.explain()
                    self.survived()
                    done = True
                elif player_input.lower() == "run":
                    self.run()
                    self.survived()
                    done = True

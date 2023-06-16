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
            print("You kick back and manage to hit you adversary right in the knee, making them buckle and ")

        def died(self):
            print("YOU DIED.")
        def survived(self):
            print("YOU SURVIVED, but at what cost?")


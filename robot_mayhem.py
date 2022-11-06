def title():
    print('''
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    !!!*************************!!!
    !!!******ROBOT MAYHEM*******!!!
    !!!*************************!!!
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    ''')
    print("Type 'start' to continue: ")
    global input1
    input1=str(input())
    return input1.lower()

def start():
    print('"The inventions we made \nwill become our downfall"-\n Arnold Shwarzenegger')
    global input2
    input2=input("Type 'y' to continue: ")
    return input2

def intro():
    print("""
    There are flames everywhere. You are lying on the cold floor, your
    ears are ringing because of the explosion. You slowly trying to stand
    up. You are barely standing while you are slowly catch you're breath.
    You look around and all you see is smoke and flames. But from the ashes
    of your laboratory a black skeleton like creature emerges. Its eyes are
    glowing red and its staring at you as its start to walk on your direction.
    Its metallic limbs creeking and you know that it is a deadly robot, 
    designed to kill...
    """)
    global decision1
    decision1=input("a:You start to run like never. b:You try to reason with the hellish machine.: ")
    return decision1

def game_over():
    print("""
    The creature whose creation took the better half of your life 
    is finally catching up to you. Its cold metallic arms bursts 
    your chests and as you are grasping for air it ripped out
    your heart. The last thing you see is its evil dead eyes.
    You almost feel the heat of the hellfire because you know that
    this thing will kill again.""")

def run():
    print("""
    You are turn around and run like never before. Your
    heart beats like a drum, you dont look back, because you know
    its behind you closely. After running for an eternity the maze
    like corridors go into two seperate ways.
    """)
    global decision2
    decision2=input("Which way you go? a:Right b:Left: ")
    return decision2

def right():
    print("""
    The corridor ends in an airwent. You rip open the bars on it
    as you watch your back and see that the robot is only a few 
    meters away. Its running towards you. You squeeze yourself throught
    the narrow vent and stating to crawl forward. Minutes pass
    the vent is dark and cold. You can only hope that it leads somewhere.
    As you start to give up you see a light. You manage to get a sneak peak
    behind the bars and you saw another human with a weapon.
    """)
    global right_decision
    right_decision=input("a:You yell at the mysterious figure hoping for the best b:You stay hidden in the shadows ")
    return right_decision

def approach():
    print("""
    You shout for help towards the stranger. He points his gun
    at you, but after a brief moment he sighs in relief and
    said that he think that youre dead, because of the explosion.
    He help you get out of the vent and pull you out. As you crawl
    out you hear loud noise from the vent. The machine followed you!
    The guard opens fire at the robot while its emerging from the vent.
    The first few rounds do nothing with it but after that the bullets
    started to penetrate its armor. Good that the bulletproof upgrade 
    was still a month away!
    You almost feel sorry for your creation but deep inside you know
    that it has to die. The guard reloaded his weapon and move closer
    to the robot and he shot off its head.
    Its done, the machine is dead. Decades of improvement and countless
    wasted hours, but humanity isn't ready for this.
    """)

def win():
    print("Congratulation! You survived your menacing creation!")

def left():
    print("""
    You run until you reach an automatically opening door.
    you watch behind your back and see that the robot is 
    only a few meters away. Its running towards you. You 
    enter the room and there is a switch which open and 
    closes the door.
    """)
    global left_decision
    left_decision=input("a:close the door b:leave the switch and run ")
    return left_decision

def weapon():
        print("""
        After you closed the door, your hear that the robot is trying
        to get in with force. It wont hold long, but now you have time to
        prepare. You start searching to room and you find a glass case closet.
        Behind you saw a weapon. It could be useful in the upcoming fight. 
        But the glass casing can only be opened with brute force and you 
        can easily bleed out if you're not careful.
        """)
        global weapon_choice
        weapon_choice=input("a: break the casing b:leave the weapon and search for another way out ")
        return weapon_choice

def fight():
    print("""
    You broke throught the glass. There is blood everywhere,
    your own blood, but you manage to get the weapon. Its a
    big f**king gun. The robot manage to open the door and
    gets inside the room. You've never hold a weapon before
    but you are full of rage because you crated this machine
    to help not to kill. It killed all your collegues and it's
    probably messed up your career. You thinking about these things
    as you pull the trigger. The blast from the weapon catches 
    the robot body and it explodes to million little pieces.
    The blast radius from the explosion kick you back onto the wall.
    This was the second explosion that caught you today. Your ears 
    are still ringing from the first. You're hurt and sad, but you're
    alive. As your vision starts to blur you're hearing other people.
    The cavalry is here, you think that before you're passing away.
    You almost feel sorry for your creation but deep inside you know
    that it has to die.
    Its done, the machine is dead. Decades of improvement and countless
    wasted hours, but humanity isn't ready for this.
    """)
#The Game:
title()
if input1:
    start()
    if input2:
        intro()
        if decision1=="b":
            game_over()
        elif decision1=="a":
            run()
            if decision2=="a":
                right()
                if right_decision=="b":
                    game_over()
                elif right_decision=="a":
                    approach()
                    win()
            elif decision2=="b":
                left()
                if left_decision=="b":
                    game_over()
                elif left_decision=="a":
                    weapon()
                    if weapon_choice=="b":
                        print("The robot bursts into the room.")
                        game_over()
                    elif weapon_choice=="a":
                        fight()
                        win()
        else:
            print("Invalid answer")




######################################################
# Alina Hagen
# Room Adventure
# Last Edited: 05/01/2023

# Game Title: Ode to Rhythm: Riddles from the Dark Room
# Game guide and puzzle anwsers at the bottom of the document. 


from Room import Room
#Imported from class handout
import time,sys
######################################################
def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.001)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.001)
  value = input()  
  return value

######################################################
# creates the rooms

# Do Edit descriptions, i changed the AddItem array to have 4 parameters. The first is the item. The second the item description.
# The third is the the grabbable on that item. And then based on if item[2] is in the players inventory, it will/won't print the grabbable description.

def createRooms():
# Source Code With my additions 
    global currentRoom
    n = 100
    # create the room
    living_room = Room("living room")
    kitchen = Room("kitchen")
    basement = Room("basement")
    bedroom = Room ("bedroom")
    bathroom = Room ("bathroom")
    # add exits to Living Room
    living_room.addExit("kitchen", kitchen)
    living_room.addExit("bedroom", bedroom)
    living_room.addExit("basement", basement)
    # add grabbables to Living Room
    living_room.addGrabbable("lilies")
    living_room.addGrabbable("yarn")
    living_room.addGrabbable("physics_book")
    living_room.addGrabbable("rat")
    living_room.addGrabbable("lighter")
    living_room.addGrabbable("candle")
    living_room.addGrabbable("blanket")
    # add items to Living Room
    living_room.addItem("end_table", "The end table is made of sturdy pine, and on it rests a lamp with no lightbulb and a vase ", "lilies", "full of [lilies]")
    living_room.addItem("bookshelf", "The bookshelf is filled with various knick-knacks,", "physics_book", " but one stands out: a theoretical [physics_book]")
    living_room.addItem("front_door", "The front door is painted a dark green with windows frosted at the top. When you try the door, it appears to be locked, or rather, could never have been opened in the first place", " ", " ")
    living_room.addItem("fireplace", "The fireplace, similar to the corner, is barren, not a spec of ash or dust." , 'lighter' ," Besides it rests a [lighter]")
    living_room.addItem("couch", "The couch that you woke up on... it is worn and old.", "blanket", " On it rests a ratty [blanket] covered in a mysterious black fur")
    living_room.addItem("ottoman", "Just infront of the couch is a wooden ottoman.", "yarn", " Underneath is a ball of [yarn].")
    living_room.addItem("corner", "The corner, like the fireplace, is free of dust.","rat", " Curled up in the juncture of the two walls lays a dead [rat]")
    living_room.addItem("window", "The windows are frosted, revealing nothing of what lays outside this cabin..." , "candle", " on the windowsill rests a [candle]")
    living_room.addItem("entity", "A void", " ", " ")
    # add exits to Kitchen
    kitchen.addExit("living_room", living_room)
    # add grabbables to Kitchen
    kitchen.addGrabbable("milk")
    kitchen.addGrabbable("bottle_water")
    kitchen.addGrabbable("tea")
    kitchen.addGrabbable("soda")
    kitchen.addGrabbable("candle")
    # add items to Kitchen
    kitchen.addItem("table", "Nestled besides the counter is a small breakfast nook. On it is a perscription renewal form for painkillers", "tea", " and a mug of steaming orange [tea]")
    kitchen.addItem("counter", "The counter is a dark granite.", "bottle_water", " On it is a [bottle_water]")
    kitchen.addItem("fridge", "There is a note on the fridge that reads 3467.", "soda", " Inside is a can of [soda]")
    kitchen.addItem("cabinet", "The cabinet are made from the same pine as the end table. Inside, not a crumb of food remains.", "candle", " However, inside, weirdly enough, is a [candle]")
    kitchen.addItem("back_door", "Like the front door, the backdoor is locked. You don't beleive it could be opened to begin with.", " ", " ")
    kitchen.addItem("sink", "The sink is void of dishes." ,"milk" , " Except for a glass of [milk]")
    kitchen.addItem("entity", "A void", " ", " ")
    # add exits to Basement
    basement.addExit("living_room", living_room)
    # add grabbables to Basement
    basement.addGrabbable("bag")
    basement.addGrabbable("meat")
    basement.addGrabbable("blanket")
    basement.addGrabbable("candle")
    basement.addGrabbable("boxes")
    # add items to Basement
    basement.addItem("safe", "In the corner of the basement is a small a black safe. It appears to be locked. (To unlock safe, use verb: [unlock])" ," ", " ")
    basement.addItem("shelves", "The shelves in the basement are cluttered.", "boxes", "They are stacked full of cardboard [boxes]. They look unstable")
    basement.addItem("computer_desk", "On the desk is an old PC computer. It is the only technology you've see so far in the cabin. When you try to turn it on, only static greets you."," ", " ")
    basement.addItem("rocking_chair", "In the corner, next to the safe, is an old rocking chair that creaks softly as it titters back and forth." , "blanket", "On it is a wool knit [blanket] with mysterious black fur on it.")
    basement.addItem("entity", "A void", " ", " ")
    basement.addItem("windows", "Windows line the top of the walls. They are frosted, revealing nothing of what lays outside this cabin...", " ", " ")
    basement.addItem("end_table", "Next to the rocking chair is a small end table. ", "candle", "On it is a lone [candle].")
    # add exits to Bedroom
    bedroom.addExit("living_Room", living_room)
    bedroom.addExit("bathroom", bathroom)
    # add grabbables to Bedroom
    bedroom.addGrabbable("clown_fish")
    bedroom.addGrabbable("beta_fish")
    bedroom.addGrabbable("clown_fish")
    bedroom.addGrabbable("beta_fish")
    bedroom.addGrabbable("clown_fish")
    bedroom.addGrabbable("beta_fish")
    bedroom.addGrabbable("clown_fish")
    bedroom.addGrabbable("beta_fish")
    bedroom.addGrabbable("clown_fish")
    bedroom.addGrabbable("beta_fish")
    bedroom.addGrabbable("gold_fish")
    bedroom.addGrabbable("blanket")
    bedroom.addGrabbable("gold_peak_tea")
    bedroom.addGrabbable("candle")
    bedroom.addGrabbable("gold_coin")
    # add items to Bedroom
    bedroom.addItem("bed", "The bed is rumpled and disorganized. ", "blanket", "On it, an intricate [blanket] lays covered in mysterious black fur")
    bedroom.addItem("nightstand", "The nightstand is to the right of the bed. On it is a lamp with no lightbulb, a bedside alarm clock that you cannot read ", "gold_peak_tea", "and a bottle of [gold_peak_tea]")
    bedroom.addItem("fishtank", "To the left of the bed is a bubbling fish tank. ", "gold_fish", "Inside are several [clown_fish], a couple [beta_fish], and 1 [gold_fish].")
    bedroom.addItem("closet","The closet has a sliding linoleum door. Inside are rows of the same black shirt", "candle", "  and a [candle] on the floor]")
    bedroom.addItem("corner","The corner is free of dust. ", "gold_coin", "In the juncture of the two walls lays a [gold_coin]")
    bedroom.addItem("window", "The windows are frosted, revealing nothing of what lays outside this cabin... ", " ", " ")
    bedroom.addItem("entity", "A void", " ", " ")
    # add exits to Bathroom
    bathroom.addExit("bedroom", bedroom)
    # add grabbables to Bathroom
    bathroom.addGrabbable("perscription")
    bathroom.addGrabbable("candle")
    # add items to Bathroom
    bathroom.addItem("cabnit", "The bathroom cabnit creaks as you open it. Inside is an array of bottles and supplies, ", "perscription", "included in which is a [perscription] for pain relief. You think if you take this, your might feel a little better.")
    bathroom.addItem("toliet", "The lid to the toliet is closed. ", "candle", "On it is a [candle]")
    bathroom.addItem("sink", "The sink is full of water, but you cannot see your reflection", " ", " ")
    bathroom.addItem("entity", "A void", " ", " ")
    # set room 1 as the current room at the beginning of the game
    currentRoom = living_room
    return currentRoom



######################################################
def gamertime(life, blanket, candle):
# In this subroutine, i added alot of verbs. Some to add more fun stuff (the candle and blanket acheievements)
# some for puzzles (unlock)
# some beacuse the people who play tested this for me wanted to eat everything. or burn books. So i added those verbs for fun.
# Print verbs as an easy way to see all valid verbs

# Source Code With my additions 
    currentRoom=createRooms()
    while (True):
        status = "{}\nYou are carrying: {}\nCurrent HP: {}".format(currentRoom, inventory,life)
        if (currentRoom == None):
            status = "You are dead."
        print("=========================================")
        print(status)
        if (currentRoom == None):
            death()
            break
        action = input("What do you want to do? ")
        action = action.lower()
        if (action == "quit" or action == "exit" or action == "bye"):
            break
        response = "I don't understand. Try verb noun. Valid verbs are go, look, and take"
        words = action.split()
        if (len(words) == 2):
            verb = words[0]
            noun = words[1]
            if (verb == "go"):
                response = "Invalid exit."
                for i in range(len(currentRoom.exits)):
                    if (noun == currentRoom.exits[i]):
                        currentRoom =  currentRoom.exitLocations[i]
                        response = "Room changed."
                        break
            elif (verb == "look"):
                response = "I don't see that item."
                for i in range(len(currentRoom.items)):
                    if (noun == currentRoom.items[i]):
                        response = currentRoom.itemDescriptions[i]
                        if currentRoom.itemGrabs[i] not in inventory: #I added this to edit description
                            response += currentRoom.grabDesc[i]
                        break   
            elif (verb == "take"):
                response = "I don't see that item."
                for grabbable in currentRoom.grabbables:
                    if (noun == grabbable):
                        if noun == "gold_fish": # I added this based on the original Take verb action
                            inventory.append(grabbable)
                            currentRoom.delGrabbable(grabbable)
                            response =("You grab the fish, it flops around in your hands. The other fish swim away in fear " +"\n")
                            break
                        if noun == "boxes": # I added this based on the original Take verb action
                            inventory.append(grabbable)
                            currentRoom.delGrabbable(grabbable)
                            response =("The boxes fall onto you, ouch!" +"\n")
                            life -= 1
                            break
                        if noun == "blanket": # I added this based on the original Take verb action
                            blanket +=1
                            inventory.append(grabbable)
                            currentRoom.delGrabbable(grabbable)
                            response =("Item grabbed")
                            break
                        if noun == "perscription": # I added this based on the original Take verb action
                            inventory.append(grabbable)
                            currentRoom.delGrabbable(grabbable)
                            response =("Item grabbed: To use perscription, type [use perscription]")
                            break
                        else: #Original
                            inventory.append(grabbable)
                            currentRoom.delGrabbable(grabbable)
                            response = "Item grabbed."
                            break
            elif (verb == "talk"): #I addded this verb based on the original ones 
                response = "I don't see that item."
                for i in range(len(currentRoom.items)):
                    if (noun == currentRoom.items[i]):
                        response = "Leaving Now"
                        typingPrint("\n{}".format(response) + "\n")
                        return life, blanket, candle
            elif (verb == "light"): #I addded this verb based on the original ones 
                response = "You do not have a lighter."
                if "lighter" in inventory: 
                    for grabbable in currentRoom.grabbables:
                        response = "I don't see that item."
                        if (noun == "candle"):
                            candle +=1
                            response = 'You light the candle, it burns gently, illuminating the room.'
                            break
            elif (verb == "unlock"): #I addded this verb based on the original ones 
                response = "I don't see that item."
                for grabbable in currentRoom.grabbables:
                    if (noun == "safe"):
                        code = int(input("Code: "))
                        if code == 3467:
                            if "meat" not in inventory:
                                response ='Inside the safe is a small [bag]. Inside appears to be dehydrated meat. Maybe it\'s edible? '
                                break
                            else:
                                response = "The safe is now empty."
                                break
                        else:
                            response ="ERROR: CODE INCORRECT"
                            break
                    else:
                        response = "'Invalid Noun. What are you trying to unlock?'"
                        break
            elif (verb == "print"): #I addded this verb based on the original ones 
                response = "Invalid verb."
                verbs = ["Go","Take","Look", "Talk", "Unlock", "Light", "Eat", "Burn", "Use"]
                if (verb == "print"):
                    response = ""
                    for i in range(len(verbs)):
                        response += verbs[i] + " "
            elif (verb == "eat"): #I addded this verb based on the original ones 
                response = "I don't see that item."
                for grabbable in currentRoom.grabbables:
                    if (noun == grabbable):
                        response =("Blehhh, that doesn't taste right... Maybe don't try to eat here" +"\n")
                        life -= 1
                        break
            elif (verb == "burn"): #I addded this verb based on the original ones 
                response = "I don't see that item."
                for grabbable in currentRoom.grabbables:
                    if (noun == grabbable):
                        currentRoom.delGrabbable(grabbable)
                        response = ("You set fire to {}. It crumbles away in your hands. I hope that wasn't something important".format(noun))
                        break
            elif (verb == "use"): #I addded this verb based on the original ones 
                response = "I can't use this item"
                for grabbable in inventory:
                    if (noun == grabbable):
                        if noun == "perscription":
                            inventory.remove(grabbable)
                            response =("That feels better" +"\n")
                            life += 1
                            break
        typingPrint("\n{}".format(response) + "\n")
        
        
  
def giveItem(thing, life, blanket, candle):
# I created this subroutine to mediate giving my main antogonist the items he wanted. I used the original code provided for take, and modified it to instead be a give feature
# Based on Source Code
    blanket = blanket
    candle = candle
    while True:
        action = input("What do you do? ")
        action = action.lower()
        if (action == "quit" or action == "exit" or action == "bye"):
            response = "Goodbye"
            typingPrint("\n{}".format(response) + "\n")
            return  
        words = action.split()
        if (len(words) == 2):
            verb = words[0]
            noun = words[1]
            if (verb == "give"):
                response = "I don't see that item."
                for i in range(len(inventory)):
                    if noun not in inventory:
                        typingPrint("\n" + "You can't give me something you don't have" + "\n")
                        break
                    else:
                        if (thing == noun):
                            inventory.remove(noun)
                            typingPrint("\n" "You give the item to the entity" + "\n")
                            stats(life)
                            return life, blanket, candle
                        else:  
                            life -=1
                            typingPrint("\n" + "Thats not what i asked for" + "\n")
                            stats(life)
                            while True:
                                again = typingInput("Would you like to try another item? Yes or No: ")
                                again=again.lower()
                                if again == "yes":
                                    break
                                elif again == "no":
                                    again = typingInput("Would you like to return to the room? Yes or No: ")
                                    again = again.lower()
                                    if again == "yes":
                                        while True:
                                            game = gamertime(life, blanket, candle)
                                            life = game [0]
                                            blanket = game [1]
                                            candle = game [2]
                                            time.sleep(0.5)
                                            response = typingInput("Do you have the item I want? Yes or No: ")
                                            if response == "yes":
                                                break
                                            if response == "no":
                                                print("I suggest you go find it then")
                                                continue
                                    elif again == "no":
                                        print("Dev: Well I guess we will just sit here then.")
                                        time.sleep(1)
                                        print("Dev: I didn't know what to program if you didn't have the item and didn't want to go back to the room.")
                                        time.sleep(1)
                                        print("Would you like to just... continue the game? Even though you didn't complete the riddle?")
                                        response = typingInput("Yes or No: ")
                                        response=response.lower()
                                        if response == "yes":
                                            return life, blanket, candle
                                        elif response == "no":
                                            print("Dev: Just restart the program then. Or don't. I don't know what you want")
                                    else:
                                        print("Invalid Response. Please try again.")
                                        continue
                                    break 
                                else:
                                    print("Invalid Response. Please try again.")
                                    continue
                            break
                        continue
            else:
                response= "Invalid verb. Please respond using the following template: *Give ___*"
                print(response)
                continue
            
def stats(life): #can only use this for living room stats
# Based on Source Code
    currentRoom= "living room"
    status = "{}\nYou are carrying: {}\nCurrent HP: {}".format(currentRoom, inventory, life)
    print("=========================================")
    print(status + "\n")
    return

def hint (hints, answer):
# There were multiple points were the player could ask for a hint, So i made a subroutine to streamline that
# My Code
    while True:
        response=str(input("What do you do? "))
        response = response.lower()
        if response == "a":
            if hints == 1:
                typingPrint('"Not this time,  Go, take a look. You are smart."' + "\n")
                return hints 
            elif hints == 0:
                typingPrint('{}'.format(answer) + "\n")
                hints +=1
                return hints
        elif response == "b":
            return hints 
        else:
            print("Invalid Response. Please try again.")
            continue
        

def riddleTime (thing, confirm, life, blanket, candle):
# This mediated the entire process when the player is looking for objects and giving things to the entity.
# My Code 
    while True:
        game = gamertime(life, blanket, candle)
        life = game[0]
        blanket = game [1]
        candle = game [2]
        response = typingInput("Do you have the item I want? Yes or No: ")
        time.sleep(0.5)
        if response == "yes":
            item= giveItem(thing, life, blanket, candle)
            life = item[0]
            blanket = item [1]
            candle = item [2]
            typingPrint("\n" + " The entity chuckles has you hand it the {}.".format(thing) + "\n"
                        '{}'.format(confirm))
            return life, blanket, candle
        elif response == "no":
            print("I suggest you go find it then")
            continue            


def acheivements(candle, blanket,anger, life, pet, sleep):
# I thought it would be fun to have a hidden acheivements list
# My Code
    acheivement_list = []
    missed = []
    if pet == 1:
        acheivement_list.append("Soft Kitty: Pet the Cat")
    else:
        missed.append("Soft Kitty: Pet the Cat")
    if candle == 5:
        acheivement_list.append("Warm Kitty: Light all Candles")
    else:
        missed.append("Warm Kitty: Light all Candles")
    if blanket == 3:
        acheivement_list.append("Little Ball of Fur: Collect all Blankets")
    else:
        missed.append("Little Ball of Fur: Collect all Blankets")
    if anger == 0:
        acheivement_list.append("Happy Kitty: Finish the game with an anger rating of 0")
    else:
        missed.append("Happy Kitty: Finish the game with an anger rating of 0")
    if sleep ==1:
        acheivement_list.append("Sleepy Kitty: Finish the game with the Good Ending.")
    else:
        missed.append("Sleepy Kitty: Finish the game with the Good Ending.")
    if life == 5:
        acheivement_list.append("Purr, Purr, Purr: Finish the game with a HP of 5")
    else:
        missed.append("Purr, Purr, Purr: Finish the game with a HP of 5")
    print("Achievements Earned:")
    for i in range(len(acheivement_list)):
        typingPrint(acheivement_list[i] + "\n")
    print ('\n')
    print("Achievements Missed: ")
    for i in range(len(missed)):
        print(missed[i] +'\n')

def credit():
#My Code
    typingPrint ('Writing and Development: Ali'+"\n")
    typingPrint ('Programing: Ali '+"\n")
    typingPrint ('Story Development: Ali / Jonah T.'+"\n")
    typingPrint ('A speacial thanks to Gabbi, Emily, Brooke, Alex, Jonah, and Brenden for play testing during development'+"\n")


##############################################
# Main Game
inventory = [] 
createRooms()
life = 5
hints = 0
anger = 0
candle = 0
blanket = 0
dream = 0
pet = 0
sleep = 0
# Initializing variables i needed to make the game work


# While life is above 0, the game plays. When life hits 0, The game ends
#The text While loops all follow the same general format. Input -> if input equals a, then b. the break. and repeat
#Text While loops was my coding
while life > 0:

    typingPrint(r"You awaken, lying on a couch in a dark room barely illuminated by some unknown light source." + "\n"
                "Around you, crickets chirp, and the house creaks and groans as its foundation settles and shifts." + "\n")
    time.sleep(1)
    typingPrint("You awake... confused. Where are you? And when did you fall asleep? Or better yet... who are you?" +"\n")
    time.sleep(0.5)
    typingPrint("As you sit up and muse these questions, a voice speaks out from the darkness, its origin unknown." +"\n")
    time.sleep(0.5)
    typingPrint("\n" + "\"I see you're finally awake. You've been asleep for a long while now.\"" + "\n")
    time.sleep (1)

    print (r'Response A: "Who are you."' + "\n"
           'Response B: \"Where am I?\"'+ "\n"
           "Response C: Stay Quiet"+ "\n")
    print ("To select a response, type [letter(a, b, c, etc)]")

    while True:
        response=str(input("What do you do? "))
        response = response.lower()
        if response == "a":
            typingPrint(r'"Who I am is not important. What matters more is you and your purpose here.' + "\n"
                        'I\'ve been waiting for you to wake up, and with you now conscious, we can finally begin.\"' + "\n")
            break
        elif response == "b":
            typingPrint(r'"Where you are… well, that is a complicated matter. I would not focus on that too much.' + "\n"
                        "What matters more is you and your purpose here. I've been waiting for you to wake up, and with you now conscious, we can finally begin.\"" + "\n")
            break
        elif response == "c":
            typingPrint("\"Not very talkative, I see. I had hoped for more… energetic company, I suppose.\"" + "\n")
            time.sleep(0.5)
            print (r'Response A: "Who are you."' + "\n"
               'Response B: \"Where am I?\"'+ "\n"
               "Response C: Stay Quiet"+ "\n")
            while True:
                response=str(input("What do you do? "))
                print("\n")
                response = response.lower()
                if response == "a":
                    typingPrint(r'"Who I am is not important. What matters more is you and your purpose here.' + "\n"
                                'I\'ve been waiting for you to wake up, and with you now conscious, we can finally begin.\"' + "\n")
                    break
                elif response == "b":
                    typingPrint(r'"Where you are… well, that is a complicated matter. I would not focus on that too much.' + "\n"
                            "What matters more is you and your purpose here. I've been waiting for you to wake up, and with you now conscious, we can finally begin.\"" + "\n")
                    break
                elif response == "c":
                    typingPrint("\"Fine then, if you're going to be like that. I guess it doesn't matter, really, in the grand scheme of things." + "\n"
                                "What matters more is you and your purpose here. I've been waiting for you to wake up, and with you now conscious, we can finally begin." + "\n")
                    break
                else:
                    print("Invalid Response. Please try again.")
                    continue
            break
        else:
            print("Invalid Response. Please try again.")
            continue
        
    time.sleep(0.5)
    print("\n")
    typingPrint(r"The voice of this entity seems to be coming from an armchair across the room." + "\n"
                'However, with the lack of light, you cannot determine what is speaking to you.' + "\n")
    time.sleep(0.5)
    typingPrint("\n" +'"I know you are confused. The others always were, in the beginning, at the very least."' + "\n")
    time.sleep(1)
    print (r'Response A: "Others?"' + "\n"
           'Response B: "About that purpose..?"'+ "\n")

    while True:
        response=str(input("What do you do? "))
        response = response.lower()
        if response == "a":
            typingPrint("\"Oh yes, you aren't the first to pass through here. With any luck, you will be the last. But we see how that turned out for the rest of them.\"" + "\n")
            break
        elif response == "b":
            typingPrint("\"You are no fun, you know that.\"" + "\n")
            time.sleep(0.5)
            print (r'Response A: "Its kinda hard to have fun when you do not know who you are or where you are."' + "\n"
                   'Response B: "Sorry..."'+ "\n"
                   'Response C: Stay Quiet.' + "\n")
            while True:
                response=str(input("What do you do? "))
                response = response.lower()
                if response == "a":
                    typingPrint('"I don\'t see how that\'s my problem. Sounds like a skill issue. If you let me continue, you could learn something."')
                    anger += 1
                    time.sleep(0.5)
                    typingPrint("[The Entity will remember this.]" + "\n")
                    print("\n")
                    break
                elif response == "b":
                    typingPrint("\"You should be. Now, where was I?\"" + "\n")
                    break
                elif response == "c":
                    break
                else:
                    print("Invalid Response. Please try again.")
                    continue
            break
        else:
            print("Invalid Response. Please try again.")
            continue
        
    time.sleep(1)
    print("\n")
    typingPrint(r'"Your purpose for being here is rather simple. I have things that I want. And you must find them."' + "\n"
                "\"Consider this a test. If you play along, perhaps you will learn something. About yourself, about this place, that's up to you.\"" + "\n")
    time.sleep (0.5)
    typingPrint("\n" +"\"Now you can refuse. But I don't recommend it. I would hate to cut our conversation short.\"" + "\n")
    time.sleep (1)
    print("Do you accept?")
    print("Response A: Yes")
    print("Response B: No" +"\n")


    while True:
    #This does just end the game if your say B. I thought it would be funny you could just refuse to play and die
        response=str(input("What do you do? "))
        response = response.lower()
        if response == "a":
            break
        elif response == "b":
            typingPrint ('"Well... Goodbye then.'+"\n")
            time.sleep(0.5)
            typingPrint ('"As you awaken, the memories of what happened in the cabin are already fading.'+"\n")
            time.sleep(0.25)
            typingPrint ('"You get the sense that you\'ve lost something important'+"\n")
            credit()
            quit()
        else:
            print("Invalid Response. Please try again.")
            continue

    typingPrint('"Great. Let us begin then," The entity purrs.' +"\n")
    print("\n")
    time.sleep (1)
    typingPrint("\"They say that there are 13 cries in the rhythm of life. The first cry is for sorrow. This is the involuntary cry. The one that is ripped from us in the beginning.\"" + "\n"
                "\"It is a cry to be soothed. This is the first cry, and one that is the first repeated, again and again and again.\"" + "\n")
    time.sleep(0.5)
    print (r'Response A: "What does this have to do with your test?"' + "\n"
           'Response B: "I\'ve never cried like that."'+ "\n"
           "Response C: \"That sounds very lonely.\""+ "\n"
           "Response D: Stay Quiet" + "\n")

    while True:
        response=str(input("What do you do? "))
        response = response.lower()
        if response == "a":
            typingPrint('"Everything. It has everything to do with the test." The entity growls, "If you let me continue, maybe you\'ll see why."' + "\n")
            time.sleep(0.5)
            typingPrint("[The Entity will remember this.]" + "\n")
            anger +=1
            break
        elif response == "b":
            typingPrint('"You have; you just don\'t remember. Well, you don\'t remember a lot right now, I suppose."' + "\n")
            break
        elif response == "c":
            typingPrint('"Perhaps. But it is the first that leads to the next."' + "\n")
            break
        elif response == "d":
            break
        else:
            print("Invalid Response. Please try again.")
            continue

    time.sleep(0.5)
    typingPrint('"The second cry is much different. This one signifies something much more joyous. Two cries is mirth, it is play, it is excitement in rhythm."' + "\n")
    time.sleep(1)
    typingPrint("\n" + "The entity pauses. And despite the silence, you can hear its smirk." + "\n")
    time.sleep(0.5)
    typingPrint("\n"+ '"This is your first test. Find me something to embody this mirth, the joy in play. You will find it in this room if you look."' + "\n")
    time.sleep(0.5)
    print (r'Response A: "Can I have a hint?"' + "\n"
           'Response B: Get up and Look'+ "\n")

    anwser = '"Just this once, I suppose. Here is your hint: I have never been one for reading."'
    hints = hint(hints,anwser)
        
    time.sleep(1)
    print("\n")
    print("To select an action, type: [VERB] [NOUN], using an underscore '_' for any spaces in the noun. Basic Verbs are: Go, Take, Look")
    print("To return to the speach panel, type: [Talk Entity], to give an item, type [give ____]")
    print("To print a list of *all* valid verbs, type: [print verbs]")
    print("\n")
    time.sleep(1)

#Brings the player to the Room Subroutines and allows them to move around. Thing and Confirm are the items that the player is looking for 
    thing = "yarn"
    confirm = '"This most defiently embodies mirth. Very good. Let us continue then."'
    riddle= riddleTime(thing, confirm, life, blanket, candle)
#Reinitialize acheievement variables
    life = riddle[0]
    blanket = riddle [1]
    candle = riddle [2]
    if life == 0:
        break
    
        
    print("\n")
    time.sleep(0.5)
    typingPrint('"The third cry is for a wedding. A momentous shift in rhythm. A day that builds on the first and the second."' + "\n"
                '"A sorrowful joyous day of new beginnings and starts. A nightmare of a day and a daydream of a night."' + "\n")
    time.sleep(0.5)
    print (r'Response A:"A dream?"' + "\n"
           'Response B: "What does marriage have to do with your test?"'+ "\n"
           'Response C: "Did you know that divorce rates for first marriages in the US are upwards of 40-50%?"'+ "\n"
           "Response D: Stay Quiet" + "\n")

    while True:
        response=str(input("What do you do? "))
        response = response.lower()
        if response == "a":
            typingPrint('"A lovely dream, is it not? Or a frightening nightmare. It\'s a test of rhythm in the end."' + "\n"
                        'As the Entity responds, you start to wonder... dream..? test...? The Entity continues as you muse these thoughts.' + "\n")
            dream+=1
            break
        elif response == "b":
            typingPrint('"Everything and Nothing. This is your test, after all, not mine. What do you think it means?"' + "\n")
            time.sleep(0.5)
            print (r'Response A: "Was I married?"' + "\n"
               'Response B: "I think this is dumb."'+ "\n"
               "Response C: Stay Quiet" + "\n")
            while True:
                response=str(input("What do you do? "))
                response = response.lower()
                if response == "a":
                    typingPrint('"Perhaps. Perhaps not. You could have been, or you could still be looking. Who knows, not you, apparently."' + "\n")
                    print (r'Response A:  "Are you being difficult on purpose?"' + "\n"
                           'Response B: "You are really starting to get on my nerves."'+ "\n"
                           'Response C:  "Haha, laugh it up."' + "\n"
                           "Response D: Stay Quiet" + "\n")
                    while True:
                        response=str(input("What do you do? "))
                        response = response.lower()
                        if response == "a":
                            typingPrint('"Oh, absolutely I am. Consider it… payback."' + "\n")
                            print (r'Response A: "Payback?"' + "\n"
                                   'Response B: Stay Quiet'+ "\n")
                            while True:
                                response=str(input("What do you do? "))
                                response = response.lower()
                                if response == "a":
                                    typingPrint('"Oh, never mind that we have a test to finish."' + "\n")
                                    break
                                elif response == "b":
                                    typingPrint('"Let us continue then."'+"\n")
                                    break
                                else:
                                    print("Invalid Response. Please try again.")
                                    continue
                            break
                        elif response == "b":
                            typingPrint('"Consider the regard mutual, human." The Entity growls, "May I continue, or do you want to opt-out now?"' +"\n")
                            time.sleep(0.5)
                            typingPrint("[The Entity will remember this.]" + "\n")
                            print (r'Response A: Continue' + "\n"
                                   'Response B: Opt-out'+ "\n")
                            anger +=1
                            while True:
                                response=str(input("What do you do? "))
                                response = response.lower()
                                if response == "a":
                                    break
                                elif response == "b":
                                    typingPrint ('"Well... Goodbye then.'+"\n")
                                    time.sleep(0.5)
                                    typingPrint ('"As you awaken, the memories of what happened in the cabin are already fading.'+"\n")
                                    time.sleep(0.25)
                                    typingPrint ('"You get the sense that you\'ve lost something important'+"\n")
                                    credit()
                                    quit()
                                else:
                                    print("Invalid Response. Please try again.")
                                    continue
                            break
                        elif response == "c":
                            typingPrint ('"Trust me, I am. Let us continue."' + "\n")
                            break
                        elif response == "d":
                            typingPrint('"Well then, let us continue."' +"\n")
                            break
                        else:
                            print("Invalid Response. Please try again.")
                            continue
                    break
                elif response == "b":
                    typingPrint('"Says the person who does not know who or where they are. You don\'t even know what game you are playing or its rules."' +"\n"
                                '"I advise considering your position before you speak next." The Entity growls.' + "\n"
                                'Without waiting for your affirmation, the Entity continues.' + "\n")
                    anger +=1
                    time.sleep(0.5)
                    typingPrint("[The Entity will remember this.]" + "\n")
                    break
                elif response == "c":
                    break
                else:
                    print("Invalid Response. Please try again.")
                    continue
            break
        elif response == "c":
            typingPrint('"... how do you remember that? You know what, never mind, you pessimist. Just listen to the tale."' + "\n")
            break
        elif response == "d":
            break
        else:
            print("Invalid Response. Please try again.")
            continue

    print("\n")
    time.sleep(0.5)
    typingPrint('"A birth heralds the fourth cry, and now the cycle continues with a new rhythm. New life, brought forward from the previous three cries.' + "\n"
                'The fourth is seldom repeated, no more than a handful of times in rhythm, but such is life, the ebb and flow of rhythm. "'+"\n")
    time.sleep(0.5)
    typingPrint('"This is your second test. Find me a drink that will remind me of my youthful days. You will find it in the kitchen."'+"\n")
    time.sleep(0.5)
    print (r'Response A:"Can I have a hint?"' + "\n"
           'Response B: Get up and look'+ "\n")

    answer = '"Just this once, I suppose. Here is your hint: What is the first thing you ever drank?"'
    hints = hint(hints, answer)

#Brings the player to the Room Subroutines and allows them to move around. Thing and Confirm are the items that the player is looking for 
    thing = "milk"
    confirm = '"This most defiently reminds me of my youth. Very good, most refreshing. Let us continue then."'
    riddle= riddleTime(thing, confirm, life, blanket, candle)
# Reinitialize achievement variables
    life = riddle[0]
    blanket = riddle [1]
    candle = riddle [2]
    if life == 0:
        break
        
    print("\n")
    time.sleep(0.5)
    typingPrint(r"The Fifth and Sixth cries are for silver and gold. It is for good fortune, riches throughout rhythm." + "\n"
                "These cries are often the loudest. Wailing, piercing cries. Desperate. But with these cries comes sacrifice." + "\n"
                "Do you remember what you sacrificed?" + "\n")
    time.sleep(0.5)
    print (r'Response A:"What?"' + "\n"
           'Response B: "I haven\'t sacraficed anything"'+ "\n"
           'Response C: "Can you tell me"'+ "\n"
           "Response D: Stay Quiet" + "\n")

    secret = 0

    while True:
        response=str(input("What do you do? "))
        response = response.lower()
        if response == "a":
            typingPrint('"Ahh. I should have expected this. Nevermind that then."' + "\n")
            time.sleep(0.5)
            print (r'Response A: "No, tell me. Please"' + "\n"
                   'Response B: Stay Quiet'+ "\n")
            while True:
                response=str(input("What do you do? "))
                response = response.lower()
                if response == "a":
                    typingPrint('The entity quiets for a moment, before responding: "Time. You sacrificed time that which was already limited.' + "\n"
                                '"But, let us continue. No need to keep them waiting longer than they already have"' + "\n"
                                "You swear that the entity sounds. . . sad. But that can't be right." + "\n")
                    secret +=1
                    anger -= 1
                    time.sleep(0.5)
                    typingPrint("[The Entity will remember this.]" + "\n")
                    time.sleep(0.5)
                    print (r'Response A:"Is that what this is about then? I sacrificed something?"' + "\n"
                           'Response B:  Stay Quiet'+ "\n")
                    while True:
                        response=str(input("What do you do? "))
                        response = response.lower()
                        if response == "a":
                            typingPrint('"Perceptive. A sacrifice was made yes."' +"\n"
                                        '"But, let us continue. No need to keep them waiting longer than they already have."' + "\n")
                            break
                        elif response == "b":
                            typingPrint('The Entity continues' + "\n")
                            break
                        else:
                            print("Invalid Response. Please try again.")
                            continue
                        break
                    else:
                        typingPrint('"Just this once, I suppose. Here is your hint: What is the first thing you ever drank?"' + "\n")
                        break
                    break
                elif response == "b":
                    break
                else:
                    print("Invalid Response. Please try again.")
                    continue
            break
        elif response == "b":
            typingPrint('"Oh but you have. You did. You wouldn not be here if you hadn\'t."' + "\n")
            print (r'Response A:"Well are you going to tell me then?"' + "\n"
                   'Response B: "Don\'t remember. Didn\'t happen."'+ "\n"
                   'Response C: "Is that what this is about then? I sacrificed something and now this is my punishment?"'+ "\n"
                   "Response D: Stay Quiet" + "\n")
            while True:
                response=str(input("What do you do? "))
                response = response.lower()
                if response == "a":
                    typingPrint('"I don\'t think I will. This is a test after all. Remember it yourself."' + "\n")
                    break
                elif response == "b":
                    typingPrint('You feel anger radiating off of the entity. "Typical."' + "\n"
                                'The entity continues. Malice permeating their tone. ' + "\n")
                    anger +=3
                    time.sleep(0.5)
                    typingPrint("[The Entity will *really* remember this.]" + "\n")
                    break
                elif response == "c":
                    typingPrint('"Punishment? No. This is an intervention. But I can see why you would see it that way, human." The entity growls.' + "\n"
                                "Pray you learn something before the rhythm runs its course. That would be punishment." + "\n"
                                'The entity continues.' + "\n")
                    time.sleep(0.5)
                    typingPrint("[The Entity will remember this.]" + "\n")
                    anger +=1
                    secret +=1
                    break
                elif response == "d":
                    break
                else:
                    print("Invalid Response. Please try again.")
                    continue
            break
        elif response == "c":
            typingPrint('"If I tell you, then what point does the test have? The answers are here if you listen."' + "\n")
            break
        elif response == "d":
            break
        else:
            print("Invalid Response. Please try again.")
            continue

    print("\n")
    time.sleep(0.5)
    typingPrint('"The seventh cry is for a secret. One that should not be missed. This is your next test.' + "\n"
                ' The previous person hid something from me in the basement. I want you to find it, and give it to me."'+"\n")
    time.sleep(0.5)
    print (r'Response A:"Can I have a hint?"' + "\n"
           'Response B: Get up and look'+ "\n")

    anwser = '"Just this once, I suppose. Here is your hint: It\'s well protected"'
    hints= hint(hints, anwser)

#Brings the player to the Room Subroutines and allows them to move around. Thing and Confirm are the items that the player is looking for 
    thing = "meat"
    confirm = '"Ahh, there it is... *crunch*... As delicious as I remember. Let us continue" The entity purrs with content"'
    riddle= riddleTime(thing, confirm, life, blanket, candle)
#Reinitialize achievement variables
    life = riddle[0]
    blanket = riddle [1]
    candle = riddle [2]
    if life == 0:
        break
        
        
    print("\n")
    time.sleep(0.5)
    typingPrint(r'"The eighth cry is for a wish, a desire to be heard. This cry can be received or given."' + "\n"
                '"But it is your choices that dictate how the eighth cry carries throughout rhythm."' + "\n")
    time.sleep(0.5)
    print(r'Response A:"Its like asking for help."' + "\n"
           'Response B: "Well here\'s my desire to be heard: Can I go home yet?"'+ "\n"
          'Response C: Stay Quiet"')
    if secret >= 1:
        print('Response D: "Can you tell me more about what you said earlier? You mentioned another rhythm, I\'m here because of someone else?"' +"\n"
              '"Someone that to be heard?"'+ "\n")


    while True:
        response=str(input("What do you do? "))
        response = response.lower()
        if response == "a":
            typingPrint('"In a way yes, but not exactly. A wish can be anything. Help, Money, Opportunity. Attention. It depends on the one who lets their desire be heard."' + "\n")
            break
        elif response == "b":
            typingPrint('The entity seethes as it answers. "Sure, just answer this last question: Where is home?"' + "\n")
            time.sleep(0.5)
            print (r'Response A:"Its... Damn it"' + "\n"
                   'Response B: "..."'+ "\n"
                   'Response C: That\'s not fair."' +"\n")
            while True:
                response=str(input("What do you do? "))
                response = response.lower()
                if response == "a" or response == "b":
                    typingPrint('"That\'s what I thought, human"' + "\n")
                    anger +=1
                    break
                elif response == "c":
                    typingPrint('""It\'s not my fault you don\'t know. Guess we are going to continue"' + "\n")
                    break
                else:
                    print("Invalid Response. Please try again.")
                    continue
            break
        elif response == "c":
            break
        elif response == "d":
            typingPrint('The entity pauses. "I knew you were smart. I never doubted that. We should continue. You still have one more riddle.""'+"\n")
            anger -=1
            break
        else:
            print("Invalid Response. Please try again.")
            continue

    print("\n")
    time.sleep(0.5)
    typingPrint(r'"The ninth and tenth cries signify a goodbye. The Ninth is for a kiss, the parting gift. The tenth, a feline to revel in miss."' + "\n"
                '"Two sides of a coin of exchange: the parting and the parted. The ninth and tenth cries are the most common in rhythm, often repeated with pattern and certainty."' + "\n")
    time.sleep(0.5)
    print("\n")
    typingPrint('The entity continues before you can offer an input'+'\n')
    print("\n")
    time.sleep(0.5)
    typingPrint(r'"The eleventh cry is for health, for however long lasting. Like the eighth, this cry is a desire, but quieter. "' + "\n"
                '"More personal. The Eleventh cry is a desire for rhythm to continue onwards and upwards."' + "\n")
    time.sleep(0.5)
    if life == 1:
        typingPrint('"You don\'t look well. I would check the bathroom. Maybe you\'ll find something to aid your wavering rhythm."')
        time.sleep(0.5)
        print(r'Response A:"Thanks for the advice"' + "\n"
               'Response B: Stay Quiet'+ "\n") 
        while True:
            response=str(input("What do you do? "))
            response = response.lower()
            if response == "a":
                anger -=1
                break
            elif response == "b":
                break
            else:
                print("Invalid Response. Please try again.")
                continue
            
    print("\n")
    time.sleep(0.5)
    typingPrint(r'"Where the fifth and sixth were silver and gold, the twelfth is for something much more valuable. Wealth is something that looks different to everyone."' + "\n"
                '"Wealth in riches, Wealth in knowledge. Wealth can be a very personal achievement."' + "\n")
    time.sleep(0.5)
    typingPrint('"This is your final riddle. Find me something so that I may be wealthy in my own right. You will find it in the bedroom."'+'\n')
    time.sleep(0.5)
    print (r'Response A:"Can I have a hint?"' + "\n"
           'Response B: Get up and look'+ "\n")

    while True:
        response=str(input("What do you do? "))
        response = response.lower()
        if response == "a":
            if hints == 1:
                typingPrint('"Not this time,  Go, take a look. You are smart."' + "\n")
                print (r'Response A:"Please, I\'m really confused' + "\n"
                       'Response B: Get up and look'+ "\n")
                while True:
                    response=str(input("What do you do? "))
                    response = response.lower()
                    if response == "a":
                        typingPrint('"Fine. Here is your hint: Consider the sixth"' + "\n")
                    elif response == "b":
                        break
                    else:
                        print("Invalid Response. Please try again.")
                        continue
                break
            elif hints == 0:
                typingPrint('"Just this once, I suppose. Here is your hint: Consider the sixth"' + "\n")
                hints +=1
                break
        elif response == "b":
            break
        else:
            print("Invalid Response. Please try again.")
            continue

#Brings the player to the Room Subroutines and allows them to move around. Thing and Confirm are the items that the player is looking for 
    thing = "gold_fish"
    confirm = '"Ahh, there it is... this does make me wealthy, amongst my own" The entity purrs with content' 
    riddle= riddleTime(thing, confirm, life, blanket, candle)
# Reinitialize acheivement variables 
    life = riddle[0]
    blanket = riddle [1]
    candle = riddle [2]
    if life == 0:
        break

    print("\n")
    time.sleep(0.5)
    typingPrint(r'"And that brings us the final cry, the last judgement. Where you must stand before your decisions and choices throughout the rhythm of your life and be faced with the rewards and consequences, come what may."' + "\n")
    time.sleep(0.5)
    typingPrint('"You\'ve been here for awhile now. I hope you have looked around. So tell me, do you know where you are?"'+'\n')
    time.sleep(0.5)
    print (r'Response A:"Heaven?"' + "\n"
           'Response B: "Hell"'+ "\n"
           'Response C: "Purgatoy"')
    if dream ==1:
        print("Response D: A Dream?" + "\n")

    while True:
        response=str(input("What do you do? "))
        response = response.lower()
        if response == "a" or response == "b":
            typingPrint('"No, you aren\'t dead. Not yet any case. Nor are you in any danger of it. No, you are somewhere in-between. Nestled in the comfort of your own subconscious. This is a dream."' + "\n")
            break
        elif response == "c":
            typingPrint('"Not quite, but close. You are somewhere in-between. Nestled in the comfort of your own subconscious. This is a dream."' + "\n")
            break
        elif response == "d":
            typingPrint('"Very perceptive. . ." The entity purrs. "You are correct. You are nestled in the comfort of your own subconscious. This is a dream."' + "\n")
            break
        else:
            print("Invalid Response. Please try again.")
            continue
        
    while True:
        final= str(typingInput('"To end our little test, tell me: What am I?" '))
        print('\n')
        final = final.lower()
        if "cat" in final:
            typingPrint('"Very good" The Entity purrs.' + '\n')
            break
        else:
            print('\n')
            typingPrint("Not quite. Give it another go. You can't leave here until you get it." +'\n')
            life -=1
            while True:
                final= str(typingInput('Do you need a hint? '))
                final = final.lower()
                if final == "yes":
                    typingPrint('During the game, you gave the entity a ball of yarn, a glass of milk, treats, and a gold fish. What do those items remind you of?' +'\n')
                    break
                else:
                    continue
            continue

    typingPrint('The entity, or rather, the cat, hops off the armchair and pads over to you.' + '\n')
    typingPrint('You now see the cat has dark black fur and piercing green eyes. The level of knowing in the cat\'s eyes unsettles you.' +'\n')
    time.sleep(0.5)

    if anger >=6:
        typingPrint('You could swear the cat scowls as it looks up at you.'+'\n')
        print('\n')
        time.sleep(0.5)
        typingPrint('"You may have passed these tests, but don\'t think I\'ve forgotten the scorn you sent me this entire experience."'+'\n')
        time.sleep(0.5)
        print('\n')
        typingPrint('The cat turns and begins walking back into the darkness of the cabin'+'\n')
        break
    else:
        typingPrint('You could swear the cat smiles as it looks up at you.'+'\n')
        print('\n')
        time.sleep(0.5)
        typingPrint('"You\'ve done well, you figured out every single one of my riddles. This has been fun. I hope you enjoyed this as much as I have."'+'\n')
        time.sleep(0.5)
        print('\n')
        typingPrint('The cat walks forward, rubbing against the side of your legs. The cat looks like they want pets'+'\n')
        final = str(typingInput("What would you like to do? "))
        if "pet" in final:
            typingPrint("The cat is very soft." + '\n')
            pet +=1
    

    print("\n")
    time.sleep(0.5)
    typingPrint(r'"You better wake up now, before you forget how."' + "\n")
    time.sleep(0.5)
    print ('\n')
    typingPrint(".    .    .    .    ." + '\n')
    print('\n')

    if anger >=6:
        typingPrint('You awaken. . . In your bed.'+'\n')
        print('\n')
        time.sleep(0.5)
        typingPrint('The time on the bedside clock reads [4:01 AM], and already, the memories of that strange dream, the trials in a dark cabin with frosted windows and locked doors,' +'\n'
                    'are fading. You are left with a pounding headache and groggy ayes after the early morning rise, however what woke you, you cannot tell.'+'\n')
        time.sleep(0.5)
        print('\n')
        typingPrint('You as you fall back asleep, unsettled, you wonder: Where is your cat?'+'\n')
        print ('\n')
        typingPrint('You get the feeling you lost something important. '+'\n')
    else:
        typingPrint('You awaken. . . In your bed.'+'\n'
                    'The time on the bedside clock reads [4:01 AM], and your cat is meowing quite insistently on your chest.' +'\n')
        print('\n')
        time.sleep(0.5)
        typingPrint('Already, the memories of that strange dream, the trials in a dark cabin with frosted windows and locked doors, are fading.' + '\n'
                    'Instead, you are left with a very happy kitty and groggy eyes from the early morning rise.'+'\n')
        time.sleep(0.5)
        print('\n')
        typingPrint('Your cat, seemingly content with your attention, curls up next to you, purring against your chest. '+'\n')
        print ('\n')
        typingPrint('You fall back asleep, surrounded by comfort and warmth, and you do not wake until the sun rises.'+'\n')
        sleep+=1
    
    
    time.sleep(5)
    print('\n'+ "=========================================" +'\n')
    acheivements(candle, blanket, anger, life, pet, sleep)
    print('\n'+ "=========================================" +'\n')
    credit()
    print('\n'+ "=========================================" +'\n')
    quit()

print("GAME OVER")
quit()

######################
# Sources:
# https://www.101computing.net/python-typing-text-effect/
# https://stackoverflow.com/questions/10406130/check-if-something-is-not-in-a-list-in-python
# Akanchar
# https://note.nkmk.me/en/python-function-return-multiple-values/
# https://stackoverflow.com/questions/5319922/check-if-a-word-is-in-a-string-in-python


#######################
# Game Guide
# Riddle 1 Answer: Yarn, under the ottoman
# Riddle 2 Anwser: Milk, in the sink
# Riddle 3 Anwser: Meat, in the bag in the safe. Code: 3467
# Riddle 4 Answer: Gold_fish, in the fishtank

# Acheivement Guide
# 5 candles to light. One in each room. Must grab lighter
# 3 Blankets to take. One in Living Room, One in Basement, One in Bedroom

# What am I: answer must contain word "cat"
# You can only pet the cat when you are on the good ending track



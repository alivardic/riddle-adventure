
import streamlit as st
from Room import Room

# === Initialize Rooms ===
def create_rooms():
# Source Code With my additions 
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
    bedroom.addExit("living_room", living_room)
    bedroom.addExit("bathroom", bathroom)
    # add grabbables to Bedroom
    # Instead of adding duplicates manually
    for _ in range(5):
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

    return living_room

def initialize_game():
    if "initialized" not in st.session_state:
        st.session_state.currentRoom = create_rooms()
        st.session_state.life = 5
        st.session_state.inventory = []
        st.session_state.anger = 0
        st.session_state.blanket = 0
        st.session_state.candle = 0
        st.session_state.hints = 0
        st.session_state.pet = 0
        st.session_state.sleep = 0
        st.session_state.stage = "intro"
        st.session_state.initialized = True

def display_status():
    st.write(f"**Room:** {st.session_state.currentRoom.name}")
    st.write(f"**HP:** {st.session_state.life}")
    st.write(f"**Inventory:** {st.session_state.inventory}")
    st.write(st.session_state.currentRoom)

def process_command(command):
    command = command.lower().strip()
    if not command:
        return "Enter a command."
    words = command.split()
    if len(words) < 2:
        return "Use VERB NOUN format (e.g., take candle)."
    verb, noun = words[0], words[1]
    if verb == "go":
        if noun in st.session_state.currentRoom.exits:
            idx = st.session_state.currentRoom.exits.index(noun)
            st.session_state.currentRoom = st.session_state.currentRoom.exitLocations[idx]
            return f"You go to the {noun}."
        return "Invalid exit."
    if verb == "look":
        if noun in st.session_state.currentRoom.items:
            idx = st.session_state.currentRoom.items.index(noun)
            desc = st.session_state.currentRoom.itemDescriptions[idx]
            if st.session_state.currentRoom.itemGrabs[idx] not in st.session_state.inventory:
                desc += st.session_state.currentRoom.grabDesc[idx]
            return desc
        return "You don't see that item."
    if verb == "take":
        if noun in st.session_state.currentRoom.grabbables:
            st.session_state.inventory.append(noun)
            st.session_state.currentRoom.delGrabbable(noun)
            return f"You take the {noun}."
        return "You can't take that."
    return "Unknown command."

def show_intro():
    st.write("You awaken on a couch in a dark room...")
    st.write("A voice speaks out from the darkness.")
    choice = st.radio("What do you say?", ["Who are you?", "Where am I?", "Stay Quiet"])
    if st.button("Continue"):
        st.session_state.stage = "riddle1"

def play_riddle1():
    st.write("Your first test: Find me something that embodies mirth and joy in play.")
    display_status()
    command = st.text_input("Enter a command (e.g., 'take yarn', 'go kitchen')", key="cmd1")
    if st.button("Submit Command", key="btn1"):
        st.write(process_command(command))
    if "yarn" in st.session_state.inventory:
        if st.button("Give yarn to the entity"):
            st.session_state.stage = "riddle2"

def play_riddle2():
    st.write("Your second test: Find me something that gives comfort in warmth.")
    display_status()
    command = st.text_input("Enter a command (e.g., 'take blanket', 'go bedroom')", key="cmd2")
    if st.button("Submit Command", key="btn2"):
        st.write(process_command(command))
    if "blanket" in st.session_state.inventory:
        if st.button("Give blanket to the entity"):
            st.session_state.stage = "ending"

def show_achievements():
    st.write("### Achievements Earned:")
    if st.session_state.candle == 5:
        st.write("✅ Warm Kitty: Lit all candles")
    else:
        st.write("❌ Warm Kitty: Missed lighting candles")

def run_stage():
    if st.session_state.stage == "intro":
        show_intro()
    elif st.session_state.stage == "riddle1":
        play_riddle1()
    elif st.session_state.stage == "riddle2":
        play_riddle2()
    elif st.session_state.stage == "ending":
        show_achievements()

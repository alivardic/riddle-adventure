
import streamlit as st
from Room import Room

def create_rooms():
    # COPY your create_rooms() code here (corrected version)
    living_room = Room("living room")
    kitchen = Room("kitchen")
    basement = Room("basement")
    bedroom = Room("bedroom")
    bathroom = Room("bathroom")

    # ... all your addExit/addItem/addGrabbable logic here ...
    bedroom.addExit("living_room", living_room)
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

import streamlit as st
from game_logic import create_rooms, display_status, process_command

st.set_page_config(page_title="Ode to Rhythm", layout="centered")

# === Initialize Session State ===
if "currentRoom" not in st.session_state:
    st.session_state.life = 5
    st.session_state.inventory = []
    st.session_state.currentRoom = create_rooms()

st.title("🎮 Ode to Rhythm: Riddles from the Dark Room")

display_status()

command = st.text_input("Enter a command (e.g., 'go kitchen', 'take candle')")

if st.button("Submit Command"):
    result = process_command(command)
    st.write(result)

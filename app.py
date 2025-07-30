import streamlit as st
from game_logic_full import initialize_game, run_stage

st.set_page_config(page_title="Ode to Rhythm", layout="centered")

initialize_game()
st.title("🎮 Ode to Rhythm: Riddles from the Dark Room")

run_stage()

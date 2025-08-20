import streamlit as st
import random

# Set page config
st.set_page_config(
    page_title="Rock Paper Scissors Game",
    page_icon="✂️",
    layout="centered"
)


def get_hand_emoji(choice):
    """Get hand emoji for the choice"""
    hand_emojis = {"rock": "✊", "paper": "✋", "scissors": "✌️"}
    return hand_emojis.get(choice, "❓")


# Main app
st.title("🪨📄✂️ Rock Paper Scissors")
st.write("Welcome, to Rock Paper Scissor Game!")

# Game logic
words = ["rock", "paper", "scissors"]

# Create columns for better layout
col1, col2, col3 = st.columns(3)

with col1:
    rock_btn = st.button("✊ Rock", use_container_width=True)

with col2:
    paper_btn = st.button("✋ Paper", use_container_width=True)

with col3:
    scissors_btn = st.button("✌️ Scissors", use_container_width=True)

# Handle button clicks
p_choice = None
if rock_btn:
    p_choice = "rock"
elif paper_btn:
    p_choice = "paper"
elif scissors_btn:
    p_choice = "scissors"

# Game execution
if p_choice:
    # Display choices side by side with big hand emojis
    st.write("---")

    # Create two columns for the face-off
    choice_col1, vs_col, choice_col2 = st.columns([2, 1, 2])

    with choice_col1:
        st.markdown(
            f"<div style='text-align: center'><h3>You</h3><div style='font-size: 120px;'>{get_hand_emoji(p_choice)}</div><h4>{p_choice.title()}</h4></div>",
            unsafe_allow_html=True)

    with vs_col:
        st.markdown("<div style='text-align: center; padding-top: 80px;'><h2>VS</h2></div>", unsafe_allow_html=True)

    with choice_col2:
        c_random = random.randint(0, 2)
        c_choice = words[c_random]
        st.markdown(
            f"<div style='text-align: center'><h3>Computer</h3><div style='font-size: 120px;'>{get_hand_emoji(c_choice)}</div><h4>{c_choice.title()}</h4></div>",
            unsafe_allow_html=True)

    st.write("---")

    # Results centered and prominent
    if p_choice == c_choice:
        st.markdown("<div style='text-align: center'><h2>🤝 It is a draw!</h2></div>", unsafe_allow_html=True)
    elif p_choice == words[0] and c_choice == words[2]:
        st.markdown("<div style='text-align: center'><h2>🎉 You Win!</h2></div>", unsafe_allow_html=True)
    elif p_choice == words[2] and c_choice == words[0]:
        st.markdown("<div style='text-align: center'><h2>😔 You Lose!</h2></div>", unsafe_allow_html=True)
    elif p_choice > c_choice:
        st.markdown("<div style='text-align: center'><h2>🎉 You Win!</h2></div>", unsafe_allow_html=True)
    elif p_choice < c_choice:
        st.markdown("<div style='text-align: center'><h2>😔 You Lose!</h2></div>", unsafe_allow_html=True)
    else:
        st.markdown(
            "<div style='text-align: center'><h2>❌ Sorry, you picked an invalid input<br>Restart and try again!</h2></div>",
            unsafe_allow_html=True)

# Instructions
st.write("---")
st.write("**How to play:** Click one of the buttons above to make your choice!")
st.caption("Rock beats Scissors, Scissors beats Paper, Paper beats Rock")
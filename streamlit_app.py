import streamlit as st
import random

# Set page config
st.set_page_config(
    page_title="Rock Paper Scissors Game",
    page_icon="✂️",
    layout="centered"
)


def print_action(player, choice):
    """Display the player's choice with appropriate emoji"""
    emojis = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
    emoji = emojis.get(choice, "❓")
    return f"{player}: {choice.title()} {emoji}"


# Main app
st.title("🪨📄✂️ Rock Paper Scissors Game!")
st.write("Welcome, to Rock Paper Scissor Game!")

# Game logic
words = ["rock", "paper", "scissors"]

# Create columns for better layout
col1, col2, col3 = st.columns(3)

with col1:
    rock_btn = st.button("🪨 Rock", use_container_width=True)

with col2:
    paper_btn = st.button("📄 Paper", use_container_width=True)

with col3:
    scissors_btn = st.button("✂️ Scissors", use_container_width=True)

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
    # Display player choice
    st.write("---")
    st.write("**Choices:**")
    st.write(print_action('You', p_choice))

    # Computer choice
    c_random = random.randint(0, 2)
    c_choice = words[c_random]
    st.write(print_action('Computer', c_choice))

    # Results
    st.write("---")
    st.write("**Results:**")

    if p_choice == c_choice:
        st.info('🤝 It is a draw!')
    elif p_choice == words[0] and c_choice == words[2]:
        st.success('🎉 You Win!')
    elif p_choice == words[2] and c_choice == words[0]:
        st.error('😔 You Lose!')
    elif p_choice > c_choice:
        st.success('🎉 You Win!')
    elif p_choice < c_choice:
        st.error('😔 You Lose!')
    else:
        st.warning('❌ Sorry, you picked an invalid input\nRestart and try again!')

# Instructions
st.write("---")
st.write("**How to play:** Click one of the buttons above to make your choice!")
st.caption("Rock beats Scissors, Scissors beats Paper, Paper beats Rock")
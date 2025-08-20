import random
import actions
words = ["rock", "paper", "scissors"]
emotes = [actions.rock, actions.paper, actions.scissors]
p_choice = input('Welcome, to Rock Paper Scissor Game!\nPlease type in "rock", "paper" or "scissors"').lower()
actions.print_action(p_choice)
c_random = random.randint(0,2)
c_choice = words[c_random]
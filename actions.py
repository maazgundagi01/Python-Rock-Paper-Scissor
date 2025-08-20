def print_action(label, action):
    if action == 'rock':
        print(label)
        print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
        ''')
    elif action == 'paper':
        print(label)
        print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
        ''')
    elif action == 'scissors':
        print(label)
        print('''
    ______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
        ''')
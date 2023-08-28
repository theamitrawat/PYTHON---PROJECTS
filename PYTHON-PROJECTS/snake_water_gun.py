import random

print('\n===========================================================================================================')
print('\t\t\t\t\tSNAKE GUN WATER GAME')
print('===========================================================================================================\n')

def user_input_option():
    print("\n\t1. Type [ Rules ] input to read the rules of the game.")
    print("\t2. Type [ Start ] input to start the game.")
    print("\t3. Type [ exit ] input to Exit the game.")
    user_input = input('\nEnter your input: ').capitalize()
    if user_input not in ['Rules','Start', 'Exit']:
        print('Invalid choice! Please choose a correct option.')
        print('--------------------------------------------------------------------------------------------------')
        user_input = user_input_option()
        return user_input
    else:
        return user_input


def Game_rules():
    print('\n=============================================================')
    print('\t\t\t RULES OF THE GAME')
    print('=============================================================\n')

    print("1. There are three option in this game (Snake, Water, Gun). \n2. You have to choose only one option from all three options. \n3. Then computer choose a option randomly from all three options. \n4. here the chance of winning: \n\ti) Snake Beat's Water \n\tii) Water Beat's Gun \n\tiii) Gun Beat's Snake \n4. If your choosen option is better than computer's option then you will win this game otherewise you lose this game\n")

    print('\n--------------------------------------------------------------------------------------------------\n')
    play_game(user_input_option())

def get_user_choice():
    print("Enter [ snake ] for choosing -SNAKE.")
    print("Enter [ water ] for choosing -WATER.")
    print("Enter [ gun ] for choosing -GUN.\n")

    user_choice = input('Enter your choice: ').lower()
    if user_choice not in ['snake', 'water', 'gun']:
        print('Invalid choice! Please choose a correct option.')
        print('\n--------------------------------------------------------------------------------------------------\n')
        user_choice = get_user_choice()
        return user_choice
    else:
        return user_choice
    
def get_computer_choice():
    return random.choice(['snake', 'water', 'gun'])

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return '\n\t ~ Game is Tie. Try again! ~\n--------------------------------------------------------------------------------------------------\n'
    elif user_choice == "snake":
        return "\n\t~ You win! ~\n--------------------------------------------------------------------------------------------------\n" if computer_choice == "water" else "\n\t~ Computer wins! ~\n--------------------------------------------------------------------------------------------------\n"
    elif user_choice == "water":
        return "\n\t~ You win! ~\n--------------------------------------------------------------------------------------------------\n" if computer_choice == "gun" else "\n\t~ Computer wins! ~\n--------------------------------------------------------------------------------------------------\n"
    elif user_choice == "gun":
        return "\n\t~ You win! ~\n--------------------------------------------------------------------------------------------------\n" if computer_choice == "snake" else "\n\t~ Computer wins! ~\n--------------------------------------------------------------------------------------------------\n"
    elif user_choice == 'exit':
        return'\n **** THANKS FOR PLAYING! GOODBYE! ***\n'

def game_steps():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print('\n|\t Your Choice: ',user_choice,'\t\t |')
    print('|\tComputer Choice: ',computer_choice,'\t |')
    game_winner = winner(user_choice,computer_choice)
    print(game_winner)

def play_game(user_input):
    match user_input:
        case 'Rules':
            print(Game_rules())
        case 'Start':
            print('\n=============================================================')
            print('\t  ALL THE VERY BEST! - LET START THE GAME')
            print('=============================================================\n')
            while True:
                game_steps()                
        case 'Exit':
            print('\n **** THANKS FOR PLAYING! GOODBYE! ***\n')

play_game(user_input_option())
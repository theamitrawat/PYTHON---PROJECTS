# The line `import random` is importing the `random` module in Python. This module provides functions for generating random numbers, selecting random elements from a list, and other randomization-related operations. In this code, the `random` module is used to randomly select the computer's choice in the game of Rock Paper Scissors.
import random

# The Rock_Paper_Scissors class is used to play the game of rock, paper, scissors.
class Rock_Paper_Scissors:
  """
  The function initializes the attributes of a class for a rock-paper-scissors game.
  """
  def __init__(self):
    self.choices_list = ['rock', 'paper', 'scissors']
    self.player_score = 0
    self.computer_score = 0

  """
  The function `get_player_choice` prompts the user to choose from a list of options and returns the selected choice.
  :return: the player's choice from the list of choices.
  """
  def get_player_choice(self):
    # The `while True:` statement creates an infinite loop. It means that the code inside the loop will keep executing indefinitely until a break statement is encountered or an exception is raised. In this specific code, the loop is used to repeatedly play the game of Rock Paper Scissors until the user chooses not to play again.
    while True:
      print("\n\t\tChoose one:\n")
      for i, choice in enumerate(self.choices_list, start=1):
        print(f"\t\t\t{i}. for {choice.capitalize()}")

      # The `try` block is used to handle any potential errors that may occur when the user enterstheir choice.
      try:
        choice_number = int(input("\nEnter your choice: "))
        if 0 <= choice_number <= len(self.choices_list):
          return self.choices_list[choice_number - 1]
        
        else:
          print("\n~ Invalid choice. Please chose from above choices!. ~")
          print('\n--------------------------------------------------------')

      except ValueError:
        print("\n~ Invalid input. Please enter a number. ~")
        print('\n--------------------------------------------------------')

  """
  The function returns a random choice from a list of choices.
  :return: a randomly chosen element from the list "choices_list".
  """
  def get_computer_choice(self):
    return random.choice(self.choices_list)
  """
  The function determines the winner of a rock-paper-scissors game based on the choices made by the player and the computer.
  :param player_choice: The choice made by the player (rock, paper, or scissors)
  :param computer_choice: The computer's choice in the game (rock, paper, or scissors)
  :return: a string that indicates the result of the round. If it's a tie, it returns "~ It's a tie
  ~". If the player wins, it returns "~ You win this round! ~". If the computer wins, it returns "~
  Computer wins this round! ~".
  """
  def determine_winner(self, player_choice, computer_choice):
    if player_choice == computer_choice:
      return "\n~ It's a tie ~"
    
    elif ((player_choice == "rock" and computer_choice == "scissors")
          or (player_choice == "paper" and computer_choice == "rock")
          or (player_choice == "scissors" and computer_choice == "paper")):
      self.player_score += 1
      return "\n~ You win this round! ~"
    
    else:
      self.computer_score += 1
      return "\n~ Computer wins this round! ~"
  """
  The function `play_game` allows the user to play a game of Rock Paper Scissors against the computer for a specified number of rounds and displays the results at the end.
  """
  def play_game(self):
    print("\n-------------- ROCK PAPER SCISSORS GAME -------------\n")
    rounds = int(input("Enter no of rounds: "))

    for round_num in range(1, rounds + 1):
      print(f"\n\t\tRound {round_num}/{rounds}:")
      player_choice = self.get_player_choice()
      computer_choice = self.get_computer_choice()

      print(f"\n--> You choose: {player_choice}")
      print(f"--> Computer choose: {computer_choice}")
      result = self.determine_winner(player_choice, computer_choice)
      print(result)

      print(f"\n\tPlayer Score: {self.player_score}")
      print(f"\tComputer Score: {self.computer_score}")
      print('\n--------------------------------------------------------')

    print("Game over!")
    if self.player_score > self.computer_score:
      print("Congratulations! You win the game!\n")
    elif self.computer_score > self.player_score:
      print("Computer wins the game. Better luck next time!\n")
    else:
      print("It's a tie!\n")


# Create an instance of the game and start playing The code block 
# `while True:` creates an infinite loop that allows the user to play the game of Rock Paper Scissors multiple times.
while True:
  game = Rock_Paper_Scissors()
  game.play_game()

  play_again = input("Do you want to play again? (yes/no): ").lower()
  if play_again != 'yes':
    print("\n\t~ Thanks for playing! Goodbye! ~\n")
    break

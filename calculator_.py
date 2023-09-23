# The Calculator class is a Python class that performs mathematical calculations.
class Calculator:

  """
  The above function is a constructor that initializes two instance variables, num1 and num2.  
  :param num1: The first number that will be passed as an argument when creating an instance of the class
  :param num2: The parameter `num2` is a variable that represents the second number. It is used to initialize the `num2` attribute of the object
  """

  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2

    """
    The above code defines three functions for performing addition, subtraction, and multiplication.
    """

  def addition(self):
    print(f"\n\tAddition = {num1 + num2} ")
    print("\n----------------------------------------------\n")

  def subtraction(self):
    print(f"\n\tSubtraction = {num1 - num2} ")
    print("\n----------------------------------------------\n")

  def multiplication(self):
    print(f"\n\tMultiplication = {num1 * num2} ")
    print("\n----------------------------------------------\n")

  """
  The function performs division between two numbers, handling the case where the second number is zero.
  """

  def division(self):
    if self.num2 == 0:
      print("\n~ number cannot divide by zero. ~\n")
    else:
      print(f"\n\tDivision = {num1 / num2} ")
      print("\n----------------------------------------------\n")

print('\n------------- BASIC CALCULATOR ---------------\n')

# The code block you provided is a while loop that continuously prompts the user for two numbers and an operation choice until the user decides to exit the program.

while True:
  try:
    num1 = float(input("first number : "))
    num2 = float(input("second number: "))

    print('\n(+) for addition')
    print('(-) for subtraction')
    print('(*) for multiplication')
    print('(/) for division')

    # The code `user_operation_choice = input("\nEnter your choice: ")` is prompting the user to enter their choice of operation (+, -, *, /) for the calculator.

    user_operation_choice = input("\nEnter your choice: ")
    calculator = Calculator(num1, num2)

    # The code block you provided is checking if the user's operation choice (`user_operation_choice`) is present in the `choice_list` list.

    choice_list = ['+','-','*','/']
    if user_operation_choice in choice_list:
      match user_operation_choice:
        case '+':
          calculator.addition()
        case '-':
          calculator.subtraction()
        case '*':
          calculator.multiplication()
        case '/':
          calculator.division()
        
    # The `else` block is executed when the user's operation choice is not present in the`choice_list` list. It prints a message indicating that the option is invalid and prompts the user to choose a correct option.

    else:
      print("\n\tInvalid option. Please choose correct option.")
      print("\n--------------------------------------------------------\n")
  except ValueError:
    print("\n~ Invalid input. Please enter valid numbers. ~")
    print("\n--------------------------------------------------------\n")

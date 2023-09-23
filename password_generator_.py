# The `import random` statement imports the `random` module, which provides functions for generating random numbers, selecting random elements from a sequence, and shuffling sequences randomly.
# The `import string` statement imports the `string` module, which provides a collection of useful string constants and functions. In this code, the `string` module is used to access constants like `string.ascii_lowercase`, `string.ascii_uppercase`, `string.digits`, and `string.punctuation`, which represent lowercase letters, uppercase letters, digits, and special characters respectively. These constants are used in the `PasswordGenerator` class to define the choices for generating passwords.

import random
import string

# The PasswordGenerator class is used to generate random passwords.
class PasswordGenerator:

  """
    The function initializes a dictionary with keys representing different character sets and values representing the corresponding characters.
  """

  def __init__(self):
    self.choices = {
        'lowercase': string.ascii_lowercase,
        'uppercase': string.ascii_uppercase,
        'digits': string.digits,
        'special_chars': string.punctuation
    }

  """
    The function generates a random password of a specified length, with options to include lowercase letters, uppercase letters, digits, and special characters.
    :param length: The length parameter specifies the desired length of the generated password
    :param include_lowercase: A boolean value indicating whether lowercase letters should be included
    in the generated password. If set to True, lowercase letters will be included. If set to False,lowercase letters will not be included, defaults to True (optional)
    :param include_uppercase: This parameter determines whether or not to include uppercase letters in the generated password. If set to True, uppercase letters will be included. If set to False, uppercase letters will not be included, defaults to True (optional)
    :param include_digits: The parameter include_digits determines whether or not to include digits (numbers) in the generated password. If include_digits is set to True, digits will be included in the password. If it is set to False, digits will not be included, defaults to True (optional)
    :param include_special_chars: This parameter determines whether special characters should be included in the generated password. If set to True, special characters will be included. If set to False, special characters will not be included, defaults to True (optional)
    :return: a randomly generated password based on the specified length and character options.
    """

  def generate_password(self,length,
                        include_lowercase=True,
                        include_uppercase=True,
                        include_digits=True,
                        include_special_chars=True):
    characters = ''
    if include_lowercase:
      characters += self.choices['lowercase']
    if include_uppercase:
      characters += self.choices['uppercase']
    if include_digits:
      characters += self.choices['digits']
    if include_special_chars:
      characters += self.choices['special_chars']

    if length < 1:
      return "\n~ Password length must be at least 1 character. ~\n"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

  def get_user_preferences(self):
    print(
        "\n---------------------- PASSWORD GENERATOR -----------------------\n"
    )
    print("Give your valueable (yes/no) input to generate a strong password.")
    print(
        '\n-----------------------------------------------------------------\n'
    )

    # The `try` block is used to handle potential errors that may occur when the user enters input for generating a password.
    try:
      length = int(input("Enter Password length: "))
      if length < 1:
        print("Password length must be at least 1 character.")
        return

      lowercase = input(
          "\nDo you want to Include lowercase letters? (yes/no): ").lower(
          ) == "yes"
      uppercase = input("Do you want to Include uppercase letters? (yes/no): "
                        ).lower() == "yes"
      digits = input(
          "Do you want to Include digits (0-9)? (yes/no): ").lower() == "yes"
      special_chars = input(
          "Do you want to Include special characters? (yes/no): ").lower(
          ) == "yes"

      password = self.generate_password(length, lowercase, uppercase, digits,
                                        special_chars)

      print(f"\nGenerated Password:\n\n\t{password}\n")

    except ValueError:
      print("\n~ Invalid input. Please enter a valid number for the password length! ~\n")

"""
The main function creates an instance of the PasswordGenerator class and calls the
get_user_preferences method.
"""

def main():
  password_generator = PasswordGenerator()
  password_generator.get_user_preferences()

# The `if __name__ == "__main__":` statement is used to check if the current script is being run as the main module. If it is, the `main()` function is called. This is a common practice in Python to ensure that the code inside the `main()` function is only executed when the script is run directly, and not when it is imported as a module by another script.
if __name__ == "__main__":
  main()

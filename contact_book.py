# The Contacts class is a class that represents a collection of contacts.
class Contacts:

  """
  The function initializes an object with the given name, phone number, email, and address.
  
  :param name: The name parameter is used to store the name of the person
  :param phone_no: The phone_no parameter is used to store the phone number of the person
  :param email: The email parameter is used to store the email address of the person
  :param address: The address parameter is used to store the address of the person. It can be a string that includes the street name, city, state, and postal code
  """

  def __init__(self, name, phone_no, email, address):
    
    self.name = name
    self.phone_no = phone_no
    self.email = email
    self.address = address

# The Contacts_Book class is a class that represents a contacts book.
class Contacts_Book:

  """
  The above function is the constructor for a class that initializes an empty list called "contacts".
  """

  def __init__(self):
    self.contacts = []

  """
  The function adds a contact to a contact book and prints a confirmation message.
  
  :param contact: The parameter "contact" is an object that represents a contact to be added to the contact book. It likely has attributes such as name, phone number, email, etc
  """

  def add_contact(self, contact):

    self.contacts.append(contact)
    print(f"\n~ {contact.name} has been added to the contact book.")
    print('\n--------------------------------------------------------\n')

  """
  The function "view_contacts" checks if the contact book is empty and prints a message if it is.:return: nothing.
  """

  def view_contacts(self):
    if not self.contacts:
      print("\n~ Contact book is empty. ~")
      print('\n--------------------------------------------------------\n')
      return

    print("\n\tContact List:\n")
    for i, contact in enumerate(self.contacts, start=1):
      print(f"\t\t{i}. {contact.name} - {contact.phone_no}")
    print('\n--------------------------------------------------------\n')

  """
  The function searches for contacts in a list based on a given search term and prints the matching  contacts.
  
  :param search_contact: The parameter "search_contact" is the input string that is used to search for matching contacts. It can be either a name or a phone number
  """

  def search_contact(self, search_contact):
    matching_contacts = []
    for contact in self.contacts:
      if search_contact.lower() in contact.name.lower() or search_contact in contact.phone_no:
        matching_contacts.append(contact)

    if matching_contacts:
      print("\n----------Matching Contacts-----------\n")
      for i, contact in enumerate(matching_contacts, start=1):
        print(f"\t{i}. {contact.name} - {contact.phone_no}")
    else:
      print("\n~ No matching contacts found. ~")
    print('\n--------------------------------------------------------\n')

  """
  The function `update_contact` searches for contacts that match a given search term and prints the matching contacts' names and phone numbers.
  
  :param search_contact: The parameter `search_contact` is the contact information that you want to search for. It can be either the name or the phone number of a contact :return: nothing.
  """

  def update_contact(self, search_contact):
    matching_contacts = []
    for contact in self.contacts:
      if search_contact.lower() in contact.name.lower() or search_contact in contact.phone_no:
        matching_contacts.append(contact)

    if not matching_contacts:
      print("\n~ No matching contacts found. ~")
      print('\n--------------------------------------------------------\n')
      return

    print("\n----------Matching Contacts-----------\n")
    for i, contact in enumerate(matching_contacts, start=1):
      print(f"\t{i}. {contact.name} - {contact.phone_no}")

    # The `try` block is used to handle any potential errors that may occur when the user enters their choice for updating a contact.
    try:
      choice = int(
          input("\nEnter the index of the contact you want to update: ")) - 1
      if 0 <= choice < len(matching_contacts):
        updated_contact = matching_contacts[choice]
        updated_name = input("Enter updated name (press Enter to keep the same): ").strip()
        updated_phone_no = input("Enter updated phone number (press Enter to keep the same): "
        ).strip()
        updated_email = input("Enter updated email (press Enter to keep the same): ").strip()
        updated_address = input("Enter updated address (press Enter to keep the same): ").strip()

        if updated_name:
          updated_contact.name = updated_name
        if updated_phone_no:
          updated_contact.phone_no = updated_phone_no
        if updated_email:
          updated_contact.email = updated_email
        if updated_address:
          updated_contact.address = updated_address

        print(
            f"\n~ {updated_contact.name}'s contact information has been updated."
        )
      else:
        print("\n~ Invalid choice. ~")
      print('\n--------------------------------------------------------\n')
    except ValueError:
      print("\n ~ Invalid input. Please enter a valid number. ~")
      print('\n--------------------------------------------------------\n')

  def delete_contact(self, search_contact):
    """
    The `delete_contact` function searches for contacts that match the given search criteria and prints them, or displays a message if no matching contacts are found.
    
    :param search_contact: The parameter `search_contact` is the contact information that you want to search for. It can be either the name or the phone number of a contact :return: nothing.
    """
    matching_contacts = []
    for contact in self.contacts:
      if search_contact.lower() in contact.name.lower() or search_contact in contact.phone_no:
        matching_contacts.append(contact)

    if not matching_contacts:
      print("\n~ No matching contacts found. ~")
      print('\n--------------------------------------------------------\n')
      return

    print("\n----------Matching Contacts-----------\n")
    for i, contact in enumerate(matching_contacts, start=1):
      print(f"\t{i}. {contact.name} - {contact.phone_no}")

  # The code block you provided is handling the deletion of a contact from the contact book.

    try:
      choice = int(
          input("\nEnter the index of the contact you want to delete: ")) - 1
      if 0 <= choice < len(matching_contacts):
        deleted_contact = matching_contacts[choice]
        self.contacts.remove(deleted_contact)
        print(f"\n~ {deleted_contact.name}'s contact has been deleted.")

      else:
        print("\n~ Invalid choice. ~")
      print('\n--------------------------------------------------------\n')
    except ValueError:
      print("\n~ Invalid input. Please enter a valid number. ~")
      print('\n--------------------------------------------------------\n')

"""
The main function creates a contact book and provides a menu for adding, viewing, searching,updating, and deleting contacts.
"""

def main():
  contact_book = Contacts_Book()
  print("\n------------------------ CONTACT BOOK --------------------------\n")
  while True:
    print("\tContact Book Menu: \n")
    print("\t\t1. Add Contact")
    print("\t\t2. View Contacts")
    print("\t\t3. Search Contact")
    print("\t\t4. Update Contact")
    print("\t\t5. Delete Contact")
    print("\t\t6. Exit")

    choice = input("\n\tEnter your choice: ")

    """      
    The `match` statement is a new feature introduced in Python 3.10. It is used as an alternative to the traditional `if-elif-else` statement when there are multiple conditions to be checked against a single value.
    """
    
    choice_list = ['1','2','3','4','5','6']
    if choice in choice_list:
      match choice:
        case '1':
           name = input("\nEnter name: ")
           phone_no = input("Enter phone number: ")
           email = input("Enter email: ")
           address = input("Enter address: ")
           new_contact = Contacts(name, phone_no, email, address)
           contact_book.add_contact(new_contact)
        case '2':
           contact_book.view_contacts()
        case '3':
           search_contact = input("\n\tEnter name or phone number to search: ")
           contact_book.search_contact(search_contact)
        case '4':
           search_contact = input("\n\tEnter name or phone number to update: ")
           contact_book.update_contact(search_contact)
        case '5':
           search_contact = input("\n\tEnter name or phone number to delete: ")
           contact_book.delete_contact(search_contact)
        case '6':
           print("\n\t~ Exiting Contact Book. Goodbye! ~")
           print('\n--------------------------------------------------------')
           break
    else:
      print("\n\tInvalid option. Please choose correct option.")
      print("\n--------------------------------------------------------")

# The `if __name__ == "__main__"` condition is used to check if the current script is being run as the main module. This condition is true when the script is executed directly, but false when the script is imported as a module into another script.

if __name__ == "__main__":
  main()

# List to store user information during registering
users = []
Id = [0]

# Function of validation password
def validate_password(password):
    # Check if the password is at least 8 characters long
    if len(password)<8:
        print("Password must be at least 8 characters long.")
        return False
    letter= False
    digit= False
    special=False
    special_characters ="!@#$%^&*()"
    #Check each character manually
    for char in password:
        if char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            letter = True
        elif char in "0123456789":
            digit = True
        elif char in special_characters:
            special = True
    # Ensure password contains at least one letter, one digit, and one special character
    if not letter:
        print("Password must contain at least one letter.")
        return False
    if not digit:
        print("Password must contain at least one number.")
    if not special:
        print(f"Password must contain at least one special character ({special_character})")
        return False

    return True
# Create a new user function
def create_user():
    # Input the user for their first name
    first_name = input("Enter First Name: ")
    # Input the user for their last name
    last_name = input("Enter Last Name: ")
    # Input the user for their date of birth
    dob = input("Enter Date of Birth (DD/MM/YYYY): ")
    # Input the user for their phone number
    phone = input("Enter Phone Number: ")
    password = input("Enter Password: ")
    address = input("Enter Address: ")

    # Store the user information in a list

    user = [first_name, last_name, dob, phone, password, address, Id[0]]

    # Append the new user to the users list
    users.append(user)
    # Notify that the user has been created succesfully
    print("User created successfully! with an ID of:", Id[0])

    Id[0] = Id[0] + 1


# Function of registered users
def view_users():
    # Check if there are any registered users
    if len(users) == 0:
        # Notify if no users are registered
        print("No users registered yet.\n")
    else:
        # Loop through the users list and print their details
        for user in users:
            print(f"Name: {user[0]} {user[1]}, Phone: {user[3]}, ID: {user[6]}")
        print()


# Function of finding a user by phone number
def find_user():
    # Input the user for the phone number to find
    phone = input("Enter Phone Number to find: ")
    # Loop through the users list to search for the phone number
    for user in users:
        # If the phone number matches
        if user[3] == phone:
            # Print the user's details
            print("\n--- User Details ---")
            print(f"First Name: {user[0]}")
            print(f"Last Name: {user[1]}")
            print(f"Date of Birth: {user[2]}")
            print(f"Phone: {user[3]}")
            print(f"Address: {user[5]}")
            # Exit the function after displaying the details
            return
    # Notify if the user was not found
    print("User not found.\n")


def edit_users():
    id = input("what is your id?")
    first_name = input("Enter First Name: ")
    # Input the user for their last name
    last_name = input("Enter Last Name: ")
    # Input the user for their date of birth
    dob = input("Enter Date of Birth (DD/MM/YYYY): ")
    # Input the user for their phone number
    phone = input("Enter Phone Number: ")
    address = input("Enter Address: ")
    password = input("Enter Password: ")

    # Store the user information in a list

    user = [first_name, last_name, dob, phone, password, address, id]

    # Append the new user to the users list
    users[int(id)] = user
    # Notify that the user has been created succesfully
    print("Successfully edited")


def delete_users():
    id = int(input("what is your id?"))
    del users[id]


# Function of menu system
def main():
    # Start an infinite loop to keep the program running
    # Display menu options
    while True:
        print("1. Create New User")
        print("2. View All Users")
        print("3. Find User by Phone Number")
        print("4. Edit User")
        print("5. Delete User")
        print("6. Exit")

        # Input the user for their choice
        choice = input("Choose an option (1-6): ")

        # Handle the user's choice
        if choice == "1":
            # Call the function to create a new user
            create_user()
        elif choice == "2":
            # Call the function to view all registered users
            view_users()
        elif choice == "3":
            # Call the function to find a user by phone number
            find_user()
        elif choice == "4":
            # Call the function to find a user by phone number
            edit_users()
        elif choice == "5":
            # Call the function to find a user by phone number
            delete_users()
        elif choice == "6":
            # Notify that the program is exiting
            print("Exit")
            # Exit the loop and end the program
            break
        else:
            # Notify if the user input is invalid
            print("Invalid option, please enter a number between 1 and 6.\n")


# Run the program
if __name__ == "__main__":
    main()





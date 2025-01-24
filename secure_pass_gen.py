import random
import string

class SecurePassGen:
    def __init__(self):
        self.saved_password = {}

    def welcome_message(self):
        print("\033[1m\033[4mSecurePassGen\033[0m")
        print("Made by Alif")
        print("Version - v1.0")
        print("Release Date - 27-Feb-2024")
        print("=" * 50)
        print()

    def generate_password(self):
        print("Please provide the following information:")
        name = input("Name (Press enter to Skip): ")
        father_name = input("Father's Name (Press enter to Skip): ")
        mother_name = input("Mother's Name (Press enter to Skip): ")
        dob = input("Date of Birth (DD/MM/YYYY) (Press enter to Skip): ")
        best_friend_name = input("Best Friend's Name (Press enter to Skip): ")
        special_characters = input("Special Characters (Press enter to Skip): ")
        favourite_color = input("Favorite Color (Press enter to Skip): ")
        mobile_number = input("Mobile Number (Press enter to Skip): ")
        
        if not any([name, father_name, mother_name, dob, best_friend_name, special_characters, favourite_color, mobile_number]):
            print("No information provided. Please provide at least one piece of information.")
            return
        
        password_length = input("Set password length: ")
        password_difficulty = input("Password Difficulty (Easy/Medium/Hard): ")
        password_type = input("Password Type (1-Alphanumeric, 2-Alphabetic, 3-Numeric): ")

        if not any(char.isdigit() for char in password_length):
            print("No numeric value found in password length. Try again.")
            return

        generated_password = self.generate_password_based_on_inputs(name, father_name, mother_name, dob, best_friend_name, special_characters, favourite_color, mobile_number, password_length, password_difficulty, password_type)
        
        print("Your generated password is:", generated_password)
        
        save_password = input("Do you want to save this password? (Y/N): ")
        if save_password.upper() == 'Y':
            password_name = input("Set name for this password: ")
            self.saved_password[password_name] = generated_password
            print("Your password is saved as '{}'".format(password_name))
        else:
            print("The password is not saved.")

    def generate_password_based_on_inputs(self, name, father_name, mother_name, dob, best_friend_name, special_characters, favourite_color, mobile_number, password_length, password_difficulty, password_type):
        # Dummy password generation logic based on inputs
        length = int(password_length)
        if password_type == '1':  # Alphanumeric
            if password_difficulty.lower() == 'easy':
                characters = string.ascii_letters + string.digits
            elif password_difficulty.lower() == 'medium':
                characters = string.ascii_letters + string.digits + string.punctuation
            else:  # Hard
                characters = string.ascii_letters + string.digits + string.punctuation + ' '.join([name, father_name, mother_name, dob, best_friend_name, special_characters, favourite_color, mobile_number])
        elif password_type == '2':  # Alphabetic
            characters = string.ascii_letters
        else:  # Numeric
            characters = string.digits

        return ''.join(random.choice(characters) for _ in range(length))

    def recover_password(self):
        if not self.saved_password:
            print("No password saved.")
            return
        
        password_name = input("Enter the name you saved the password with: ")
        if password_name in self.saved_password:
            print("Your password is:", self.saved_password[password_name])
        else:
            print("No password found with the given name.")

    def start(self):
        self.welcome_message()
        while True:
            print("\nDo you want to generate a password (P) or recover your password (R)?")
            option = input("Enter your choice: ").upper()
            if option == 'P':
                self.generate_password()
            elif option == 'R':
                self.recover_password()
            else:
                print("Invalid option. Please enter 'P' for generating a password or 'R' for recovering a password.")

            another_action = input("\nDo you want to perform another action? (Y/N): ")
            if another_action.upper() != 'Y':
                print("\nThank you for using Secure Pass Gen")
                print("Made by Alif")
                print("Version - v1.0")
                break

if __name__ == "__main__":
    spg = SecurePassGen()
    spg.start()

import string
import random

def generate_password():
    while True:
        length = int(input('Please enter your preferred password length: '))
        chars = string.ascii_letters + string.digits + '!@#$%^&*()_+-='

        text = []
        for i in range(length):
            text.append(random.choice(chars))

        password = ''.join(text)

        print('Your Password: {}'.format(password))

        # ask the user if they want to create another password
        choice = ''
        while choice.lower() not in ['y', 'yes', 'n', 'no', 'q']:
            choice = input('Do you want to create another password? (Y/N/Q): ')
            if choice.lower() in ['n', 'no', 'q']:
                return  # exit the function and end the program

        # exit the function if user enters "n" or "q"
        if choice.lower() in ['n', 'no', 'q']:
            return

generate_password() # call the function to generate password

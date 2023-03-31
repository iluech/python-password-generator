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

        # exit the loop after generating the password
        break

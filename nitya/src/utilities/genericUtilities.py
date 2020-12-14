import logging as logger
import random
import string

def random_email_and_password(domain = None, email_prefix = None):
    if not domain:
        domain = 'gmail.com'
    if not email_prefix:
        email_prefix = 'testeruser'

    # Generation random email

    random_string_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase,k=random_string_length))
    email = email_prefix + '_'+random_string+'@'+domain

    # Generating random password

    password_string_length = 15
    password_string = ''.join(random.choices(string.ascii_letters,k=password_string_length))

    # random info as dict
    randominfo = {'email':email,'password':password_string}
    logger.debug(f"Randomly generated email and passwords are : {randominfo}")

    return randominfo

def get_randomString(k):
    random_string_length = k
    random_string = ''.join(random.choices(string.ascii_lowercase,k=random_string_length))
    return random_string
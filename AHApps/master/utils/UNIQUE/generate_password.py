import string
import random

def create_password(length=8):
    """
    Generate a random password of the specified length.
    Parameters:
    length (int): The length of the password to be generated. Defaults to 8.
    Returns:
    str: A randomly generated password consisting of letters, digits, and special characters.
    Example:
    >>> create_password(12)
    'aB9@3dF4_g5Q'
    
    >>> create_password()
    '7sYk@9L_'
    """
    chars = string.ascii_letters + string.digits + "@#._"
    password = ""
    for num in range(1,length+1):
        ch = chars[random.randint(0, len(chars)-1)]
        password += ch

    return password
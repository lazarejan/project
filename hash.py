def encrypt(password: str) -> str:
    """
    Encrypts the password using hashing algorithm.
    """

    len_ = len(password)
    for i, l in enumerate(password):
        password = password[:i] + chr(ord(l) - len_) + password[i+1:]
    return password

def decrypt(password: str) -> str:
    """
    Decrypts the password using hashing algorithm.
    """

    len_ = len(password)
    for i, l in enumerate(password):
        password = password[:i] + chr(ord(l) + len_) + password[i+1:]
    return password
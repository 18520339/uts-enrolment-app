import os
import hashlib
from getpass import getpass
from common import Validator


class PasswordSecurer:
    SALT_LENGTH = 32  # The length of the salt in bytes
    HASH_NAME = 'sha256'  # The name of the hash digest algorithm to use
    HASH_ITERS = 100000 # It is recommended to use >= 100,000 iterations of SHA-256 
    
    @staticmethod
    def input_and_confirm_password(prompt: str) -> str:
        password = getpass(prompt)
        if Validator.validate_password(password):
            confirm_password = getpass('\tConfirm password: ')
            if password == confirm_password: return password
            raise ValueError('\tPasswords do not match. Please try again')
 
    @staticmethod
    def hash_password(password: str) -> str:
        # Hashes a password with a randomly generated salt
        salt = os.urandom(PasswordSecurer.SALT_LENGTH)  # A new salt for this user
        key = hashlib.pbkdf2_hmac(
            PasswordSecurer.HASH_NAME, # The hash digest algorithm
            password.encode('utf-8'), # Convert the password to bytes
            salt = salt, # Provide the salt
            iterations = PasswordSecurer.HASH_ITERS  
        )
        storage = salt + key # Store the salt and key together
        return storage.hex() # Return the hashed password as hex digits for storage

    @staticmethod
    def verify_password(stored_password: bytes, provided_password: str) -> bool:
        # Verifies a provided password against the stored hash.
        stored_password_bytes = bytes.fromhex(stored_password)
        new_key = hashlib.pbkdf2_hmac(
            PasswordSecurer.HASH_NAME,
            provided_password.encode('utf-8'),
            salt = stored_password_bytes[:PasswordSecurer.SALT_LENGTH], # The salt is the first 32 bytes
            iterations = PasswordSecurer.HASH_ITERS
        )
        return new_key == stored_password_bytes[PasswordSecurer.SALT_LENGTH:] # The key is the last 32 bytes
import string
import secrets
import hashlib


class PasswordSecurer:
    salt_length = 32  # The length of the salt in bytes
    hash_name = 'sha256'  # The name of the hash digest algorithm to use
    hash_iterations = 100000 # It is recommended to use >= 100,000 iterations of SHA-256 

    @staticmethod
    def generate_temp_password(length: int) -> str:
        # Generates a secure temporary password
        alphabet = string.ascii_letters + string.digits + string.punctuation
        return ''.join(secrets.choice(string.printable) for i in range(length))

    @staticmethod
    def hash_password(password: str) -> str:
        # Hashes a password with a randomly generated salt
        salt = os.urandom(salt_length)  # A new salt for this user
        key = hashlib.pbkdf2_hmac(
            hash_name, # The hash digest algorithm
            password.encode('utf-8'), # Convert the password to bytes
            salt = salt, # Provide the salt
            iterations = hash_iterations  
        )
        storage = salt + key # Store the salt and key together
        return storage.hex() # Return the hashed password as hex digits for storage

    @staticmethod
    def verify_password(stored_password: bytes, provided_password: str) -> bool:
        # Verifies a provided password against the stored hash.
        stored_password_bytes = bytes.fromhex(stored_password)
        new_key = hashlib.pbkdf2_hmac(
            hash_name,
            provided_password.encode('utf-8'),
            salt = stored_password_bytes[:salt_length], # The salt is the first 32 bytes
            iterations = hash_iterations
        )
        return new_key == stored_password_bytes[salt_length:] # The key is the last 32 bytes
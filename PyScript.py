import hashlib
import time

def pbkdf2_with_custom_salt(password, salt, iterations, key_length):
    # Generate the derived key using PBKDF2HMAC
    derived_key = hashlib.pbkdf2_hmac(
        'sha256',               # Hash function (you can use other hashlib algorithms like 'sha1', 'md5', etc.)
        password.encode('utf-8'), # Convert the password to bytes
        salt,                   # Salt (should be a byte string)
        iterations,             # Number of iterations
        key_length              # Desired length of the derived key in bytes
    )
    return derived_key

# Example usage
if __name__ == "__main__":
    product_no = input("Enter Product No: ")
    imei_number = input("Enter IMEI Number: ")
    timestamp = str(int(time.time()))  # Get the current timestamp and convert to a string

    # Concatenate the three values and convert to a byte string to use as the salt
    salt = (product_no + imei_number + timestamp).encode('utf-8')

    iterations = 30000                        # Number of iterations (adjust based on your security requirements)
    key_length = 64                           # Desired key length in bytes (adjust based on your needs)

    password = input("Enter the password: ")

    # Derive the key using PBKDF2 with the custom salt
    derived_key = pbkdf2_with_custom_salt(password, salt, iterations, key_length)

    print("Derived Key (hex):", derived_key.hex())

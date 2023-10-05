from Crypto.Cipher import ARC4
import os

def encrypt_file(file_path, key):
    # Create the RC4 cipher object
    cipher = ARC4.new(key)

    # Read the file data
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Encrypt the file data
    encrypted_data = cipher.encrypt(file_data)

    # Write the encrypted data to a new file
    encrypted_file_path = file_path + ".enc"
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    print("File encrypted successfully. Encrypted file saved as:", encrypted_file_path)


# Example usage
file_path = "new.txt"
key = b"mysecretpasswordkey"  # Any length of bytes

encrypt_file(file_path, key)

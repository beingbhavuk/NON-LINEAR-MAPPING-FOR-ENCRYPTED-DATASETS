from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import os

def encrypt_file(file_path, key):
    # Generate a random initialization vector
    iv = get_random_bytes(8)

    # Create the DES cipher object
    cipher = DES.new(key, DES.MODE_CBC, iv)

    # Encrypt the file
    encrypted_data = b""
    with open(file_path, 'rb') as file:
        # Read the file in chunks of 8 bytes
        chunk = file.read(8)
        while len(chunk) > 0:
            # Pad the chunk if it's smaller than 8 bytes
            chunk += b" " * (8 - len(chunk))
            # Encrypt the chunk
            encrypted_chunk = cipher.encrypt(chunk)
            # Append the encrypted chunk to the encrypted data
            encrypted_data += encrypted_chunk
            # Read the next chunk
            chunk = file.read(8)

    # Write the encrypted data to a new file
    encrypted_file_path = file_path + ".enc"
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(iv)
        encrypted_file.write(encrypted_data)

    print("File encrypted successfully. Encrypted file saved as:", encrypted_file_path)


# Example usage
file_path = "new.txt"
key = b"mysecret"  # 8 bytes long

encrypt_file(file_path, key)

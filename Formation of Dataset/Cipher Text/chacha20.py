from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
import os

def encrypt_file(file_path, key, nonce):
    # Create the ChaCha20 cipher object
    cipher = ChaCha20.new(key=key, nonce=nonce)

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


def decrypt_file(encrypted_file_path, key, nonce):
    # Create the ChaCha20 cipher object
    cipher = ChaCha20.new(key=key, nonce=nonce)

    # Read the encrypted file data
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    # Decrypt the file data
    decrypted_data = cipher.decrypt(encrypted_data)

    # Write the decrypted data to a new file
    decrypted_file_path = encrypted_file_path[:-4]  # Remove the ".enc" extension
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

    print("File decrypted successfully. Decrypted file saved as:", decrypted_file_path)


# Example usage
file_path = "new.txt"
key = b"mysecretkeypasswordforchachaencr"  # 256-bit key
nonce = b"mysecretpass"  # 96-bit nonce

encrypt_file(file_path, key, nonce)
# decrypt_file(file_path + ".enc", key, nonce)
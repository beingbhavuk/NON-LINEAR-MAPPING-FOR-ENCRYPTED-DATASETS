File Encryption in Python

This Python script demonstrates how to encrypt a file in Cipher Block Chaining (CBC) mode. It uses the 'pycryptodome' library to perform the encryption.

Before Running program make sure you have the following prerequisites:

1) Python 3.x installed on your system.

2) The pycryptodome library installed. You can install it using pip:
   pip install pycryptodome

USAGE:

1) Save your file that you want to encrypt in the same directory as this script or provide the full path to the file in the 'file_path' variable in the script.

2) Open the script (encrypt_file.py) in a text editor and set your desired encryption key in the key variable.

3) Run the script.

4) The script will generate an encrypted file with a ".enc" extension in the same directory as your original file. The initialization vector (IV) is prepended to the encrypted data in the output file.

5) Make sure to keep your encryption key safe. Losing the key will result in data loss as it's required for decryption.
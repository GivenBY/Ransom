import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Set the encryption key for AES
encryption_key = b"12345678"
path=os.getcwd()
# Function to encrypt a file using AES
def encrypt_file(file_path, key):
    # Generate a random initialization vector (IV)
    iv = os.urandom(16)

    # Read the contents of the file
    with open(file_path, "rb") as file:
        file_contents = file.read()

    # Pad the file contents to a multiple of 16 bytes
    padded_contents = pad(file_contents, AES.block_size)

    # Create a new AES cipher
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Encrypt the padded contents
    encrypted_contents = cipher.encrypt(padded_contents)

    # Return the IV and encrypted contents as a tuple
    return (iv, encrypted_contents)

# Encrypt the file
iv, encrypted_contents = encrypt_file(path, encryption_key)

# Write the IV and encrypted contents to a new file
with open(path+"\encrypted_file.bin", "wb") as encrypted_file:
    encrypted_file.write(iv)
    encrypted_file.write(encrypted_contents)

import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Set the decryption key for AES
decryption_key = b"12345678"
path=os.getcwd()
# Function to decrypt a file using AES
def decrypt_file(iv, encrypted_contents, key):
    # Create a new AES cipher
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the encrypted contents
    padded_contents = cipher.decrypt(encrypted_contents)

    # Unpad the contents
    file_contents = unpad(padded_contents, AES.block_size)

    # Return the decrypted contents
    return file_contents

# Read the IV and encrypted contents from the file
with open(path+"\encrypted_file.bin", "rb") as encrypted_file:
    iv = encrypted_file.read(16)
    encrypted_contents = encrypted_file.read()

# Decrypt the file
decrypted_contents = decrypt_file(iv, encrypted_contents, decryption_key)

# Write the decrypted contents to a new file
with open("path/to/decrypted_file.txt", "wb") as decrypted_file:
    decrypted_file.write(decrypted_contents)

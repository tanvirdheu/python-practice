# python program to encrypt message

import random
import string

# function to encryption
def encrypt(chars, key):
    plain_text = input("Enter a message to encrypt: ")
    encrypt_text = ""

    for letter in plain_text:
        index = chars.index(letter)
        encrypt_text += key[index]

    print(f"Original message: {plain_text}")
    print(f"Encrypted message: {encrypt_text}")

# function to decryption
def decrypt(chars, key):
    decrypt_text = input("Enter a message to decrypt: ")
    plain_text = ""

    for letter in decrypt_text:
        index = key.index(letter)
        plain_text += chars[index]

    print(f"Encrypted message: {decrypt_text}")
    print(f"Decrypted message: {plain_text}")

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars : {chars}")
# print(f"key: {key}")

encrypt(chars, key)
decrypt(chars, key)



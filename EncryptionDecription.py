import string
import random

#adding all keybinds to char
chars = " " + string.punctuation + string.digits + string.ascii_letters 

#creating a list for char
chars = list(chars)

#copying char elements
key = chars.copy()

#this makes the list for the key randomized, so the encryption is never the same
random.shuffle(key)

#wouldn't want our users to see this now would we??? -_- 
#print(f"\nchars: {chars}")
#print(f"\nkey: {key}")

#encrytion
plain_text = input('\nEnter a message to encrypt: ')
encrypted_text = ""

for letter in plain_text:
    index = chars.index(letter)
    encrypted_text += key[index]

print(f"Original message: {plain_text}")
print(f"Encrypted message: {encrypted_text}")

#decryption 
encrypted_text = input('\nEnter a message for decrypt: ')
plain_text = ""

for letter in encrypted_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted message: {encrypted_text}")
print(f"Original message: {plain_text}")








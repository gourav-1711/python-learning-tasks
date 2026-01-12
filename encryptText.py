import random
import string

chars = string.ascii_letters + string.digits + string.punctuation + string.whitespace  

chars = list(chars)
keys = chars.copy()

random.shuffle(keys)
# print(chars)
# print(keys)


text = input("Enter a message to encrypt : ")
encrypted = ""

for letter in text:
    index = chars.index(letter)
    encrypted += keys[index]

print(f"YOUR MESSAGE : {text}")
print(f"ENCRYPTED : {encrypted}") 
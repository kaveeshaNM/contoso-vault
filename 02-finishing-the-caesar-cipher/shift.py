ALPHABET_SIZE = 26

message = str(input("Message: "))  # "ABZ78"
key = int(input("Key: "))

ciphertext = ""

#Encryption
for character in message: 
    if "A" <= character <= "Z":
        shifted = ord(character) + key 
        if shifted > ord("Z"):
            shifted -= ALPHABET_SIZE
        ciphertext += chr(shifted)
    else:
        ciphertext += character

print("ciphertext: ",ciphertext)

#Decryption

plaintext = ""

for character in ciphertext: 
    if "A" <= character <= "Z":
        shifted = ord(character) - key  
        if shifted < ord("A"):
            shifted += ALPHABET_SIZE
        plaintext += chr(shifted)
    else:
        plaintext += character
print("plaintext: ",plaintext)  
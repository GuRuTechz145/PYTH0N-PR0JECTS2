def caesar_decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - ascii_offset - key) % 26 + ascii_offset)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext


ciphertext = input("Enter the ciphertext: ")
key = int(input("Enter the key (a number between 1 and 25): "))

plaintext = caesar_decrypt(ciphertext, key)
print("Decrypted plaintext:", plaintext)

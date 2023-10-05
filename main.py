def caesar_encrypt(text, shift):


    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_text += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

shift = 3  

text= str(input("Zadej text k zasifrovani: "))
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)
encrypted_text = caesar_encrypt(text, shift)
print("Zasifrovany text:", encrypted_text)

decrypted_text = caesar_decrypt(encrypted_text, shift)
print("Rozsifrovany text:", decrypted_text)
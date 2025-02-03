def encrypt(plaintext, shift):
    encrypted_text = ""
    
    for char in plaintext:
        if char.isalpha():  
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Add non-alphabet characters unchanged
            
    return encrypted_text

def decrypt(ciphertext, shift):
    decrypted_text = ""
    
    for char in ciphertext:
        if char.isalpha():  
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char  # Add non-alphabet characters unchanged
            
    return decrypted_text

if __name__ == "__main__":  # Corrected this line
    action = input("Would you like to (e)ncrypt or (d)ecrypt? ").lower()
    text = input("Enter the text: ")
    
    try:
        shift = int(input("Enter the shift value: "))
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        exit(1)
    
    if action == 'e':
        encrypted = encrypt(text, shift)
        print(f"Encrypted: {encrypted}")
    elif action == 'd':
        decrypted = decrypt(text, shift)
        print(f"Decrypted: {decrypted}")
    else:
        print("Invalid action. Please choose 'e' or 'd'.")
      

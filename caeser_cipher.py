def encrypt(text, shift):
    """
    Encrypts the input text using the Caesar cipher algorithm.
    
    Parameters:
    text (str): The text to be encrypted.
    shift (int): The number of positions to shift each character.
    
    Returns:
    str: The encrypted text.
    """
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = shift % 26  # Ensure the shift is within the range of 0-25
            if char.islower():  # Check if the character is lowercase
                shifted_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
                '''The ord determines the unicode of a character... like the ord('a') is 97
                So the ord(char) will return the unicode of whatever character is inputted like if it is 'c', that is 99
                (ord(char) - ord('a') = shift_amount will subtract the unicode of the two and add to the shift amount
                 % 26 this is to enable that the resulgt of the previous line does not exceed the 0-25, if it does it is wrapped
                 + ord('a'); this adds the value back to 97(Unicode of a)
                chr(.....): This returns the character of the unicode, e.g chr(99) is c'''
            else:  # The character is uppercase
                shifted_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_text += shifted_char
        else:
            encrypted_text += char  # Non-alphabetic characters are added as is meaning they are just copied as they are
    return encrypted_text

def decrypt(text, shift):
    """
    Decrypts the input text using the Caesar cipher algorithm by reversing the shift.
    
    Parameters:
    text (str): The text to be decrypted.
    shift (int): The number of positions to shift each character back.
    
    Returns:
    str: The decrypted text.
    """
    return encrypt(text, -shift)# the minus before the shift is to take the text back to its position like decrypting back

def main():
    """
    The main function that provides a simple user interface for the Caesar cipher program.
    """
    choice = input("Would you like to (e)ncrypt or (d)ecrypt? ").lower()
    '''This just basically asks which the user would like to do, encrypt or decrypt. And the .lower()just changes everything to lowercase'''
    if choice not in ['e', 'd']:
        print("Invalid choice. Please choose 'e' to encrypt or 'd' to decrypt.")#self explnatory, if the user does not select
        return                                                                        #e or d, there should return that error in print

    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'e':
        result = encrypt(text, shift)
        print(f"Encrypted text: {result}")
    else:
        result = decrypt(text, shift)
        print(f"Decrypted text: {result}")#So basically, the f before the string just says that it is a formatted string literal that 
                                          #allows embedded expressions inside co#urly bacelets

if __name__ == "__main__":
    main()#This just ensures that the script will run only when it is executed directly

# Caesar Cipher

This project implements a simple Caesar Cipher encryption and decryption algorithm in Python. The Caesar Cipher is one of the earliest known encryption techniques, where each letter in the plaintext is shifted a fixed number of places down or up the alphabet.

## Features

- Encrypts plaintext using a specified shift.
- Decrypts ciphertext using a specified shift.
- Handles both uppercase and lowercase letters.
- Ignores non-alphabetical characters.

## Getting Started

### Prerequisites

- Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/your-username/caesar-cipher.git
    ```

2. **Navigate to the project directory**:
    ```sh
    cd caesar-cipher
    ```

### Usage

1. **Run the script**:
    ```sh
    python caesar_cipher.py
    ```

2. **Follow the prompts**:
    - Choose whether you want to (e)ncrypt or (d)ecrypt a message.
    - Enter the text you want to process.
    - Enter the shift value (an integer).

### Example

```sh
Would you like to (e)ncrypt or (d)ecrypt? e
Enter the text: Hello, World!
Enter the shift value: 3
Encrypted text: Khoor, Zruog!

Would you like to (e)ncrypt or (d)ecrypt? d
Enter the text: Khoor, Zruog!
Enter the shift value: 3
Decrypted text: Hello, World!


HOW IT WORKS

The Caesar Cipher shifts each letter in the input text by a fixed number of positions down the alphabet. For example, with a shift of 1, A becomes B, B becomes C, and so on. The script handles both encryption and decryption:

Encryption: Shifts letters forward in the alphabet.
Decryption: Shifts letters backward in the alphabet.
Encryption Function
python
Copy code
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                shifted_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                shifted_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text
Decryption Function python
Copy code:
def decrypt(text, shift):
    return encrypt(text, -shift)

 LICENSE
This project is licensed under the MIT License. See the LICENSE file for details.

    CONRIBUTIONS
Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features.

    Acknowledgements
Inspired by the simplicity and historical significance of the Caesar Cipher.

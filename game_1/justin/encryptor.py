#!/usr/bin/python3
def password_to_binary(password):
    binary_password = ''
    for char in password:
        binary_char = bin(ord(char))[2:].zfill(8)
        binary_password += binary_char
    return binary_password

def encrypt_message(message, binary_password):
    encrypted_message = ''
    password_length = len(binary_password)
    for i, char in enumerate(message):
        if char == ' ':
            encrypted_message += ' '
        else:
            password_index = i % password_length
            xor_result = ord(char) ^ int(binary_password[password_index])
            encrypted_message += chr(xor_result)
    return encrypted_message

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None


password = input("Enter a four-character password: ")
if len(password) != 4:
    print("Password must be exactly four characters long.")
else:
    filename = input("Enter the name of the file containing the message: ")

    message = read_file(filename)
    if message:

        binary_password = password_to_binary(password)

        encrypted_message = encrypt_message(message, binary_password)
        print("Encrypted message:", encrypted_message)

def password_to_binary(password):
    binary_password = ''
    for char in password:
        binary_char = bin(ord(char))[2:].zfill(8)
        binary_password += binary_char
    return binary_password

def decrypt_message(encrypted_message, binary_password):
    decrypted_message = ''
    password_length = len(binary_password)
    for i, char in enumerate(encrypted_message):
        if char == ' ':
            decrypted_message += ' '
        else:
            password_index = i % password_length
            xor_result = ord(char) ^ int(binary_password[password_index])
            decrypted_message += chr(xor_result)
    return decrypted_message

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None


password = input("Enter the four-character password used for encryption: ")
if len(password) != 4:
    print("Password must be exactly four characters long.")
else:
    encrypted_filename = input("Enter the name of the file containing the encrypted message: ")
    binary_password = password_to_binary(password)


    encrypted_message = read_file(encrypted_filename)
    if encrypted_message:

        decrypted_message = decrypt_message(encrypted_message, binary_password)
        print("Decrypted message:", decrypted_message)

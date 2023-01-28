# Elias Woldie
# Object-Oriented programming –-> Inheritance
# This program allows the user to encrypt or decrypt messages using different types of encryption methods.
# Encrypted messages will read from the console and then written to a file called ‘message.txt’, and 
# decrypted messages will be read from the ‘message.txt’ file then displayed to the console.




import check_input
import cipher
import caesar_cipher


def main():
    c = cipher.Cipher()
    encordec = check_input.get_int_range("Secret Decoder Ring:\n 1. Encrypt \n 2. Decrypt\n", 1, 2)
    if encordec == 1:
        encrypt_choice = check_input.get_int_range("Enter encryption type: \n 1. Atbash  \n 2. Caesar \n", 1, 2)
        message_input = input("Enter message: ")
        shift = check_input.get_int_range("Enter a shift value (0-25): ", 1, 25)
        cc = caesar_cipher.CasesarCipher(shift)
        if encrypt_choice == 1:
            with open('message.txt', 'w') as message:
                message.write(c.encrypt_message(message_input))
        else:
            with open('message.txt', 'w') as message:
                message.write(cc.encrypt_message(message_input))
    elif encordec == 2:
        decrept_choice = check_input.get_int_range("Enter encryption type: \n 1. Atbash  \n 2. Caesar \n", 1, 2)
        shift_choice = check_input.get_int("Enter shift value: ")
        cc = caesar_cipher.CasesarCipher(shift_choice)
        if decrept_choice == 1:
            with open('message.txt', 'r') as message:
                read = message.read()
                message.read(c.decrypt_message(read))
        else:
            with open('message.txt', 'r') as message:
                message.read(cc._decrypt_letter(shift_choice))

main()
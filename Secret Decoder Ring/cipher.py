import string


class Cipher:
    """
    This class implements the Atbash Cipher
    Attributes:
        alphabet(chr) - list with the letters A-Z
    """
    def __init__(self):
        # Initializes the alphabet A-Z
        self.alphabet = list(string.ascii_uppercase)

    def encrypt_message(self, message):
        """
        Convert the message to upper case letters, then loop through the message string one character at a time, if it
        is a letter A-Z, then call the encrypt_letter method, otherwise ignore the character.
        :param message:
        :return: string
        """
        # Convert the message to upper case letters
        message = message.upper()
        new_message = ""
        # looping through the message string one character at a time
        for i in message:
            # if it is a letter A-Z, then call the encrypt_letter method, otherwise ignore the character.
            if i in self.alphabet:
                new_message += self._encrypt_letter(i)
            else:
                new_message += str(i)
        return new_message

    def decrypt_message(self, message):
        """
        Convert the message to upper case letters, then loop through the message string one character at a time, if it
        is a letter A-Z, then call the decrypt_letter method, otherwise ignore the character.

        :param message:
        :return: string
        """
        message = message.upper()
        new_message = ""
        # looping through the message string one character at a time
        for i in message:
            # if it is a letter A-Z, then call the encrypt_letter method, otherwise ignore the character.
            if i in self.alphabet:
                new_message += self._decrypt_letter(i)
            else:
                new_message += str(i)
        return new_message

    def _encrypt_letter(self, letter):
        """
        Looks up the letter in the alphabet to find its location and the uses that location to calculate the position of
        the encrypted letter then return the encrypted letter.
        :param letter:
        :return: char
        """
        # Initializes location to the index of the letter
        location = self.alphabet.index(letter)
        # Initializes position location - to the last index of the alphabet(25)
        position = 25 - location
        # Initializes the encrypted letter to the alphabets index
        encryptedletter = self.alphabet[position]
        return encryptedletter

    def _decrypt_letter(self, letter):
        """
        Looks up the letter in the alphabet to find its location and the uses that location to calculate the position of
        the encrypted letter then return the decrypted letter.
        :param letter:
        :return: char
        """
        # Initializes position to location - to the last index of the alphabet(25)
        location = self.alphabet.index(letter)
        # Initializes position to the last index of the alphabet(25) - to location
        position = location - 25
        # Initializes the encrypted letter to the alphabets index
        decryptedletter = self.alphabet[position]
        return decryptedletter










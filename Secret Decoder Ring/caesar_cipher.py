import cipher


class CasesarCipher(cipher.Cipher):
    """
    This class implements a Caesar Cipher. Inherits from the Cipher class
    """
    def __init__(self, shift):
        # giving access to methods in the parent class
        super().__init__()
        # Initializing the shift value
        self.shift = shift

    def _encrypt_letter(self, letter):
        """

        :param letter:
        :return: int
        """

        location = self.alphabet.index(letter)
        position = location + self.shift
        if position in range(1, 26):
            encryptedletter = self.alphabet[position]
        else:
            position = position - 26
            encryptedletter = self.alphabet[position]
        return encryptedletter

    def _decrypt_letter(self, letter):
        location = self.alphabet.index(letter)
        position = location - self.shift
        encryptedletter = self.alphabet[position]
        return encryptedletter
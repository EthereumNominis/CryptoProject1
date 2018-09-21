from baseCipher import Cipher


# -------------------- CBC Cipher -------------------- #
class CBCCipher(Cipher):

    def encrypt(self, msg_array):
        """
        Encrypt the message array
        :param msg_array: ((0, b'Lorem ipsum dolo'), (1, b'r sit amet, cons'),......)
        :return:tuple(encrypted_message_array): (b'\xd9v\xf6\xfa\xa2\xa2\x1cCS\x99\x04[0ahD', b'\xe98\x02\x069\x1f\xab\xa2i]\x8e.>.\xc6/', b'\x1eV\x15k\xac\x9dnY\xa0v\xf6\xe2\xd5\x04\xac\x86', ......)
        """
        # print(msg_array)
        if len(msg_array) == 0:
            raise Exception("Input Message should NOT be NONE......")
        encrypted_message_array = list()
        for i in msg_array:
            if i[0] == 0:
                encrypted_message_array.append(self.AESCipher.encrypt(self.xor(self.IV, i[1])))
            else:
                encrypted_message_array.append(
                    self.AESCipher.encrypt(self.xor(encrypted_message_array[i[0] - 1], i[1])))
        encrypted_message_bytes = bytes()
        for k in encrypted_message_array:
            encrypted_message_bytes += k
        return tuple(encrypted_message_array)

    def decrypt(self, cipher_text_array):
        """
        Decrypt cipher message array
        :param cipher_text_array: (b'\......',b'\......',b'\......',b'\......')
        :return:decrypt_message_array: (b'\......',b'\......',b'\......',b'\......')
        """
        # print(cipher_text_array)
        if len(cipher_text_array) == 0:
            raise Exception("The Cipher text cannot be NONE......")
        decrypt_message_array = list()
        index = 0
        for i in cipher_text_array:
            if index == 0:
                decrypt_message_array.append(self.xor(self.AESCipher.decrypt(i), self.IV))
                index += 1
            else:
                decrypt_message_array.append(self.xor(self.AESCipher.decrypt(i), cipher_text_array[index - 1]))
                index += 1
        return tuple(decrypt_message_array)

    def unpadded(self, decrypt_msg_array):
        """
        Convert decrypted message array into unpadded string
        :param decrypted_message_array: array of padded decrypted message array
        :return: unpadded string
        """
        unpadded_str = str()
        num_of_bytes_cutted = decrypt_msg_array[-1][-1]
        # print(decrypt_msg_array[-1])
        # print((decrypt_msg_array[-1][:-num_of_bytes_cutted]).decode('latin-1'))
        for i in range(len(decrypt_msg_array)):
            if i == len(decrypt_msg_array)-1:
                unpadded_str += (decrypt_msg_array[-1][:-num_of_bytes_cutted]).decode('latin-1')
            else:
                unpadded_str += (decrypt_msg_array[i]).decode('latin-1')
        return unpadded_str

    def setIV(self, ivBytes):
        self.IV = ivBytes




if __name__ == '__main__':
    my_cbc_cipher = CBCCipher('ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', 16)
    iv = my_cbc_cipher.IV
    print("IV->\n", iv.hex(), "\n\n")
    print(iv)
    plaintext = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut ' \
                'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris' \
                ' nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit ' \
                'esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat ' \
                'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum'
    plaintext_bytes = bytes(plaintext, 'latin-1')
    padded_plaintext_bytes = my_cbc_cipher.pad(plaintext_bytes)
    print("CBC MODE:" + '\n>' * 3)
    # print(padded_plaintext_bytes)
    cipher_text_array = my_cbc_cipher.encrypt(padded_plaintext_bytes)
    print("\nCipher->\n\t")
    for i in cipher_text_array:
        print(i.hex())
        print(i.decode('latin-1'))
    # print('\n\n\nCBC-mode CIPHER ENCRYPTION OUTPUT:')
    decrypt_msg_array = my_cbc_cipher.decrypt(cipher_text_array)
    print("\nDecrypt->\n\t", decrypt_msg_array,"\n\n")
    my_cbc_cipher.unpadded(decrypt_msg_array)

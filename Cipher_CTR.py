from baseCipher import Cipher


# -------------------- CTR Cipher -------------------- #
class CTRCipher(Cipher):

    def encrypt(self, msg_array_item):
        confusion = (int.from_bytes(self.IV, byteorder='big') + msg_array_item[0])
        conf_bytes = confusion.to_bytes(16, byteorder='big')
        cipher_item = self.xor(self.AESCipher.encrypt(conf_bytes), msg_array_item[1])
        return cipher_item


    def decrypt(self, cipher_msg_item):
        # print(cipher_msg_item[1].hex())
        # print(self.IV.hex())
        confusion = (int.from_bytes(self.IV, byteorder='big') + cipher_msg_item[0])
        conf_bytes = confusion.to_bytes(16, byteorder='big')
        plain_item = self.xor(self.AESCipher.encrypt(conf_bytes), cipher_msg_item[1])
        # print(plain_item)
        return plain_item

    def unpadded(self, msg_array):
        print("\n\n\n\n")
        unpadded_string = str()
        num_of_bytes_cutted = ord(msg_array[-1][-1])
        # num_of_bytes_cutted = b'\x10'
        # print(ord(num_of_bytes_cutted))
        for i in range(len(msg_array)):
            if i == len(msg_array)-1:
                unpadded_string += (msg_array[i][:-num_of_bytes_cutted])
            else:
                unpadded_string += msg_array[i]
        # print(repr(unpadded_string))
        return unpadded_string

    def setIV(self, ivstringBytes):
        self.IV = ivstringBytes

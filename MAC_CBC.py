from Crypto.Cipher import AES
import os
import hashlib
import binascii
from numpy import frombuffer, bitwise_xor, byte
from baseCipher import Cipher

# BLOCK SIZE
BYTES = 16

class mac_cbc_cipher(Cipher):

    def __init__(self, key, bytes_per_block):

        Cipher.__init__(self, key, bytes_per_block)

    def verify(self, msg, proposed_tag):
        # check if padded
        if not len(msg) % self.bytes_per_block == 0:
            print('unpadded')
            return 0
        else:
            true_tag = self.gen_mac(msg)
            return true_tag == proposed_tag

    #accepts string
    def tag(self, msg):
        #
        bytes_unpadded = bytes(msg,'latin-1')
        bytes_padded = self.pad(bytes_unpadded)
        #
        m_0 = len(bytes_padded).to_bytes(16,byteorder='big')
        aes_output = self.AESCipher.encrypt(m_0)
        for byte in bytes_padded:
            xor_output = self.xor(byte[1],aes_output)
            aes_output = self.AESCipher.encrypt(xor_output)
        return aes_output

    def encrypt(self, msg_array):
        pass

    def decrypt(self, cipher_msg_array):
        pass

def main():
    BYTES = 16
    # Test vector for the empty string:
    #
    #
    # msg = empty
    # K = 603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4
    # Tag = 028962f61b7bf89efc6b551f4667d983
    key_string1 = '603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4'




    #tag_string = ''
    #tag_hex = int(tag_string,16).to_bytes(len(tag_string),byteorder='big')


    mycipher = mac_cbc_cipher(key_string1, BYTES)


    msg1 = ''
    filename = 'sherlock_holmes.txt'
    with open(filename) as f:
        msg2 = f.readlines()


    my_tag = mycipher.tag(str(msg2))
    print(my_tag)
    print(len(my_tag))

    my_tag = mycipher.tag(msg1)
    print(my_tag)
    print(len(my_tag))
















if __name__ == "__main__":
    main()




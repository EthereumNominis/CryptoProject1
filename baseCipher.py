import abc
from Crypto.Cipher import AES
import os
import hashlib
import binascii
from numpy import frombuffer, bitwise_xor, byte


# -------------------- Abstract Base Class: Cipher -------------------- #
class Cipher(abc.ABC):

    def __init__(self, key, bytes_per_block):
        self.key = bytes.fromhex(key)
        self.IV = os.urandom(bytes_per_block)
        self.bytes_per_block = bytes_per_block
        self.AESCipher = AES.new(self.key, AES.MODE_ECB)

    # numpy xor, returns byte literal
    def xor(self, a, b):
        # print(a)
        # print (b)
        a_buff = frombuffer(a, dtype=byte)
        b_buff = frombuffer(b, dtype=byte)
        output = bitwise_xor(a_buff, b_buff)
        return output.tostring()

    # expects bytes
    def pad(self, msg):
        block_len = self.bytes_per_block
        block_pad = (block_len - len(msg) % block_len)
        block_pad = (block_len - len(msg) % block_len) * chr(block_pad)
        block_pad = binascii.a2b_qp(block_pad)
        # print("size:\t\t", self.bytes_per_block)
        num_of_substr = int(len(msg + block_pad) / self.bytes_per_block)
        complete_message = msg + block_pad
        msg_array = list()
        for i in range(num_of_substr):
            msg_array.append((i, complete_message[i * self.bytes_per_block: (i + 1) * self.bytes_per_block]))
        return tuple(msg_array)

    @abc.abstractmethod
    def encrypt(self, msg_array):
        """ Encrypt Message with previous input """

    @abc.abstractmethod
    def decrypt(self, cipher_msg_array):
        """ Decrypt Message """

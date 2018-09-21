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



def vector_for_test_CBC(i):
    list_of_keys = [
        "6ed76d2d97c69fd1339589523931f2a6cff554b15f738f21ec72dd97a7330907",
        "dce26c6b4cfb286510da4eecd2cffe6cdf430f33db9b5f77b460679bd49d13ae",
        "fe8901fecd3ccd2ec5fdc7c7a0b50519c245b42d611a5ef9e90268d59f3edf33",
        "0493ff637108af6a5b8e90ac1fdf035a3d4bafd1afb573be7ade9e8682e663e5",
        "9adc8fbd506e032af7fa20cf5343719de6d1288c158c63d6878aaf64ce26ca85",
        "73b8faf00b3302ac99855cf6f9e9e48518690a5906a4869d4dcf48d282faae2a",
        "9ddf3745896504ff360a51a3eb49c01b79fccebc71c3abcb94a949408b05b2c9",
        "458b67bf212d20f3a57fce392065582dcefbf381aa22949f8338ab9052260e1d",
        "d2412db0845d84e5732b8bbd642957473b81fb99ca8bff70e7920d16c1dbec89",
        "48be597e632c16772324c8d3fa1d9c5a9ecd010f14ec5d110d3bfec376c5532b"
    ]
    list_of_iv = [
        "851e8764776e6796aab722dbb644ace8",
        "fdeaa134c8d7379d457175fd1a57d3fc",
        "bd416cb3b9892228d8f1df575692e4d0",
        "c0cd2bebccbb6c49920bd5482ac756e8",
        "11958dc6ab81e1c7f01631e9944e620f",
        "b3cb97a80a539912b8c21f450d3b9395",
        "e79026639d4aa230b5ccffb0b29d79bc",
        "4c12effc5963d40459602675153e9649",
        "51c619fcf0b23f0c7925f400a6cacb6d",
        "d6d581b8cf04ebd3b6eaa1b53f047ee1"
    ]
    list_of_plainText = [
        "6282b8c05c5c1530b97d4816ca434762",
        "50e9eee1ac528009e8cbcd356975881f957254b13f91d7c6662d10312052eb00",
        "8d3aa196ec3d7c9b5bb122e7fe77fb1295a6da75abe5d3a510194d3a8a4157d5c89d40619716619859da3ec9b247ced9",
        "8b37f9148df4bb25956be6310c73c8dc58ea9714ff49b643107b34c9bff096a94fedd6823526abc27a8e0b16616eee254ab4567dd68e8ccd4c38ac563b13639c",
        "c7917f84f747cd8c4b4fedc2219bdbc5f4d07588389d8248854cf2c2f89667a2d7bcf53e73d32684535f42318e24cd45793950b3825e5d5c5c8fcd3e5dda4ce9246d18337ef3052d8b21c5561c8b660e",
        "3adea6e06e42c4f041021491f2775ef6378cb08824165edc4f6448e232175b60d0345b9f9c78df6596ec9d22b7b9e76e8f3c76b32d5d67273f1d83fe7a6fc3dd3c49139170fa5701b3beac61b490f0a9e13f844640c4500f9ad3087adfb0ae10",
        "cf52e5c3954c51b94c9e38acb8c9a7c76aebdaa9943eae0a1ce155a2efdb4d46985d935511471452d9ee64d2461cb2991d59fc0060697f9a671672163230f367fed1422316e52d29eceacb8768f56d9b80f6d278093c9a8acd3cfd7edd8ebd5c293859f64d2f8486ae1bd593c65bc014",
        "256fd73ce35ae3ea9c25dd2a9454493e96d8633fe633b56176dce8785ce5dbbb84dbf2c8a2eeb1e96b51899605e4f13bbc11b93bf6f39b3469be14858b5b720d4a522d36feed7a329c9b1e852c9280c47db8039c17c4921571a07d1864128330e09c308ddea1694e95c84500f1a61e614197e86a30ecc28df64ccb3ccf5437aa",
        "026006c4a71a180c9929824d9d095b8faaa86fc4fa25ecac61d85ff6de92dfa8702688c02a282c1b8af4449707f22d75e91991015db22374c95f8f195d5bb0afeb03040ff8965e0e1339dba5653e174f8aa5a1b39fe3ac839ce307a4e44b4f8f1b0063f738ec18acdbff2ebfe07383e734558723e741f0a1836dafdf9de82210a9248bc113b3c1bc8b4e252ca01bd803",
        "0c63d413d3864570e70bb6618bf8a4b9585586688c32bba0a5ecc1362fada74ada32c52acfd1aa7444ba567b4e7daaecf7cc1cb29182af164ae5232b002868695635599807a9a7f07a1f137e97b1e1c9dabc89b6a5e4afa9db5855edaa575056a8f4f8242216242bb0c256310d9d329826ac353d715fa39f80cec144d6424558f9f70b98c920096e0f2c855d594885a00625880e9dfb734163cecef72cf030b8"
    ]
    list_of_cipherText = [
        "6acc04142e100a65f51b97adf5172c41",
        "2fa0df722a9fd3b64cb18fb2b3db55ff2267422757289413f8f657507412a64c",
        "608e82c7ab04007adb22e389a44797fed7de090c8c03ca8a2c5acd9e84df37fbc58ce8edb293e98f02b640d6d1d72464",
        "05d5c77729421b08b737e41119fa4438d1f570cc772a4d6c3df7ffeda0384ef84288ce37fc4c4c7d1125a499b051364c389fd639bdda647daa3bdadab2eb5594",
        "9c99e68236bb2e929db1089c7750f1b356d39ab9d0c40c3e2f05108ae9d0c30b04832ccdbdc08ebfa426b7f5efde986ed05784ce368193bb3699bc691065ac62e258b9aa4cc557e2b45b49ce05511e65",
        "ac3d6dbafe2e0f740632fd9e820bf6044cd5b1551cbb9cc03c0b25c39ccb7f33b83aacfca40a3265f2bbff879153448acacb88fcfb3bb7b10fe463a68c0109f028382e3e557b1adf02ed648ab6bb895df0205d26ebbfa9a5fd8cebd8e4bee3dc",
        "34df561bd2cfebbcb7af3b4b8d21ca5258312e7e2e4e538e35ad2490b6112f0d7f148f6aa8d522a7f3c61d785bd667db0e1dc4606c318ea4f26af4fe7d11d4dcff0456511b4aed1a0d91ba4a1fd6cd9029187bc5881a5a07fe02049d39368e83139b12825bae2c7be81e6f12c61bb5c5",
        "90b7b9630a2378f53f501ab7beff039155008071bc8438e789932cfd3eb1299195465e6633849463fdb44375278e2fdb1310821e6492cf80ff15cb772509fb426f3aeee27bd4938882fd2ae6b5bd9d91fa4a43b17bb439ebbe59c042310163a82a5fe5388796eee35a181a1271f00be29b852d8fa759bad01ff4678f010594cd",
        "0254b23463bcabec5a395eb74c8fb0eb137a07bc6f5e9f61ec0b057de305714f8fa294221c91a159c315939b81e300ee902192ec5f15254428d8772f79324ec43298ca21c00b370273ee5e5ed90e43efa1e05a5d171209fe34f9f29237dba2a6726650fd3b1321747d1208863c6c3c6b3e2d879ab5f25782f08ba8f2abbe63e0bedb4a227e81afb36bb6645508356d34",
        "fc5873e50de8faf4c6b84ba707b0854e9db9ab2e9f7d707fbba338c6843a18fc6facebaf663d26296fb329b4d26f18494c79e09e779647f9bafa87489630d79f4301610c2300c19dbf3148b7cac8c4f4944102754f332e92b6f7c5e75bc6179eb877a078d4719009021744c14f13fd2a55a2b9c44d18000685a845a4f632c7c56a77306efa66a24d05d088dcd7c13fe24fc447275965db9e4d37fbc9304448cd"
    ]
    return (list_of_keys[i], list_of_iv[i], list_of_plainText[i], list_of_cipherText[i])


def test_CBC():
    for k in range(9):
        (t_key, t_iv, t_plain, t_cipher) = vector_for_test_CBC(k)
        # print(t_key, t_iv, t_plain, t_cipher)
        my_cbc_cipher = CBCCipher(t_key, 16)
        my_cbc_cipher.setIV(bytes.fromhex(t_iv))
        PLAINTEXT_bytes = bytes.fromhex(t_plain)
        padded_plaintext_bytes = my_cbc_cipher.pad(PLAINTEXT_bytes)
        cipher_text_array = my_cbc_cipher.encrypt(padded_plaintext_bytes)
        cipherString = str()
        for x in cipher_text_array:
            cipherString += x.decode('latin-1')
        print("\n\ntest ", k, "\t:")
        print("=>:\t\t", (cipherString[:-16].encode('latin-1')).hex())
        print("*>:\t\t", t_cipher)



if __name__ == '__main__':
    # my_cbc_cipher = CBCCipher('ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff', 16)
    # iv = my_cbc_cipher.IV
    # print("IV->\n", iv.hex(), "\n\n")
    # print(iv)
    # plaintext = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut ' \
    #             'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris' \
    #             ' nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit ' \
    #             'esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat ' \
    #             'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum'
    # plaintext_bytes = bytes(plaintext, 'latin-1')
    # padded_plaintext_bytes = my_cbc_cipher.pad(plaintext_bytes)
    # print("CBC MODE:" + '\n>' * 3)
    # # print(padded_plaintext_bytes)
    # cipher_text_array = my_cbc_cipher.encrypt(padded_plaintext_bytes)
    # print("\nCipher->\n\t")
    # for i in cipher_text_array:
    #     print(i.hex())
    #     print(i.decode('latin-1'))
    # # print('\n\n\nCBC-mode CIPHER ENCRYPTION OUTPUT:')
    # decrypt_msg_array = my_cbc_cipher.decrypt(cipher_text_array)
    # print("\nDecrypt->\n\t", decrypt_msg_array,"\n\n")
    # my_cbc_cipher.unpadded(decrypt_msg_array)
    test_CBC()

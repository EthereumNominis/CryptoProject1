import multiprocessing
import os
import click
from Cipher_CTR import CTRCipher

my_ctr_cipher = CTRCipher('776BEFF2851DB06F4C8A0542C8696F6C6A81AF1EEC96B4D37FC1D689E6C1C104', 16)
output_queue = multiprocessing.Queue()


def readParameters(k, i):
    keyStringHex = str()
    plainText = str()
    with open(k, 'r') as keyFile:
        keyStringHex = keyFile.readline()
        print('\x1b[1;33;45m', "Successfully loaded key (Hex)\t", '\x1b[0m', repr(keyStringHex))
    with open(i, 'r') as inputPlainTextFile:
        plainTextMatrix = inputPlainTextFile.readlines()
        plainText = ''.join(plainTextMatrix)
        print('\x1b[1;33;45m', "Successfully loaded plain text file\t", '\x1b[0m')
    return (keyStringHex, plainText)


def encrypt_process(i):
    # print('\x1b[1;37;44m', "\tPid is\t",'\x1b[0m',os.getpid())
    cipherText = my_ctr_cipher.encrypt(i)
    output_queue.put((i[0], cipherText))


@click.command()
@click.option('-k',
              help='\"Key file\"\n=>\trequired, specifies a file storing a valid AES key as a hex encoded string\n.')
@click.option('-i', help='\"Input file\"\n=>\trequired, specifies the path of the file that is being operated on\n.')
@click.option('-o',
              help='\"Output file\"\n=>\trequired, specifies the path of the file where the resulting output is stored\n.')
def main(k, i, o):
    #      python3 ctr-enc.py -k temp/keyFile2 -i dataFiles/plain1.txt -o dataFiles/ctrO1
    # Applying CTR Cipher (Encryption)......
    #  Key file:        temp/keyFile2
    #  Input File:      dataFiles/plain1.txt
    #  Output File:     dataFiles/ctrO1
    #  Successfully loaded key (Hex)    '000102030405060708090a0b0c0d0e0ff0f1f2f3f4f5f6f7f8f9fafbfcfdfeff'
    #  Successfully loaded plain text file      "A good old man, sir; he will be talking: as they\nsay, when the age is in, the wit is out: God help\nus! it is a world to see. Well said, i' faith,\nneighbour Verges: well, God's a good man; an two men\nride of a horse, one must ride behind. An honest\nsoul, i' faith, sir; by my troth he is, as ever\nbroke bread; but God is to be worshipped; all men\nare not alike; alas, good neighbour!"
    #  IV is                    00000060db5672c97aa8f0b200000001
    #
    #
    #
    #                 Cipher Text
    #  0613d915bc834eca560320da30e0bf87
    #  00e8193e5c80d4730fdd5fb03dbe926a
    #  261e79f0ab75f1b1290dd124e085cb8b
    #  85775c159a55d4cf9f4f79c7fc1fc27d
    #  1dffc5120391b054a60333a04426d239
    #  068d7ca64e0c9a18ad7fbf930aacf715
    #  b89f716d46d88bf9fcb214e4813c9480
    #  3466a3a20a5dbed002bed1473078e45d
    #  a2756820901eabc153f0d2ebf4ec0c73
    #  7922956127308e17652c1f4538d39809
    #  23dad86c433a57e9de1b8a8123a88f08
    #  700f85f706ef8d8f955d77946892156e
    #  23cb4b5526d5fdd38dd1270ca7e7de7d
    #  254a95893fa0edf352b069295dee5e5a
    #  7368d7f169877b22214dd2f902636177
    #  4dd28ac0ad0bfd9731c675b6fe5348a5
    #  1381adab88783cb77f3ee9cdd1bd3137
    #  2c0e223a4979ca6b485dc014622dcb46
    #  f67a39634d56e39c86d405e03a102e59
    #  9321d6676ef0132964ee2ee0e8d0e5fb
    #  662b2d51531d1a6fb8298d65f28a8c7f
    #  d577684231daa3d6824adb6610b3acad
    #  6b254c7a663f3f4d98ac29c38044e03d
    #  523cefbffd94965db73f6b2f2247d0c9
    #                         Encryption Finished!

    # -------------------- Read files into program -------------------- #
    print("Applying CTR Cipher (Encryption)......")
    print('\x1b[0;30;42m', "Key file:\t", '\x1b[0m', k)
    print('\x1b[0;30;42m', "Input File:\t", '\x1b[0m', i)
    print('\x1b[0;30;42m', "Output File:\t", '\x1b[0m', o)
    # -------------------- Process -------------------- #
    (keyStringHex, plainText) = readParameters(k, i)
    # my_ctr_cipher.setIV('00000060DB5672C97AA8F0B200000001')
    print('\x1b[5;35;44m', "IV is\t\t\t", '\x1b[0m', my_ctr_cipher.IV.hex())
    plaintext_bytes = plainText.encode('latin-1')
    padded_plaintext_bytes = my_ctr_cipher.pad(plaintext_bytes)
    pool = multiprocessing.Pool(processes=4)
    pool.map(encrypt_process, padded_plaintext_bytes)
    # -------------------- Process -------------------- #
    print("\n\n\n", '\x1b[0;31;44m', "\t\tEncryption is processing......\t\t", '\x1b[0m')
    raw_cipher_text_list = [None]*len(padded_plaintext_bytes)
    for k in range(len(padded_plaintext_bytes)):
        temp_item = output_queue.get()
        raw_cipher_text_list[temp_item[0]] = temp_item[1]
    final_cipher_str = str()
    for j in raw_cipher_text_list:
        final_cipher_str += j.decode('latin-1')
    with open(o, 'wb') as outputFile:
        # - add iv to the encrypted file -
        outputFile.write(my_ctr_cipher.IV)
        # - add ciphertext to the encrypted file -
        outputFile.write(final_cipher_str.encode('latin-1'))
    pool.close()
    pool.terminate()
    pool.join()
    print('\x1b[1;37;44m', "\t\t\tEncryption Finished!\t\t\t")


if __name__ == '__main__':
    main()

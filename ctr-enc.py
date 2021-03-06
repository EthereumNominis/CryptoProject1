import multiprocessing
import os
import click
from Cipher_CTR import CTRCipher

my_ctr_cipher = CTRCipher('776BEFF2851DB06F4C8A0542C8696F6C6A81AF1EEC96B4D37FC1D689E6C1C104', 16)
output_queue = multiprocessing.Queue()


def readParameters(k, i):
    keyStringHex = str()
    # plainText = str()
    with open(k, 'r') as keyFile:
        keyStringHex = keyFile.readline()
        print('\x1b[1;33;45m', "Successfully loaded key (Hex)\t", '\x1b[0m', repr(keyStringHex))
    with open(i, 'rb') as inputPlainTextFile:
        plainTextBytes = inputPlainTextFile.read()
        print('\x1b[1;33;45m', "Successfully loaded plain text file\t", '\x1b[0m')
    # print((keyStringHex, plainTextBytes))
    return (keyStringHex, plainTextBytes)


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
    # -------------------- Read files into program -------------------- #
    print("Applying CTR Cipher (Encryption)......")
    print('\x1b[0;30;42m', "Key file:\t", '\x1b[0m', k)
    print('\x1b[0;30;42m', "Input File:\t", '\x1b[0m', i)
    print('\x1b[0;30;42m', "Output File:\t", '\x1b[0m', o)
    # -------------------- Process -------------------- #
    (keyStringHex, plaintext_bytes) = readParameters(k, i)
    print('\x1b[5;35;44m', "IV is\t\t\t", '\x1b[0m', my_ctr_cipher.IV.hex())

    padded_plaintext_bytes = my_ctr_cipher.pad(plaintext_bytes)
    pool = multiprocessing.Pool(processes=4)
    pool.map(encrypt_process, padded_plaintext_bytes)
    # -------------------- Process -------------------- #
    print("\n\n\n", '\x1b[0;31;44m', "\t\tEncryption is processing......\t\t", '\x1b[0m')
    raw_cipher_text_list = [None]*len(padded_plaintext_bytes)
    for k in range(len(padded_plaintext_bytes)):
        temp_item = output_queue.get()
        raw_cipher_text_list[temp_item[0]] = temp_item[1]
    # print(raw_cipher_text_list)
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

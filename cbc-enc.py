import Cipher_CBC
import click


def readParameters(k, i):
    keyStringHex = str()
    plainText = str()
    with open(k, 'r') as keyFile:
        keyStringHex = keyFile.readline()
        print('\x1b[0;30;42m', "Successfully loaded key (Hex)\t", '\x1b[0m', repr(keyStringHex))
    with open(i, 'r') as inputPlainTextFile:
        plainText = inputPlainTextFile.read()
        print('\x1b[0;30;42m', "Successfully loaded plain text file\t", '\x1b[0m', repr(plainText))
    # print("\n\n\n",repr(plainText),"\n\n\n")
    return (keyStringHex, plainText)


@click.command()
@click.option('-k',
              help='\"Key file\"\n=>\trequired, specifies a file storing a valid AES key as a hex encoded string\n.')
@click.option('-i', help='\"Input file\"\n=>\trequired, specifies the path of the file that is being operated on\n.')
@click.option('-o',
              help='\"Output file\"\n=>\trequired, specifies the path of the file where the resulting output is stored\n.')
def main(k, i, o):
    bytes = 16
    # -------------------- Read files into program -------------------- #
    print("Applying CBC Cipher (Encryption)......")
    print("Key file:\t", k)
    print("Input File:\t", i)
    print("Output File:\t", o)
    (keyStringHex, plainText) = readParameters(k, i)
    # -------------------- Generate an instance from CBCCipher class -------------------- #
    my_cbc_cipher = Cipher_CBC.CBCCipher(
        keyStringHex, bytes)
    iv = my_cbc_cipher.IV
    print('\x1b[0;30;42m', "IV is\t\t\t", '\x1b[0m', iv.hex())
    # plaintext_bytes = bytes(plainText, 'latin-1')
    padded_plaintext_bytes = my_cbc_cipher.pad(plainText.encode('latin-1'))
    cipher_text_array = my_cbc_cipher.encrypt(padded_plaintext_bytes)
    print(padded_plaintext_bytes)
    # -------------------- Output Results -------------------- #
    print('\x1b[0;33;45m', "Cipher->\t\t", '\x1b[0m')
    with open(o, 'wb') as outputFile:
        # - Add IV (bytes) to the encrypted file -
        outputFile.write(iv)
        # - Add ciphertext to the encrypted file -
        for i in cipher_text_array:
            print('\x1b[3;31;47m', i.hex(), '\x1b[0m')
            print('\t\t\t|\t',i.decode('latin-1'))
            outputFile.write(i)
    print('\x1b[1;37;44m', "\t\t\tEncryption Finished!\t\t\t")
    # -------------------- END -------------------- #


if __name__ == '__main__':
    main()

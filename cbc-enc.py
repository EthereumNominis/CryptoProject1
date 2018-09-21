import Cipher_CBC
import click


def readParameters(k, i):
    keyStringHex = str()
    plainText = str()
    with open(k, 'r') as keyFile:
        keyStringHex = keyFile.readline()
        print('\x1b[0;30;42m', "Successfully loaded key (Hex)\t", '\x1b[0m', repr(keyStringHex))
    with open(i, 'r') as inputPlainTextFile:
        plainTextMatrix = inputPlainTextFile.readlines()
        plainText = ''.join(plainTextMatrix)
        print('\x1b[0;30;42m', "Successfully loaded plain text file\t", '\x1b[0m', repr(plainText))
    return (keyStringHex, plainText)


@click.command()
@click.option('-k',
              help='\"Key file\"\n=>\trequired, specifies a file storing a valid AES key as a hex encoded string\n.')
@click.option('-i', help='\"Input file\"\n=>\trequired, specifies the path of the file that is being operated on\n.')
@click.option('-o',
              help='\"Output file\"\n=>\trequired, specifies the path of the file where the resulting output is stored\n.')
def main(k, i, o):
    # $ python3 cbc-enc.py -k temp/keyFile1 -i dataFiles/plain1.txt -o myo
    # Applying CBC Cipher (Encryption).......
    # Key file:	 temp/keyFile1
    # Input File:	 dataFiles/plain1.txt
    # Output File:	 myo
    #  Successfully loaded key (Hex)	  'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'
    #  Successfully loaded plain text file	  "A good old man, sir; he will be talking: as they\nsay, when the age is in, the wit is out: God help\nus! it is a world to see. Well said, i' faith,\nneighbour Verges: well, God's a good man; an two men\nride of a horse, one must ride behind. An honest\nsoul, i' faith, sir; by my troth he is, as ever\nbroke bread; but God is to be worshipped; all men\nare not alike; alas, good neighbour!"
    #  IV is			  1bb17a68be19499aec7348ce4c5b1912
    #  Cipher->
    # ec6f03ec6eb7e5be71c28bf52e8a4f30
    # 95bda0bf59d17188825540d5571e1e2c
    # 25630947b559c8ce7878adcc317df2d9
    # ff4269424c2d5ce5aaf5b6132edde0b1
    # bce8d23fb8d497564e60020a9261cff5
    # da29c67443b7a7a8d09e8062d18804d2
    # 1bc16115ffcfd67b9bd3d1f436249e8b
    # 69cf4112eb11191e6b5bca0d8a954a0a
    # d0524244a05ff53c2b9cf02ed6611ad8
    # 1dc91cf8e52f9d49663c4651adea7e18
    # 27a343da76572adeb89d32e6fc7bcee7
    # c7d9a53987c0c27bf24e142905f03680
    # c943f7551e15aa324e8338de21f8a269
    # 80c162ca69f22df21996508ea4dd99a7
    # 28bfdf15b52410ccae00bff9508d977b
    # cd8c38336bf23c60be04748689c984e6
    # 312404f06fb7877341b6a9b5a8af62fe
    # 93ca1ce7b2ab87b8b3d8b10d240d9724
    # ca98662a21270aae6be9b37310e81c32
    # 7c2efb15583c25a91f00abb87a706d08
    # 3f94223cdacfc734516ac7dbee14178d
    # 241bb09bbbf072dd6d4d92e5562e6e95
    # 30cb9ba84fd225cb63a862083dc275f9
    # e91ea2cb91d7b06e18a2b5d82086022c
    #  			Encryption Finished!

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
    # -------------------- Output Results -------------------- #
    print('\x1b[0;33;45m', "Cipher->\t\t", '\x1b[0m')
    with open(o, 'wb') as outputFile:
        for i in cipher_text_array:
            print('\x1b[3;31;47m', i.hex(), '\x1b[0m')
            print('\t\t\t|\t',i.decode('latin-1'))
            outputFile.write(i)
    print('\x1b[1;37;44m', "\t\t\tEncryption Finished!\t\t\t")
    # -------------------- END -------------------- #


if __name__ == '__main__':
    main()

import Cipher_CBC
import click


def readParameters(k, i):
    keyStringHex = str()
    cipherArray = list()
    with open(k, 'r') as keyFile:
        keyStringHex = keyFile.readline()
        print('\x1b[0;30;42m', "Successfully loaded key (Hex)\t", '\x1b[0m', repr(keyStringHex))
    with open(i, 'rb') as inputPlainTextFile:
        cipherTextMatrix = inputPlainTextFile.read()
        # print(cipherTextMatrix[0:16].hex())
        num_of_cipher_groups = int(len(cipherTextMatrix) / 16)  # each group with 16 bytes
        for i in range(num_of_cipher_groups):
            cipherArray.append(cipherTextMatrix[i * 16:(i * 16 + 16)])
        print('\x1b[0;30;42m', "Successfully loaded cipher file (Binary)\t", '\x1b[0m', cipherArray)
    return (keyStringHex, tuple(cipherArray))


@click.command()
@click.option('-k',
              help='\"Key file\"\n=>\trequired, specifies a file storing a valid AES key as a hex encoded string\n.')
@click.option('-i', help='\"Input file\"\n=>\trequired, specifies the path of the file that is being operated on\n.')
@click.option('-o',
              help='\"Output file\"\n=>\trequired, specifies the path of the file where the resulting output is stored\n.')
def main(k, i, o):
    #     $ python3 cbc-dec.py -k temp/keyFile1 -i dataFiles/myy -o dataFiles/plain2byENC.txt
    # Applying CBC Cipher (Encryption)......
    #  Key file:	  temp/keyFile1
    #  Input File:	  dataFiles/myy
    #  Output File:	  dataFiles/plain2byENC.txt
    #  Successfully loaded key (Hex)	  'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'
    #  Successfully loaded cipher file (Binary)	  [b"\x1d\xd9\xb6Jn\xa2x\xa6E\x8d\x05'\x01Yhq", b'\x94J\x99@\xa2!\xd3\xf6t\xff\xf6\xbb\x8a\xcdB\xa8', b'\xb1rOg,\x8d+;\xc8-\xda\xce\xb6\x12e\x1b', b'S\xbb\x01\x8c}\x89\xea\xff)zc\xea\xf3\t5\xf8', b'\x81t4\xfaV\xb9\x8f\xc4\x01a\xeb\xfc\x0e\xa2\x15/', b'\x18f\xe7G\xe7\xd0\t#%\xbd\x15\x0c\xc9d\xdd(', b'W\xce|=SU\x0816\xef\x99 \x18e\xaf\x93', b'\x97t)[\xda\xd1wk\xc9\x0c\x88h\xec\xd1+j', b'\xe1\xa9\xd1\xef\xa1)\n\x17\x9714\xe7\xf4\xc7\x17\xb7', b'\t\xbe\xd0\xf6\xfa,\xbd\xcfm5:\xb3G\xd1\x94\x82', b'\xe5n\x08\n\xb4\xd7eYF\xac\xda\x05_gM\xb2', b']\x04l&FF\xe9\xcfd5\xe6=f\xcd\xa5L', b'\xe5$\x86\xd6\x9bw)7\xe9\xbcp\xf1\xc5\xc5\xa9\xc8', b'5\xf5D\xefxu\xda\xad\x15c\x963\x8aEY\xe1', b'\x9d\xfb/\xa0BO~\x9d\xf5\xb3\xc7yI\xfe\x1f\x05', b'\xbaPg\x05\x8c=y\xb8<\xbe\xc2\xf0\x14Z(\x8f', b'\x7f~;\xd0\xd3\xf5\x95\xe0Vg\xd7\x1dG\x8e2M', b'\xf8`P\x01\xb0q\xc5h\x03\\\xbd\x7fc\xac\xaa|', b'\x9aa\xb9\x9e\x00\xddt\xc0\xfa\xbc_[{\xdcM\\', b'~\xd7\x8c\xf8wpR\xf1<B\xbf\x91B\x9d\xbaB', b'\xbcA\xc0\x8f->v\xe9\xb9\x83o\xcb\x11\x7ff-', b'\x17\x92LG\xdb\x101/\xf4\x99b\xed\xae_\xder', b'\xc90\xb3\x95\x9c\xcc\x03\xd5N\xb9\xe0\xfc\x11vi\xf1', b'\xbf\x00[]\x16S\xde\x8e7~\x1dn\x00h\x06\xcc']
    #  Plain text is:
    # A good old man, sir; he will be talking: as they
    # say, when the age is in, the wit is out: God help
    # us! it is a world to see. Well said, i' faith,
    # neighbour Verges: well, God's a good man; an two men
    # ride of a horse, one must ride behind. An honest
    # soul, i' faith, sir; by my troth he is, as ever
    # broke bread; but God is to be worshipped; all men
    # are not alike; alas, good neighbour!
    #  			Decryption Finished!
    bytes = 16
    # -------------------- Read files into program -------------------- #
    print("Applying CBC Cipher (Encryption)......")
    print('\x1b[0;30;42m', "Key file:\t", '\x1b[0m', k)
    print('\x1b[0;30;42m', "Input File:\t", '\x1b[0m', i)
    print('\x1b[0;30;42m', "Output File:\t", '\x1b[0m', o)
    (keyStringHex, cipherArray) = readParameters(k, i)
    # -------------------- Generate an instance from CBCCipher class -------------------- #
    my_cbc_cipher = Cipher_CBC.CBCCipher(
        keyStringHex, bytes)
    my_cbc_cipher.setIV('66f5bdb70010a4c69e8f0227ff6ec318')
    # -------------------- Output Results -------------------- #
    decrypt_msg_array = my_cbc_cipher.decrypt(cipherArray)
    final_plain_text = my_cbc_cipher.unpadded(decrypt_msg_array)
    print('\x1b[0;30;42m', "Plain text is:\t", '\x1b[0m')
    print(final_plain_text)
    with open(o, 'w') as outputFile:
        outputFile.write(final_plain_text)
    print('\x1b[1;37;44m', "\t\t\tDecryption Finished!\t\t\t")
    # -------------------- END -------------------- #


if __name__ == '__main__':
    main()

import multiprocessing
import os
import click
from Cipher_CTR import CTRCipher

my_ctr_cipher = CTRCipher('776BEFF2851DB06F4C8A0542C8696F6C6A81AF1EEC96B4D37FC1D689E6C1C104', 16)
output_queue = multiprocessing.Queue()


def decryption_process(item):
    print('\x1b[1;37;44m', "\tPid is\t", '\x1b[0m', os.getpid())
    # print(item)
    plain_item = my_ctr_cipher.decrypt(item)
    output_queue.put((item[0], plain_item))


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
            cipherArray.append((i, cipherTextMatrix[i * 16:(i * 16 + 16)]))
        print('\x1b[0;30;42m', "Successfully loaded cipher file (Binary)\t", '\x1b[0m', cipherArray)
    return (keyStringHex, tuple(cipherArray))


@click.command()
@click.option('-k',
              help='\"Key file\"\n=>\trequired, specifies a file storing a valid AES key as a hex encoded string\n.')
@click.option('-i', help='\"Input file\"\n=>\trequired, specifies the path of the file that is being operated on\n.')
@click.option('-o',
              help='\"Output file\"\n=>\trequired, specifies the path of the file where the resulting output is stored\n.')
def main(k, i, o):
    # $ python3 ctr-dec.py -k temp/keyFile2 -i dataFiles/k2c -o dataFiles/nnnnnk2cplain.txt
    # Applying CTR Cipher (Encryption)......
    #  Key file:	  temp/keyFile2
    #  Input File:	  dataFiles/k2c
    #  Output File:	  dataFiles/nnnnnk2cplain.txt
    #  Successfully loaded key (Hex)	  '000102030405060708090a0b0c0d0e0ff0f1f2f3f4f5f6f7f8f9fafbfcfdfeff'
    #  Successfully loaded cipher file (Binary)	  [(0, b'\x06\x13\xd9\x15\xbc\x83N\xcaV\x03 \xda0\xe0\xbf\x87'), (1, b'\x00\xe8\x19>\\\x80\xd4s\x0f\xdd_\xb0=\xbe\x92j'), (2, b'&\x1ey\xf0\xabu\xf1\xb1)\r\xd1$\xe0\x85\xcb\x8b'), (3, b'\x85w\\\x15\x9aU\xd4\xcf\x9fOy\xc7\xfc\x1f\xc2}'), (4, b'\x1d\xff\xc5\x12\x03\x91\xb0T\xa6\x033\xa0D&\xd29'), (5, b'\x06\x8d|\xa6N\x0c\x9a\x18\xad\x7f\xbf\x93\n\xac\xf7\x15'), (6, b'\xb8\x9fqmF\xd8\x8b\xf9\xfc\xb2\x14\xe4\x81<\x94\x80'), (7, b'4f\xa3\xa2\n]\xbe\xd0\x02\xbe\xd1G0x\xe4]'), (8, b'\xa2uh \x90\x1e\xab\xc1S\xf0\xd2\xeb\xf4\xec\x0cs'), (9, b'y"\x95a\'0\x8e\x17e,\x1fE8\xd3\x98\t'), (10, b'#\xda\xd8lC:W\xe9\xde\x1b\x8a\x81#\xa8\x8f\x08'), (11, b'p\x0f\x85\xf7\x06\xef\x8d\x8f\x95]w\x94h\x92\x15n'), (12, b"#\xcbKU&\xd5\xfd\xd3\x8d\xd1'\x0c\xa7\xe7\xde}"), (13, b'%J\x95\x89?\xa0\xed\xf3R\xb0i)]\xee^Z'), (14, b'sh\xd7\xf1i\x87{"!M\xd2\xf9\x02caw'), (15, b'M\xd2\x8a\xc0\xad\x0b\xfd\x971\xc6u\xb6\xfeSH\xa5'), (16, b'\x13\x81\xad\xab\x88x<\xb7\x7f>\xe9\xcd\xd1\xbd17'), (17, b',\x0e":Iy\xcakH]\xc0\x14b-\xcbF'), (18, b'\xf6z9cMV\xe3\x9c\x86\xd4\x05\xe0:\x10.Y'), (19, b'\x93!\xd6gn\xf0\x13)d\xee.\xe0\xe8\xd0\xe5\xfb'), (20, b'f+-QS\x1d\x1ao\xb8)\x8de\xf2\x8a\x8c\x7f'), (21, b'\xd5whB1\xda\xa3\xd6\x82J\xdbf\x10\xb3\xac\xad'), (22, b'k%Lzf??M\x98\xac)\xc3\x80D\xe0='), (23, b'R<\xef\xbf\xfd\x94\x96]\xb7?k/"G\xd0\xc9')]
    #  IV is			  00000060db5672c97aa8f0b200000001
    #  	Pid is	  76971
    #  	Pid is	  76972
    #  	Pid is	  76973
    #  	Pid is	  76972
    #  	Pid is	  76973
    #  	Pid is	  76971
    #  	Pid is	  76971
    #  	Pid is	  76973
    #  	Pid is	  76973
    #  	Pid is	  76971
    #  	Pid is	  76972
    #  	Pid is	  76972
    #  	Pid is	  76971
    #  	Pid is	  76971
    #  	Pid is	  76973
    #  	Pid is	  76973
    #  	Pid is	  76972
    #  	Pid is	  76972
    #  	Pid is	  76974
    #  	Pid is	  76971
    #  	Pid is	  76971
    #  	Pid is	  76973
    #  	Pid is	  76973
    #  	Pid is	  76974
    #  			Decryption Finished!
    # -------------------- Read files into program -------------------- #
    print("Applying CTR Cipher (Encryption)......")
    print('\x1b[0;30;42m', "Key file:\t", '\x1b[0m', k)
    print('\x1b[0;30;42m', "Input File:\t", '\x1b[0m', i)
    print('\x1b[0;30;42m', "Output File:\t", '\x1b[0m', o)
    # -------------------- Read Parameters -------------------- #
    (keyStringHex, cipherArray) = readParameters(k, i)
    # -------------------- Reset IV from CBCCipher class -------------------- #
    my_ctr_cipher.setIV('00000060db5672c97aa8f0b200000001')
    print('\x1b[5;35;44m', "IV is\t\t\t", '\x1b[0m', my_ctr_cipher.IV.hex())
    # my_ctr_cipher.decrypt(cipherArray[0]).decode('latin-1')
    # my_ctr_cipher.decrypt(cipherArray[1]).decode('latin-1')
    pool = multiprocessing.Pool(processes=4)
    pool.map(decryption_process, cipherArray)
    plain_text_list = [None] * len(cipherArray)
    for i in range(len(cipherArray)):
        temp_item = output_queue.get()
        plain_text_list[temp_item[0]] = temp_item[1].decode('latin-1')
    raw_plain_text = "".join(plain_text_list)
    # -------------------- write to output -------------------- #
    with open(o, 'w') as outputFile:
        outputFile.write(raw_plain_text)
    print('\x1b[1;37;44m', "\t\t\tDecryption Finished!\t\t\t")
    # -------------------- END -------------------- #


if __name__ == '__main__':
    main()

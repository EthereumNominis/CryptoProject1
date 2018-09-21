import click
from MAC_CBC import mac_cbc_cipher

@click.command()
@click.option('-k',
              help='\"Key file\"\n=>\trequired, specifies a file storing a valid AES key as a hex encoded string\n.')
@click.option('-m', help='\"Input file\"\n=>\trequired, specifies the path of the message file that is being operated on\n.')
@click.option('-t',
              help='\"Tag file\"\n=>\trequired, specifies the path of the tag file, output for cbcmac-tag\n.')
def main(k, m, t):
    # - Read parameters -
    print("Key file:\t", k)
    print("Message file:\t", m)
    print("Tag file:\t", t)


    # - Read key content -
    with open(k, 'r') as keyFile:
        keyStringHex = keyFile.readline()
        print('\x1b[0;30;42m', "Successfully loaded key (Hex)\t", '\x1b[0m', repr(keyStringHex))


    # - read message -
    with open(m, 'rb') as inputMessageFile:
        messageString = inputMessageFile.read()
        print('\x1b[1;33;45m', "Successfully loaded plain text file\t", '\x1b[0m')
        # print(messageString.decode('latin-1'))

    my_cbctag = mac_cbc_cipher(keyStringHex, 16)
    my_cbctag.tag(messageString.decode('latin-1'))

    if my_cbctag != None:
        with open(t, 'wb') as tagFile:
            tagFile.write(my_cbctag.TAG)
            print('\x1b[1;33;45m', "Successfully generated tag for the message\t", '\x1b[0m', my_cbctag.TAG.hex())
    else:
        print('\x1b[1;33;45m', "Failed generating tag for the message\t", '\x1b[0m')
    # - END -






if __name__ == '__main__':
    main()


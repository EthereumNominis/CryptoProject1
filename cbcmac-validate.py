import click
from MAC_CBC import mac_cbc_cipher


@click.command()
@click.option('-k',
              help='\"Key file\"\n=>\trequired, specifies a file storing a valid AES key as a hex encoded string\n.')
@click.option('-m',
              help='\"Input file\"\n=>\trequired, specifies the path of the message file that is being operated on\n.')
@click.option('-t',
              help='\"Tag file\"\n=>\trequired, specifies the path of the tag file, input for cbcmac-validate\n.')
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
        print('\x1b[1;33;45m', "Successfully loaded message file\t", '\x1b[0m')

    # - Read tag -
    with open(t, 'rb') as tagFile:
        tagBytes = tagFile.read()
        print('\x1b[0;30;42m', "Successfully loaded tag (Hex)\t", '\x1b[0m', tagBytes.hex())

    # - Generate the new tag and check whether the old tag is identical to new one -
    my_cbctag = mac_cbc_cipher(keyStringHex, 16)
    my_cbctag.tag(messageString.decode('latin-1'))

    if (my_cbctag.TAG != None) and (my_cbctag.TAG == tagBytes):
        print("\n\n\n\t\t\t", "-" * 40, "\n\n")
        print("\t\t\t", '\x1b[2;30;47m', "TRUR tag for the input message!", '\x1b[0m')
        print("\n\n\t\t\t", "-" * 40)
    else:
        print("\n\n\n\t\t\t", "-" * 40, "\n\n")
        print("\t\t\t", '\x1b[2;30;41m', "FALSE tag for the input message!", '\x1b[0m')
        print("\n\n\t\t\t", "-" * 40)
    # - END -


if __name__ == '__main__':
    main()

import string

selection = input("C or U? ")

if selection == "C" :
        
    plain_text = input("Text: ")

    shift = input("Shift: ")
    shift = int(shift) % 26

    # THE VERSION 1 OF CryX ONLY SUPPORTS LOWERCASE CHARACTERS
    alphabet = string.ascii_lowercase

    # ABCDEFGHIJKLMNOPQRSTUVWXYZ

    shifted = alphabet[shift:] + alphabet[:shift]

    # HIJKLMNOPQRSTUVWXYZ + ABCDEFG = HIJKLMNOPQRSTUVWXYZABCDEFG

    table = str.maketrans(alphabet, shifted)

    encrypted = plain_text.translate(table) 

    print(encrypted)

if selection == "U" :

    encrypted_text = input("Encrypted Text: ")

    shift = input("Shift: ")
    shift = 26 - int(shift)
    shift = shift % 26

    alphabet = string.ascii_lowercase
    shifted = alphabet[shift:] + alphabet[:shift]

    table = str.maketrans(alphabet, shifted)

    uncrypted = encrypted_text.translate(table) 

    print(uncrypted)
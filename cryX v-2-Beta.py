import string

def cryx(text, shift, alphabets):

    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]

    shifted_alphabets = tuple(map(shift_alphabet, alphabets))

    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabet ,final_shifted_alphabet)
    return text.translate(table)

selection = input("C or U ? ")

if selection == "C":
    plain_text = input("Text: ")
    shift = input("Shift: ")
    shift = int(shift) % 26

    print(cryx(plain_text, shift, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))

if selection == "U":
    encrypted_text = input("Encrypted Text: ")
    shift = input("Shift: ")
    shift = 26 - int(shift)
    shift = shift % 26

    print(cryx(encrypted_text, shift, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))
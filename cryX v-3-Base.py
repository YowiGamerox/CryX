import string
import os

#* The function that crypt the input text
def cryx(text, shift, alphabets):
    # The function that shifts the alphabet and returns the alphabet shifted
    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]
    # Tuples the shifted alphabets
    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    # Joins all the alphabets in a (single) final alphabet, then shifts the final alphabet
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    # Translates the final alphabet to the final shifted alphabet, then returns the text translated
    table = str.maketrans(final_alphabet ,final_shifted_alphabet)
    return text.translate(table)

#* Asks you if you want to Crypt or Uncrypt
selection = input("C or U ? ")

#* If your answer was Crypt
if selection == "C":
    # Inputs the plain text
    plain_text = input("Text: ")
    # Inputs the shift and turns it an integer
    shift = int(input("Shift: "))
    
    #* If shift is bigger than 1
    if (1 <= shift) :
        # If shift is bigger than 9
        if (shift > 9) :
            # Modules shift
            shift = shift % 26
            # If the result of the module is 0
            if (shift == 0) :
                shift = shift + 4
        # Crypt it and print the result
        print(cryx(plain_text, shift, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.digits]))
    #* If shift is lower than 1
    elif (shift < 1) :
        print(">> The shift number can't be 0 or lower") 
    
#* If your answer was Uncrypt
if selection == "U":
    # Inputs the encrypted text
    encrypted_text = input("Encrypted Text: ")
    # Inputs the shift and turns it an integer, then rests the number of alphabet characters minus shift 
    shift = int(input("Shift: "))
    shift = 26 - shift
    

    # If shift is bigger than 9
    if (shift > 9) :
        # Modules shift
        shift = shift % 26
        # If the result of the module is 0
        if (shift == 0) :
            shift = shift + 4
    # Uncrypt it and print the result
    print(cryx(encrypted_text, shift, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.digits]))
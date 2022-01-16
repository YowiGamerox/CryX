import string
import os
import shutil

#& My Functions
#* The function that encrypt the input text
def cryx(text, shift, alphabets) :
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

#* The function that creates the cryx files 
def cryxFile(filename, mode, cryxText, shift) :
    os.chdir(cryxFolder)
    f = open(filename, mode)
    f.write(cryxText + '\n' + str(shift))
    f.close()

#& EncryptFolder path
#* Get current directory
# Gets the current working directory in a variable
currentDirectory = os.getcwd()
#* EncryptFolder Creation
# Assumes the encryptFolder path
cryxFolder = currentDirectory + "\cryxFolder"
# Checks if the given path exists
cryxFolder_Exist = os.path.exists(cryxFolder)


#& Encrypt or Decrypt selection
#* Asks you if you want to enrypt or decrypt
cryxSelection = input("Do you wanna Encrypt or Decrypt? (E or D) : ")

#& Encrypt way
#* If your answer was Encrypt
if cryxSelection == "E":
    #^ The Inputs
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
        # Encrypts it and prints the result
        encryptedText = cryx(plain_text, shift, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.digits])
        print(">> Your encrypted text is: " + encryptedText)
    #* If shift is lower than 1
    elif (shift < 1) :
        print("ERROR: The shift number can't be 0 or lower") 

    #& Creating the encrypt file
    #* Encrypted file creation
    if cryxFolder_Exist == True :
        cryxFile("encrypted.txt", "w+", encryptedText, shift)
        print('>> The "encrypted.txt" file has been created')
    
    # If the folder doesn't exist
    if cryxFolder_Exist == False :
        # Creates the cryxFolder and checks if it exist
        os.makedirs(cryxFolder)
        cryxFolder_Exist = True
        # If it exist
        if cryxFolder_Exist == True :
            print(">> The cryxFolder has been created")
            cryxFile("encrypted.txt", "w+", encryptedText, shift)
            print('>> The "encrypted.txt" file has been created')

#& Decrypt way
#* If your answer was Decrypt
if cryxSelection == "D":
    #^ The Inputs
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
    # Decrypt it and print the result
    decryptedText = cryx(encrypted_text, shift, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.digits])
    print(">> Your decrypted text is: " + decryptedText)

    #& Creating the decrypt file
    #* Decrypted file creation
    if cryxFolder_Exist == True :
        cryxFile("decrypted.txt", "w+", decryptedText, shift)
        print('>> The "decrypted.txt" file has been created')
    
    # If the folder doesn't exist
    if cryxFolder_Exist == False :
        # Creates the cryptFolder and checks if it exist
        os.makedirs(cryxFolder)
        cryxFolder_Exist = True
        # If it exist
        if cryxFolder_Exist == True :
            print(">> The cryxFolder has been created")
            cryxFile("decrypted.txt", "w+", decryptedText)
            print('>> The "decrypted.txt" file has been created')    


#& Email way
from email.message import EmailMessage
message = EmailMessage()

#& Email Selection
emailSelection = input(">> Should I send it by email? (Y or N) : ")

#* If Yes
if (emailSelection == "Y") :
    sender = input(">> Write the email sender (your-name@gmail.com) : ")
    recipient = input(">> Write the email recipient (example@example.com) : ")

    message['From'] = sender
    message['To'] = recipient

    message['Subject'] = input(">> Write the email subject (Title) : " )
    body = input(">> Write the email body : " )
    message.set_content(body)
    print("\n >> This is how your email message looks: " + '\n'  + str(message))

    import mimetypes
    mime_type, _ = mimetypes.guess_type('encrypted.txt')
    print(mime_type)

    mime_type, mime_subtype = mime_type.split('/')

    with open("encrypted.txt", "rb") as file :
        message.add_attachment(file.read(),
        maintype = mime_type,
        subtype = mime_subtype,
        filename = "encrypted.txt")

    #& SMTP Server (Simple Mail Transfer Protocol)
    import smtplib
    import getpass
    mail_server = smtplib.SMTP_SSL("smtp.gmail.com")
    print("NOTE: To work you have to enable less secure app from gmail by using this link https://myaccount.google.com/lesssecureapps")
    userPassword = getpass.getpass()
    mail_server.login(sender, userPassword)
    mail_server.set_debuglevel(1)
    mail_server.send_message(message)
    mail_server.quit()
    print(">> The message has been sent!")
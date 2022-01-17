import string
import os
import shutil

def cryx(text, shift, alphabets) :    
    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]
    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabet ,final_shifted_alphabet)
    return text.translate(table)

def cryxFile(filename, mode, cryxText, shift) :
    os.chdir(cryxFolder)
    f = open(filename, mode)
    f.write(cryxText + '\n' + str(shift))
    f.close()

currentDirectory = os.getcwd()
cryxFolder = currentDirectory + "\cryxFolder"
cryxFolder_Exist = os.path.exists(cryxFolder)

scan_or_send_Selection = input("Do you want to Scan or Create a file? (S or C) : ")

if (scan_or_send_Selection == "S") :
    os.chdir(cryxFolder)
    f = open("encrypted.txt", "r")
    contents = f.readlines()
    encrypted_text = contents[0]
    shift = 26 - int(contents[1])
    shift = shift % 26
    if (shift == 0) :
            shift = shift + 4
    decryptedText = cryx(encrypted_text, shift, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.digits])
    print(">> Your decrypted text is: " + decryptedText)


elif (scan_or_send_Selection == "C") :
    cryxSelection = input("Do you wanna Encrypt or Decrypt? (E or D) : ")

    if cryxSelection == "E":        
        plain_text = input("Text: ")
        shift = int(input("Shift: "))
        if (1 <= shift) :
            if (shift > 9) :
                shift = shift % 26
                if (shift == 0) :
                    shift = shift + 4
            encryptedText = cryx(plain_text, shift, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.digits])
            print(">> Your encrypted text is: " + encryptedText)
        elif (shift < 1) :
            print("ERROR: The shift number can't be 0 or lower") 

        if cryxFolder_Exist == True :
            cryxFile("encrypted.txt", "w+", encryptedText, shift)
            print('>> The "encrypted.txt" file has been created')
                
        if cryxFolder_Exist == False :    
            os.makedirs(cryxFolder)
            cryxFolder_Exist = True
            if cryxFolder_Exist == True :
                print(">> The cryxFolder has been created")
                cryxFile("encrypted.txt", "w+", encryptedText, shift)
                print('>> The "encrypted.txt" file has been created')

    if cryxSelection == "D":        
        encrypted_text = input("Encrypted Text: ")
        shift = int(input("Shift: "))
        shift = 26 - shift
        
        if (shift > 9) :            
            shift = shift % 26
            if (shift == 0) :
                shift = shift + 4
        decryptedText = cryx(encrypted_text, shift, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.digits])
        print(">> Your decrypted text is: " + decryptedText)

        if cryxFolder_Exist == True :
            cryxFile("decrypted.txt", "w+", decryptedText, shift)
            print('>> The "decrypted.txt" file has been created')        

        if cryxFolder_Exist == False :
            os.makedirs(cryxFolder)
            cryxFolder_Exist = True
            if cryxFolder_Exist == True :
                print(">> The cryxFolder has been created")
                cryxFile("decrypted.txt", "w+", decryptedText)
                print('>> The "decrypted.txt" file has been created')    

    
    from email.message import EmailMessage
    message = EmailMessage()
    
    emailSelection = input(">> Should I send it by email? (Y or N) : ")
    
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

        shutil.rmtree(cryxFolder)
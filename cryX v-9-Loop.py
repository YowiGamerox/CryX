import string
import os
import shutil

currentDirectory = os.getcwd()
cryxFolder = currentDirectory + "\cryxFolder"
cryxFolder_Exist = os.path.exists(cryxFolder)
encryptFile = cryxFolder + "\cryX-encrypted.txt"
encryptFile_Exist = os.path.exists(encryptFile)
        
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

def get_download_path():
    if os.name == "nt":
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser("~"), "downloads")


downloadsFolder = get_download_path()
file_in_downloadsFolder = downloadsFolder + "\cryX-encrypted.txt"
file_in_downloadsFolder_Exist = os.path.exists(file_in_downloadsFolder)

active = True
while active == True:

    downloadsMode = False

    mainSelection = input("<< (～￣▽￣)～ What do you wanna do? (C/S/D) : ")

    if (mainSelection == "S") :
        print(">> ㄟ( ▔, ▔ )ㄏ Scan Mode selected")

        if (encryptFile_Exist == False) :
            print('>> The "cryX-encrypted.txt" file', "doesn't exist at", cryxFolder)
            if (cryxFolder_Exist == False):
                print(">> (￣、￣) The folder doesn't even exist")
            print(">> (￣_,￣ ) HeHe I'm searching for it in your Downloads folder")

            if(file_in_downloadsFolder_Exist == True):
                encryptFile_Exist = True
                downloadsMode = True
            else :
                print(">> (┬┬n┬┬) There's no file")

        if (encryptFile_Exist == True) :
            if(downloadsMode == False):
                os.chdir(cryxFolder)
            if(downloadsMode == True):
                os.chdir(downloadsFolder)
            f = open("cryX-encrypted.txt", "r")
            contents = f.readlines()
            encrypted_text = contents[0]
            shift = 26 - int(contents[1])
            shift = shift % 26
            if (shift == 0) :
                    shift = shift + 4
            decryptedText = cryx(encrypted_text, shift, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.digits])
            print(">>（￣︶￣）Your decrypted text is:", decryptedText)
            
    elif (mainSelection == "C") :
        cryxSelection = input("<< Fella, do you wanna Encrypt or Decrypt? (E/D) : ")

        if cryxSelection == "E":        
            plain_text = input("Text: ")
            shift = int(input("Shift: "))
            if (1 <= shift) :
                if (shift > 9) :
                    shift = shift % 26
                    if (shift == 0) :
                        shift = shift + 4
                encryptedText = cryx(plain_text, shift, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.digits])
                print(">>（￣︶￣）Your encrypted text is:", encryptedText)
            elif (shift < 1) :
                print("ERROR: The shift number can't be 0 or lower （︶^︶）") 

            if cryxFolder_Exist == True :
                cryxFile("cryX-encrypted.txt", "w+", encryptedText, shift)
                print('// The file "cryX-encrypted.txt" has been created in', currentDirectory)
                    
            if cryxFolder_Exist == False :    
                os.makedirs(cryxFolder)
                cryxFolder_Exist = True
                if cryxFolder_Exist == True :
                    print('// The folder "cryxFolder" has been created')
                    cryxFile("cryX-encrypted.txt", "w+", encryptedText, shift)
                    print('// The file "cryX-encrypted.txt" has been created')

        if cryxSelection == "D":        
            encrypted_text = input("<< Encrypted Text: ")
            shift = int(input("<< Shift: "))
            shift = 26 - shift
            
            if (shift > 9) :            
                shift = shift % 26
                if (shift == 0) :
                    shift = shift + 4
            decryptedText = cryx(encrypted_text, shift, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.digits])
            print(">>（￣︶￣）Your decrypted text is: " + decryptedText)

            if cryxFolder_Exist == True :
                cryxFile("decrypted.txt", "w+", decryptedText, shift)
                print('// The file "decrypted.txt" has been created')        

            if cryxFolder_Exist == False :
                os.makedirs(cryxFolder)
                cryxFolder_Exist = True
                if cryxFolder_Exist == True :
                    print('// The folder "cryxFolder" has been created')
                    cryxFile("decrypted.txt", "w+", decryptedText)
                    print('// The file "decrypted.txt" has been created')    

        
        from email.message import EmailMessage
        message = EmailMessage()
        
        emailSelection = input("<< (✿◡‿◡) Should I send it by email for you? (Y or N) : ")
        
        if (emailSelection == "Y") :
            sender = input("<< Write the email sender (your-name@gmail.com) : ")
            recipient = input("<< Write the email recipient (example@example.com) : ")

            message['From'] = sender
            message['To'] = recipient

            message['Subject'] = input("<< Write the email subject (Title) : " )
            body = input(">> Write the email body : " )
            message.set_content(body)
            ask_preview = input("<< (◔◡◔) Do you wanna see a preview of your email before sending it? (Y/N)")
            if (ask_preview == "Y"):
                print("\n >> This is how your email message looks: " + '\n'  + str(message))

            import mimetypes
            mime_type, _ = mimetypes.guess_type('cryX-encrypted.txt')
            mime_type, mime_subtype = mime_type.split('/')

            with open("cryX-encrypted.txt", "rb") as file :
                message.add_attachment(file.read(),
                maintype = mime_type,
                subtype = mime_subtype,
                filename = "cryX-encrypted.txt")

            
            import smtplib
            import getpass
            mail_server = smtplib.SMTP_SSL("smtp.gmail.com")
            print("!NOTE: To work you have to enable less secure app from gmail by using this link https://myaccount.google.com/lesssecureapps")
            userPassword = getpass.getpass()
            mail_server.login(sender, userPassword)
            mail_server.set_debuglevel(1)
            mail_server.send_message(message)
            mail_server.quit()
            print(">> The message has been sent! ╰(*°▽°*)╯")

            shutil.rmtree(cryxFolder)
            print(">> I deleted the cryxFolder for you ( •̀ ω •́ )✧")

        if (emailSelection == "N") :
            print(">> (≧∇≦)ﾉ Okay, have a nice day!")

    if (mainSelection == "D") :
        shutil.rmtree(cryxFolder)
        print(">> I deleted the cryxFolder for you ( •̀ ω •́ )✧")
    
    if (mainSelection == "Exit"):
        print(">> Bye~")
        active = False
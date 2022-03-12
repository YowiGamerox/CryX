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


currentDirectory = os.getcwd()
cryxFolder = currentDirectory + "\cryxFolder"
cryxFolder_Exist = os.path.exists(cryxFolder)
encryptFile = cryxFolder + "\cryX-encrypted.txt"
encryptFile_Exist = os.path.exists(encryptFile)
downloadsFolder = get_download_path()
file_in_downloadsFolder = downloadsFolder + "\cryX-encrypted.txt"
file_in_downloadsFolder_Exist = os.path.exists(file_in_downloadsFolder)
downloadsMode = False

mainSelection = input("<< (～￣▽￣)～ ¿Qué quieres hacer? (C/S/D) : ")

if (mainSelection == "S") :
    print(">> ㄟ( ▔, ▔ )ㄏ Modo Escaneo seleccionado")

    if (encryptFile_Exist == False) :
        print('>> El archivo "cryX-encrypted.txt"', "no existe en", cryxFolder)
        if (cryxFolder_Exist == False):
            print(">> (￣、￣) La carpeta ni siquiera existe")
        print(">> (￣_,￣ ) HeHe Como alternativa, lo estoy buscando en tu carpeta de Descargas")

        if(file_in_downloadsFolder_Exist == True):
            encryptFile_Exist = True
            downloadsMode = True
        else :
            print(">> (┬┬n┬┬) No hay ningún archivo")

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
        print(">>（￣︶￣）Tu texto desencriptado es:", decryptedText)
        input()
        
elif (mainSelection == "C") :
    cryxSelection = input("<< Amigo, ¿quieres Encriptar o Desencriptar? (E/D) : ")

    if cryxSelection == "E":        
        plain_text = input("Texto: ")
        shift = int(input("Shift: "))
        if (1 <= shift) :
            if (shift > 9) :
                shift = shift % 26
                if (shift == 0) :
                    shift = shift + 4
            encryptedText = cryx(plain_text, shift, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.digits])
            print(">>（￣︶￣）Tu texto encriptado es:", encryptedText)
        elif (shift < 1) :
            print("ERROR: El numero de cambio (shift) no puede ser 0 o menor （︶^︶）") 

        if cryxFolder_Exist == True :
            cryxFile("cryX-encrypted.txt", "w+", encryptedText, shift)
            print('// El archivo "cryX-encrypted.txt" ha sido creado en', currentDirectory)
                
        if cryxFolder_Exist == False :    
            os.makedirs(cryxFolder)
            cryxFolder_Exist = True
            if cryxFolder_Exist == True :
                print('// La carpeta "cryxFolder" ha sido creada')
                cryxFile("cryX-encrypted.txt", "w+", encryptedText, shift)
                print('// El archivo "cryX-encrypted.txt" ha sido creado')

    if cryxSelection == "D":        
        encrypted_text = input("<< Texto Encriptado: ")
        shift = int(input("<< Shift: "))
        shift = 26 - shift
        
        if (shift > 9) :            
            shift = shift % 26
            if (shift == 0) :
                shift = shift + 4
        decryptedText = cryx(encrypted_text, shift, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.digits])
        print(">>（￣︶￣）Tu texto desencriptado es: " + decryptedText)

        if cryxFolder_Exist == True :
            cryxFile("decrypted.txt", "w+", decryptedText, shift)
            print('// El archivo "decrypted.txt" ha sido creado')        

        if cryxFolder_Exist == False :
            os.makedirs(cryxFolder)
            cryxFolder_Exist = True
            if cryxFolder_Exist == True :
                print('// La carpeta "cryxFolder" ha sido creada')
                cryxFile("decrypted.txt", "w+", decryptedText)
                print('// El archivo "decrypted.txt" ha sido creado')    

    
    from email.message import EmailMessage
    message = EmailMessage()
    
    emailSelection = input("<< (✿◡‿◡) ¿Debería enviarlo por email por tí? (Y or N) : ")
    
    if (emailSelection == "Y") :
        sender = input("<< Introduce el email del emisor (your-name@gmail.com) : ")
        recipient = input("<< Introduce el email del receptor (example@example.com) : ")

        message['From'] = sender
        message['To'] = recipient

        message['Subject'] = input("<< Introduce el título del email (Título) : " )
        body = input(">> Introduce el cuerpo del email : " )
        message.set_content(body)
        ask_preview = input("<< (◔◡◔) ¿Quieres ver una vista previa de tu email antes de enviarlo? (Y/N)")
        if (ask_preview == "Y"):
            print("\n >> Así es como se ve tu email: " + '\n'  + str(message))

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
        print("!NOTE: Para que funcione tienes que activar la funcion Less Secure App de gmail usando este enlace https://myaccount.google.com/lesssecureapps")
        userPassword = getpass.getpass()
        mail_server.login(sender, userPassword)
        mail_server.set_debuglevel(1)
        mail_server.send_message(message)
        mail_server.quit()
        print(">> ¡Se ha enviado el mensaje! ╰(*°▽°*)╯")

        shutil.rmtree(cryxFolder)
        print(">> He borrado la carpeta cryxFolder por tí ( •̀ ω •́ )✧")

    if (emailSelection == "N") :
        print(">> (≧∇≦)ﾉ Okay, ¡que tengas un buen día!")
        input()

if (mainSelection == "D") :
    shutil.rmtree(cryxFolder)
    print(">> He borrado la carpeta cryxFolder por tí ( •̀ ω •́ )✧")
    input()
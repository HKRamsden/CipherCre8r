#### Credits:
#### Hannah Ramsden: UI design, Logic Design, AES Encryption, CFB Encryption
#### Jaren Taylor: CTR Encryption
#### Jonathan Legro: CBC Encryption
#### Alec Ryden: --

## Imports ##
from tkinter import *
import base32hex
import hashlib
import string
import random
from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

# Saving Color Codes #
eerieBlack = "#1D1E18"
feldgrau = "#445745"
resedaGreen = "#58735B"
mint = "#6B8F71"

# Creating Root Window #
root = Tk()
root.title("CipherCr8r")
root.geometry('500x500')
root.configure(bg=eerieBlack)

### VARIABLES HERE ###
enterPlaintext = StringVar()


### ENCRYPTION METHODS HERE ###

## AES Encryption ##
def aesFunc(plaintext):
    aesplaintext = plaintext.encode('utf-8')
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(aesplaintext)
    nonce = cipher.nonce
    stored_text = nonce + tag + ciphertext

    #print(stored_text)

    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    # print(data)
    decodedStr = str(data, encoding = 'utf-8')
    # print(decodedStr)
    
    encMessage.config(text = "Encrypted Message: 0x" + stored_text.hex())
    decMessage.config(text = "Decrypted Message: " + decodedStr)

## DES Encryption ##
# not complete, still developing
# now in testing 
def desFunc(plaintext):
    plaintext += '\x00' * (8 - len(plaintext) % 8)
    desplaintext = plaintext.encode('utf-8')
    password = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 8))
    salt = get_random_bytes(8).hex()
    key = password + salt
    encodedKey = key.encode('utf-8')
    m = hashlib.md5(encodedKey)
    key = m.digest()
    (dk, iv) = (key[:8], key[8:])
    cipher = DES.new(dk, DES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(desplaintext)

    decryptcipher = DES.new(dk, DES.MODE_CBC, iv)
    data = decryptcipher.decrypt(ciphertext)
    
    # print(data)
    decodedStr = str(data, encoding = 'utf-8')
    # print(decodedStr)
    
    encMessage.config(text = "Encrypted Message: 0x" + ciphertext.hex())
    decMessage.config(text = "Decrypted Message: " + decodedStr)


## CBC Encryption
def cbcFunc(plaintext):
    cbcplaintext = plaintext.encode('utf-8')
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(cbcplaintext, AES.block_size))
    iv = cipher.iv

    decryptcipher = AES.new(key, AES.MODE_CBC, iv)
    data = unpad(decryptcipher.decrypt(ciphertext), AES.block_size)
    
    # print(data)
    decodedStr = str(data, encoding = 'utf-8')
    # print(decodedStr)
    
    encMessage.config(text = "Encrypted Message: 0x" + ciphertext.hex())
    decMessage.config(text = "Decrypted Message: " + decodedStr)


## CFB Encryption ##
def cfbFunc(plaintext):
    cfbplaintext = plaintext.encode('utf-8')
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CFB)
    ciphertext = cipher.encrypt(cfbplaintext)
    iv = cipher.iv

    decryptcipher = AES.new(key, AES.MODE_CFB, iv=iv)
    data = decryptcipher.decrypt(ciphertext)
    
    # print(data)
    decodedStr = str(data, encoding = 'utf-8')
    # print(decodedStr)
    
    encMessage.config(text = "Encrypted Message: 0x" + ciphertext.hex())
    decMessage.config(text = "Decrypted Message: " + decodedStr)

    
## CTR Encryption ##
def ctrFunc(plaintext):
    ctrplaintext = plaintext.encode('utf-8')
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CTR)
    ciphertext= cipher.encrypt(ctrplaintext)

    #print(stored_text)

    decryptcipher = AES.new(key, AES.MODE_CTR, nonce = cipher.nonce)
    data = decryptcipher.decrypt(ciphertext)
    # print(data)
    decodedStr = str(data, encoding = 'utf-8')
    # print(decodedStr)
    
    encMessage.config(text = "Encrypted Message: 0x" + ciphertext.hex())
    decMessage.config(text = "Decrypted Message: " + decodedStr)


### APP COMMANDS HERE ###

# Encrypt Plaintext Using Chosen Mode #
def plaintextEncryption():
    plainText = enterPlaintext.get()
 
    for i in listbox.curselection():
        mode = listbox.get(i)
        match mode:
            case "AES":
                aesFunc(plainText)
            case "DES":
                desFunc(plainText)
            case "CBC":
                cbcFunc(plainText)
            case "CFB":
                cfbFunc(plainText)
            case "CTR":
                ctrFunc(plainText)

### UI DESIGN HERE ###

## List Box ##
listboxBorder = Frame(root,
                      highlightbackground = resedaGreen,
                      highlightcolor = mint,
                      bg = resedaGreen, 
                      highlightthickness= 5, 
                      bd = 0)
listboxBorder.place(relx = 0.01, rely = 0.01)
listbox = Listbox(listboxBorder,
                  font = "Arial 15",
                  fg = eerieBlack,
                  bg = feldgrau,
                  highlightcolor = mint,
                  width = 10,
                  height = 5)
listbox.insert(1, "AES")
listbox.insert(2, "DES")
listbox.insert(3, "CBC")
listbox.insert(4, "CFB")
listbox.insert(5, "CTR")
listbox.pack()

## Get Encryption Selection
def getEncryptionSelection():
    for i in listbox.curselection():
        print(listbox.get(i))
        mode = listbox.get(i)
        messageVar.config(text = "Current Mode: " + mode)

## Select Option Button ##
selectOptBorder = Frame(root,
                        highlightbackground = resedaGreen,
                        highlightcolor = mint,
                        bg = resedaGreen,
                        highlightthickness = 5,
                        bd = 0)
selectOptBorder.place(relx = 0.27, rely = 0.01)
selectOptButton = Button(selectOptBorder, 
                         text = "Select Mode",
                         font = "Arial 15",
                         fg = eerieBlack,
                         bg = feldgrau,
                         highlightcolor = mint,
                         width = 10, 
                         height = 2,
                         command = getEncryptionSelection)
selectOptButton.pack()

## Text Entry for Plaintext ##
plaintextEnterBorder = Frame(root, 
                             highlightbackground = resedaGreen,
                             highlightcolor = mint,
                             bg = resedaGreen, 
                             highlightthickness = 5,
                             bd = 0)
plaintextEnterBorder.place(relx = 0.27, rely = 0.18) 
plaintextEntry = Entry(plaintextEnterBorder, 
                       textvariable = enterPlaintext,
                       font = "Arial 20", 
                       fg = eerieBlack,
                       bg= feldgrau,
                       width = 21)

# Temporary Text #
def tempPlainText(e):
    plaintextEntry.delete(0, "end") 

plaintextEntry.insert(0, "Enter Plaintext Here")
plaintextEntry.bind("<FocusIn>", tempPlainText)
plaintextEntry.pack()

    
## Text Box for Encryption Choice ## 
currentChoiceBorder = Frame(root,
                            highlightbackground = resedaGreen,
                            highlightcolor = mint,
                            bg = resedaGreen,
                            highlightthickness = 5,
                            bd = 0)
currentChoiceBorder.place(relx = 0.55, rely = 0.01)
messageVar = Button(currentChoiceBorder, 
                     text = "Current Mode: ",
                     font = "Arial 15",
                     fg = eerieBlack,
                     bg = feldgrau,
                     highlightcolor= mint,
                     width = 15,
                     height = 2)
messageVar.pack()

## Encryption Button ##
encryptButtonBorder = Frame(root,
                            highlightbackground = resedaGreen,
                            highlightcolor = mint,
                            bg = resedaGreen,
                            highlightthickness= 5,
                            bd = 0)
encryptButtonBorder.place(relx = 0.01, rely = 0.3)
encryptButton = Button(encryptButtonBorder,
                         text = "Encrypt",
                         font = "Arial 15",
                         fg = eerieBlack,
                         bg = feldgrau,
                         highlightcolor = mint,
                         width = 40, 
                         height = 2,
                         command = plaintextEncryption)
encryptButton.pack()

## Label for Encrypted Message ##
encMessageBorder = Frame(root, 
                         highlightbackground = resedaGreen,
                         highlightcolor = mint,
                         bg = resedaGreen, 
                         highlightthickness = 5, 
                         bd = 0)
encMessageBorder.place(relx = 0.01, rely = 0.47)
encMessage = Label(encMessageBorder,
                   wraplength= 410,
                   text = "Encrypted message will appear here!",
                   font = "Arial 15",
                   fg = eerieBlack,
                   bg = feldgrau,
                   highlightcolor = mint,
                   width = 40,
                   height = 4)
encMessage.pack()

## Label for Decrypted Message ## 
decMessageBorder = Frame(root,
                         highlightbackground= resedaGreen,
                         highlightcolor= mint,
                         bg = resedaGreen,
                         highlightthickness= 5,
                         bd = 0)
decMessageBorder.place(relx = 0.01, rely = 0.7)
decMessage = Label(decMessageBorder, 
                   wraplength= 200,
                   text= "Decrypted Message will appear here!",
                   font = "Arial 15",
                   fg = eerieBlack,
                   bg = feldgrau,
                   highlightcolor= mint,
                   width = 40,
                   height= 4)
decMessage.pack()

# Execute Tkinter
root.mainloop()

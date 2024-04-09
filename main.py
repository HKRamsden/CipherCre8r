## Imports ##
from tkinter import *
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

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

    print(stored_text)

    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    print(data)
    decodedStr = str(data, encoding = 'utf-8')
    print(decodedStr)

## DES Encryption ##
# not complete, still developing
def desFunc(plaintext):
    print("Mode: DES")
    print(plaintext)


## CBC Encryption
## Not complete, still developing
def cbcFunc(plaintext):
    print("Mode: CBC")
    print(plaintext)


## CFB Encryption ##
## Not complete, still developing
def cfbFunc(plaintext):
    print("Mode: CFB")
    print(plaintext)

    
## CTR Encryption ##
def ctrFunc(plaintext):
    print("Mode: CTR")
    print(plaintext)


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

encryptButtonBorder = Frame(root,
                            highlightbackground = resedaGreen,
                            highlightcolor = mint,
                            bg = resedaGreen,
                            highlightthickness= 5,
                            bd = 0)
encryptButtonBorder.place(relx = 0.01, rely = 0.4)
encryptButton = Button(encryptButtonBorder,
                         text = "Encrypt",
                         font = "Arial 15",
                         fg = eerieBlack,
                         bg = feldgrau,
                         highlightcolor = mint,
                         width = 10, 
                         height = 2,
                         command = plaintextEncryption)
encryptButton.pack()

# Execute Tkinter
root.mainloop()

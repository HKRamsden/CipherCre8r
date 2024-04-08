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
plaintext = b'secret data'
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(plaintext)
nonce = cipher.nonce
stored_text = nonce + tag + ciphertext

print(stored_text)

cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)

print(data)

### APP COMMANDS HERE ###

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
                         height = 2)
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
                       bg= feldgrau)
plaintextEntry.pack()

# Execute Tkinter
root.mainloop()

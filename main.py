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





## AES Encryption ##
data = b'secret data'
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)
nonce = cipher.nonce
print(ciphertext)

# Execute Tkinter
root.mainloop()

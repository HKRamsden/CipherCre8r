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

    

# Execute Tkinter
root.mainloop()

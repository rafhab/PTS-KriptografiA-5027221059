# GUI with Tkinter for Mini-AES

import tkinter as tk
from tkinter import messagebox
from src.mini_aes import MiniAES

def to_binary_string(value):
    return format(value, '016b')

def from_binary_string(text):
    return int(text, 2)

def encrypt_action():
    plaintext = entry_plaintext.get()
    key = entry_key.get()
    
    if len(plaintext) != 16 or len(key) != 16:
        messagebox.showerror("Input Error", "Plaintext dan Key harus 16-bit biner (16 karakter 0 atau 1)")
        return

    plaintext_int = from_binary_string(plaintext)
    key_int = from_binary_string(key)

    aes = MiniAES(key_int)
    ciphertext, logs = aes.encrypt(plaintext_int)

    text_logs.delete("1.0", tk.END)
    for step, state in logs:
        text_logs.insert(tk.END, f"{step}: {to_binary_string(state)}\n")

    entry_ciphertext.delete(0, tk.END)
    entry_ciphertext.insert(0, to_binary_string(ciphertext))

def decrypt_action():
    ciphertext = entry_ciphertext.get()
    key = entry_key.get()

    if len(ciphertext) != 16 or len(key) != 16:
        messagebox.showerror("Input Error", "Ciphertext dan Key harus 16-bit biner (16 karakter 0 atau 1)")
        return

    ciphertext_int = from_binary_string(ciphertext)
    key_int = from_binary_string(key)

    aes = MiniAES(key_int)
    plaintext, logs = aes.decrypt(ciphertext_int)

    text_logs.delete("1.0", tk.END)
    for step, state in logs:
        text_logs.insert(tk.END, f"{step}: {to_binary_string(state)}\n")

    entry_plaintext.delete(0, tk.END)
    entry_plaintext.insert(0, to_binary_string(plaintext))

# Setup GUI
root = tk.Tk()
root.title("Mini-AES 16-bit Encryption/Decryption")

label_plaintext = tk.Label(root, text="Plaintext (16-bit binary):")
label_plaintext.pack()
entry_plaintext = tk.Entry(root, width=20)
entry_plaintext.pack()

label_key = tk.Label(root, text="Key (16-bit binary):")
label_key.pack()
entry_key = tk.Entry(root, width=20)
entry_key.pack()

button_encrypt = tk.Button(root, text="Encrypt", command=encrypt_action)
button_encrypt.pack(pady=5)

label_ciphertext = tk.Label(root, text="Ciphertext (16-bit binary):")
label_ciphertext.pack()
entry_ciphertext = tk.Entry(root, width=20)
entry_ciphertext.pack()

button_decrypt = tk.Button(root, text="Decrypt", command=decrypt_action)
button_decrypt.pack(pady=5)

text_logs = tk.Text(root, height=15, width=50)
text_logs.pack(pady=5)

root.mainloop()

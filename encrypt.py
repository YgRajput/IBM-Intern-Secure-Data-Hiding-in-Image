import cv2
import numpy as np
import os
import tkinter as tk
from tkinter import ttk, messagebox

def int_to_bits(num, bit_length):
    # Convert an integer to a fixed-length list of bits.
    return [int(b) for b in format(num, f'0{bit_length}b')]

def str_to_bits(s):
    # Convert a string into its 8-bit ASCII representation.
    bits = []
    for char in s:
        bits.extend([int(b) for b in format(ord(char), '08b')])
    return bits

def embed_data(image, data_bits):
    flat = image.flatten()
    if len(data_bits) > len(flat):
        raise ValueError("Data too large to embed in this image!")
    for i in range(len(data_bits)):
        flat[i] = (flat[i] & ~1) | data_bits[i]
    return flat.reshape(image.shape)

def encrypt():
    img_path = "mypic.jpg"
    if not os.path.exists(img_path):
        messagebox.showerror("Error", "Input image 'mypic.jpg' not found!")
        return
    image = cv2.imread(img_path)
    if image is None:
        messagebox.showerror("Error", "Failed to load 'mypic.jpg'.")
        return

    secret_message = secret_message_entry.get()
    passcode = passcode_entry.get()
    if not secret_message or not passcode:
        messagebox.showerror("Error", "Secret message and passcode cannot be empty!")
        return

    # Create header:
    # 16 bits: length of passcode, then passcode (8 bits per char)
    # 32 bits: length of secret message, then secret message (8 bits per char)
    header_bits = []
    header_bits.extend(int_to_bits(len(passcode), 16))
    header_bits.extend(str_to_bits(passcode))
    header_bits.extend(int_to_bits(len(secret_message), 32))
    header_bits.extend(str_to_bits(secret_message))

    try:
        encoded_image = embed_data(image, header_bits)
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return

    # Save as PNG to preserve LSBs
    output_path = "encrypted.png"
    cv2.imwrite(output_path, encoded_image)
    messagebox.showinfo("Success", f"Encryption complete! Saved as '{output_path}'.")

# GUI Setup
root = tk.Tk()
root.title("Steganography - Encrypt")
root.geometry("400x300")
style = ttk.Style(root)
style.theme_use('clam')

frame = ttk.Frame(root, padding="20")
frame.pack(expand=True)

ttk.Label(frame, text="Enter Secret Message:").grid(row=0, column=0, sticky="w", pady=5)
secret_message_entry = ttk.Entry(frame, width=40)
secret_message_entry.grid(row=1, column=0, pady=5)

ttk.Label(frame, text="Enter Passcode:").grid(row=2, column=0, sticky="w", pady=5)
passcode_entry = ttk.Entry(frame, width=40, show="*")
passcode_entry.grid(row=3, column=0, pady=5)

encrypt_button = ttk.Button(frame, text="Encrypt", command=encrypt)
encrypt_button.grid(row=4, column=0, pady=20)

root.mainloop()
# Secure Data handing in image Using Statenography
# 🖼️ SteganoCrypt - Image Steganography Tool

SteganoCrypt allows you to securely hide secret messages inside images using Least Significant Bit (LSB) encoding. It ensures safe message embedding and retrieval using a passcode.
# 🖼️ About Encrypted Image
- Encrypted Image Password:–1234.
- Encrypted Secret Data: – "Yogesh Uddalsing Rajput is Studant".
# 🚀 Features

C
- Decrypt Messages – Extract hidden messages with a passcode.
- Passcode Protection – Ensures only authorized access.
- Simple & Fast – Uses OpenCV and standard Python libraries.
- No External Dependencies – Works without NumPy.

# 📦 Installation

Ensure you have Python 3 and git installed, then install OpenCV:

     pip install opencv-python
     
Clone the repository:

     https://github.com/YgRajput/Secure-Data-handing-in-image-Using-Statenography
# Linkdin     
     https://www.linkedin.com/posts/yogesh-rajput-964913219_internship-offer-later-activity-7294757892853833728-pG2B?utm_source=share&utm_medium=member_desktop&rcm=ACoAADchZpwBSjCsAjNZ5GWlIs_WcUxXtWtWKTY
# ⚡ Usage
### 🔒 Encrypt a Message into an Image

      python3 encryption.py

- Enter the image path (supports .png, .jpg, .jpeg).
- Enter the output file name (must be .png).
- Provide the secret message to hide.
- Set a passcode for protection.
- The encrypted image is saved!

### 🔑 Decrypt a Hidden Message

      python3 decryption.py

- Enter the path of the encrypted image.
- Enter the correct passcode.
- The secret message is revealed!

# 🔧 Requirements

- Python 3.x
- OpenCV (opencv-python)

## ⚠️ Notes & Warnings
- If You use linux or macos use python3 encryption.py/decryption.py.
- The output image must be saved in PNG format to preserve the hidden data.
- If the passcode is incorrect, the message cannot be retrieved.
- Large messages may not fit in small images—use a high-resolution image.

## 📜 License

-This project is open-source and free to use!

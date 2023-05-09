"""

@author: github.com/kralchris


"""


from flask import Flask, render_template, request, send_file
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/encrypt", methods=["POST"])
def encrypt():
    # Get the secret key from the user's input
    key = request.form["key"]

    # Generate a salt and use it to derive a key using PBKDF2
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = kdf.derive(key.encode())

    # Generate a random initialization vector
    iv = os.urandom(16)

    # Read the contents of the input file
    with open("input.txt", "rb") as f:
        plaintext = f.read()

    # Encrypt the plaintext using ChaCha20
    cipher = Cipher(algorithms.ChaCha20(key, iv), mode=None)
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    # Save the salt, IV, and ciphertext to a binary file
    with open("encrypted.bin", "wb") as f:
        f.write(salt)
        f.write(iv)
        f.write(ciphertext)

    # Return a message indicating that the file has been encrypted
    return render_template("success.html")

@app.route("/decrypt", methods=["POST"])
def decrypt():
    # Get the secret key from the user's input
    key = request.form["key"]

    # Read the salt, IV, and ciphertext from the binary file
    with open("encrypted.bin", "rb") as f:
        salt = f.read(16)
        iv = f.read(16)
        ciphertext = f.read()

    # Derive the key using PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = kdf.derive(key.encode())

    # Decrypt the ciphertext using ChaCha20
    cipher = Cipher(algorithms.ChaCha20(key, iv), mode=None)
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Save the plaintext to a text file
    with open("decrypted.txt", "wb") as f:
        f.write(plaintext)
        # Save the salt, IV, and ciphertext to a binary file
    with open("encrypted.bin", "wb") as f:
        f.write(salt)
        f.write(iv)
        f.write(ciphertext)

    # Return a message indicating that the file has been encrypted
    return render_template("success.html")

    # Return the decrypted file as a download
    return send_file("decrypted.txt", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=False)

# CS50 - File Encryption Project
CS50 Final Project

[Video Demo: youtube link here](https://youtu.be/Bu-tezOltVM)

<h1>Project Description</h1>

<p>This project is a Flask-based web application that provides encryption and decryption functionalities using the ChaCha20 algorithm.</p>

<h2>Technology Stack</h2>

<ul>
  <li>Python</li>
  <li>Flask</li>
  <li>cryptography library</li>
</ul>

<h2>Files</h2>

<ul>
  <li><code>app.py</code>: The main Flask application file.</li>
  <li><code>index.html</code>: HTML template for the home page.</li>
  <li><code>success.html</code>: HTML template for the success page.</li>
  <li><code>input.txt</code>: The input file to be encrypted.</li>
  <li><code>encrypted.bin</code>: The binary file to store the encrypted data.</li>
  <li><code>decrypted.txt</code>: The decrypted file.</li>
</ul>

<h2>Encryption Method</h2>

<p>The encryption method used in this project is ChaCha20. ChaCha20 is a symmetric encryption algorithm that provides high security and performance. Through a series of mixing and round operations, it generates a keystream block. This keystream is XORed with the plaintext or ciphertext to perform encryption or decryption. ChaCha20 is known for its simplicity, speed, and resistance to cryptographic attacks when used correctly. It is widely used in applications like secure messaging protocols and disk encryption.</p>

<h2>Backend</h2>

<p>The backend of the application is built using Flask, a web framework for Python. Flask allows for the development of web applications with ease and provides integration with various libraries and tools.</p>

<p>To run the application, execute the following command:</p>

<pre><code>python app.py</code></pre>

<h2>Preview:</h2>

![preview](https://github.com/kralchris/CS50-/assets/90260861/fad2a4a0-0c60-4108-bb56-48979430b414)

<h2>Code Breakdown</h2>
<p>The application uses the Flask framework to handle HTTP requests and responses.

The / route serves as the home page, which renders the index.html template.

The /encrypt route is triggered when the user submits a form to encrypt a file.
<br><br><b>It performs the following steps:</b>

Retrieves the secret key from the user's input.
Generates a random salt and derives a key using PBKDF2 with the provided key and salt.
Generates a random initialization vector (IV).
Reads the contents of the input file to be encrypted.
Initializes a ChaCha20 cipher with the derived key and IV.
Encrypts the plaintext using the cipher.
Writes the salt, IV, and ciphertext to an output binary file.
Renders the success.html template to display a success message.
The /decrypt route is triggered when the user submits a form to decrypt a file.
<br><br><b>It performs the following steps:</b><br><br>
Retrieves the secret key from the user's input.
Reads the salt, IV, and ciphertext from the encrypted binary file.
Derives the key using PBKDF2 with the provided key and salt.
Initializes a ChaCha20 cipher with the derived key and IV.
Decrypts the ciphertext using the cipher.
Writes the decrypted plaintext to an output text file.
Renders the success.html template to display a success message.
The application runs when the script is executed directly (if __name__ == "__main__"). It runs the Flask app with debug mode disabled.</p>

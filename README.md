# Python-Password-Manager'
## About the project
This was a small coding project I started during semester break. I wanted to implement a password manager where users can choose to store a key file externally for extra security. Upon running the code, there are three paths:
  1. If the key file is contained in the same folder as the program, the user will simply   be prompted to enter a PIN (yet to be encrypted).
  2. If the user has never created a key file, the key file does not exist or is empty, the user is prompted to choose the file path where the key will be generated, and then the user will be asked to create a 4-digit PIN.
  3. If the code has been previously generated (as per the credentials file), then a directory is opened for the user to locate the key.

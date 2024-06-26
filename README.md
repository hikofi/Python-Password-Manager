# Python-Password-Manager'
## About the project
This was a small coding project I started during my winter break in uni. This password manager enables use to store a key file, 'key.txt', externally for increased security. Currently the password manager uses a simple hashing algorithm that is different each time a key is generated.


Upon running the code, there are three paths:
  1. If the key file is in the same running folder as the program, the user will simply be prompted to enter a password.
  2. If the user has never created a key file, the key file does not exist or is empty, the user is prompted to choose the file path where the key will be generated, and then the user will be asked to create a 4-digit PIN.
  3. If the code has been previously generated (as per the credentials file), then a directory is opened for the user to locate the key.

## Future Plans
* Provide Integrity if key or files are altered.
* 

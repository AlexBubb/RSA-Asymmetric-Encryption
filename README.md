OVERVIEW:
This is an implementation of the famous RSA Public Key Encryption Algorithm. The advantage of this algorithm is that it creates two sets of keys. The public key is used for encrypting messages and the private key is used for decryption. This allows anyone to send a message but only one person can read it. For example, on a messaging platform everybody can send their love letters to a celebrity crush by encrypting their message with the public key. Everybody can also trust that the only person who can read their messages is the celebrity using the hidden private key. My project consists of three files: main.py runs the demo with menus; rsafun.py is designed to be an all inclusive file that can be taken anywhere for any new implementations; screenfun.py is a general file that contains some useful functions for clearing the screen.

DEMO GUIDE:
To run the demo you must have a version of python installed. Download and extract files and run the main.py file.

RSAFUN GUDIE:
If you want to take rsafun.py and use it elsewhere here are the useful functions:

genkeys() returns two lists with the format [ [public key e, public key n], [private key d, private key n] ]

encrypt(message,e,n) takes a string message and the two numbers from the private key and returns an integer that is the encrypted message

decrypt(cyphertext,d,n) takes a string cyphertext (should be a number) and the two numbers from the private key and returns a string that is the original messag

createKeyPair() is a small menu that creates a keypair and displays them.

All other functions are called by one of those four

import rsafun
import screenfun
import ast
keys = [[],[]]
while True:
    screenfun.clear()
    print("1. Generate new keypair")
    print("2. Import a keypair")
    print("3. View current keypair")
    print("4. Encrypt message with current public key")
    print("5. Decrypt message with current private key")
    print("6. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        keys = rsafun.createKeyPair()
        
    elif choice == "2":
        keys = [[],[]]
        print("Paste in your public key in decimal with the format [e,n]")
        print("Leave it blank if you don't have the public key")
        public = input("Public Key: ")
        if public != "":
            keys[0] = ast.literal_eval(public)
            keys[0][0] = int(keys[0][0])
            keys[0][1] = int(keys[0][1])
        else:
            print("no public")
            keys[0] = []
        screenfun.clear()
        print("Paste in your private key in decimal with the format [e,n]")
        print("Leave it blank if you don't have the private key")
        
        private = input("Private Key: ")
        if private != "":
            keys[1] = ast.literal_eval(private)
            keys[1][0] = int(keys[1][0])
            keys[1][1] = int(keys[1][1])
        else:
            keys[1] = []
    elif choice == "3":
        while True:
            print("1. View public key")
            print("2. View private key")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
              print("Public key: ", keys[0])
              input("Press enter to continue...")
              screenfun.clear()
            elif choice == "2":
              print("Private key: ", keys[1][0])
              input("Press enter to continue...")
              screenfun.clear()
            elif choice == "3":
              break
            
    elif choice == "4":
        if (keys[0] != []):
            print(rsafun.encrypt(input("What would you like to encrypt: "), keys[0][0], keys[0][1]))
            input("Press enter to continue...")
        else:
            print("Please generate or import a public key in order to encrypt.")
            input("Press enter to continue...")
            
    elif choice == "5":
        if (keys[1] != []):
            print(rsafun.decrpyt(input("What would you like to dencrypt: "), keys[1][0], keys[1][1]))
            input("Press enter to continue...")
        else:
            print("Please generate or import a private key in order to decrpyt.")
            input("Press enter to continue...")
    elif choice == "6":
        break

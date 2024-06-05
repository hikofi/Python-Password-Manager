import os
from tkinter.filedialog import askdirectory

# Check if there is key file,
def keyExists():
    f = open("credentials.txt", "r")
    isKeyGenerated = f.readline(18).strip('\n')
    # When new, there won't be a key file. We have to create this and update the directory.
    # If you're using secure keys, every time you open it, you will have to locate the key
    keyPath = './keys.txt'
    # PATH = './faketestingfile'

    if os.path.isfile(keyPath) and os.access(keyPath, os.R_OK) and isKeyGenerated == "keyGenerated:TRUE":
        print("Key has been located.")
        pinUnlock()
    elif isKeyGenerated == "keyGenerated:FALSE": #Isn't this meant to be encrypted?
        print("Performing first start-up, choose a path for your key file")
        path = askdirectory()
        if path:
            keyPath = os.path.join(path, 'keys.txt')
            print(f"Key file will be created at: {keyPath}")

            with open("credentials.txt", "w") as f:
                # Not sure how well this is working
                isKeyGenerated[1:]
                f.write("keyGenerated:TRUE")

            userPin = input("Choose a 4-digit pin: ")
            if userPin !="" and userPin.isnumeric() and len(userPin) == 4:
                reapeatUserPin = input("Reapt the 4-digit pin: ")
                if userPin == reapeatUserPin:
                    # I will have to encrypt this some time
                    with open(keyPath, "w") as key_file:
                        key_file.write(userPin)

            with open(keyPath, "w") as key_file:
                key_file.write("Your key content here.")

            
    else:
        # See if credentials.txt first line reads, keyExists. If not then
        # keyGen() -> pinGen()
        print("The key file is either missing or unreadable.")
        newPath = askdirectory()
        # You need to find a way to open up the path if it is unreachable
        
       
def pinUnlock():
    # Open the key file, read the first 4 latters
        correctPin = False
        with open("keys.txt", "r") as f:
            pin = f.readline(4).strip('\n')
            # Not empty, is numeric and length of 4
            if pin !="" and pin.isnumeric() and len(pin) == 4:
                userPin = input("Enter your pin: ")
                while correctPin == False:
                    if userPin == pin:
                        correctPin = True
                        print("Good job for remembering your pin lmao")
                    else:
                        userPin = input("Wrong pin buddy. Enter your pin: ")


def main():
    keyExists()
    #



if __name__ == '__main__':
    main()
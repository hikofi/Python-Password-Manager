import os

# Check if there is key file,
def keyExists():
    f = open("credentials.txt", "r")
    isKeyGenerated = f.readline(18).strip('\n')
    # When new, there won't be a key file. We have to create this and update the directory.
    PATH = './keys.txt'
    # PATH = './faketestingfile'
    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
        print("Key has been located.")
        pinUnlock()
    elif isKeyGenerated == "keyGenerated:False":
        print("We need to generate a key first")
    else:
        # See if credentials.txt first line reads, keyExists. If not then
        # keyGen() -> pinGen()

        # You need to find a way to open up the path if it is unreachable
        print("The key file is either missing or unreadable.")
       
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
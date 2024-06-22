import os
import tkinter as tk
from tkinter import Entry, ttk

# if os.path.isfile("db/masterpassword.json"): # loading json file with stored password.
#       with open("db/masterpassword.json", 'r') as jsondata:
#           jfile = json.load(jsondata)


def keyExists():
    masterKeyPath = './masterKey.json'
    keyGenerated = False
    f = open("credentials.json", "r")
  
    if f.read(1):
    # if os.path.isfile("credentials.json") and os.path.getsize("credentials.json") > 0:
        keyGenerated = True
    else:
        pass

    if os.path.isfile(masterKeyPath) and keyGenerated == True:
        print("Key has been located.")
        return 1
    elif not os.path.isfile(masterKeyPath) and keyGenerated == True:
        print("Let's locate the key")
        return 2
    elif not os.path.isfile(masterKeyPath) and keyGenerated == False:
        print("Let's generate a key")
        return 3
        # pinUnlock()
   
    # Add a lost key file function... generate a new key!   
def main():
    root = tk.Tk()
    root.title("kofi's Password Manager")
    root.tk.call('source', 'forest-dark.tcl')
    ttk.Style().theme_use('forest-dark')
    root.geometry("960x540")
    
    option = keyExists()

    if option == 1:
        label = ttk.Label(root, text="Enter your password")
        label.pack(pady=20)
        passwordBox= ttk.Entry(root,show="*",width=20)
        passwordBox.pack()
    elif option == 0:
        label = ttk.Label(root, text="Option 0 is selected")
        label.pack(pady=20)
    # elif option == 2:
    # elif option == 3:

    root.mainloop()

if __name__ == '__main__':
    main()
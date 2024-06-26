import os
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QLineEdit, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
# from PySide6.QtCore import Qt.AlignCenter??

class LockScreen(QWidget):
    def __init__(self):
        super().__init__() #???????
        self.setupUI()
        
    def setupUI(self):
        # self.setGeometry(100, 100, 200, 100)  # Set the size of the LockScreen
        # Create a vertical layout
        self.setFixedSize(480, 540)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(120, 230, 120, 230) #left, top, right, bot

         # Set spacing between widgets (0 for no space)
        # layout.setSpacing(0)
        # QLineEdit for the password

        # Maybe use QString to be like, Hi name, then say enter your password
        self.text = QLabel("Enter your password", self)
        self.text.setAlignment(Qt.AlignCenter)
        font = QFont("Helvetica", 11)  
        self.text.setFont(font)

        self.pw = QLineEdit(self)
        self.pw.setEchoMode(QLineEdit.Password)


        # QPushButton for submission
        self.submitButton = QPushButton('Submit', self)
        font = QFont("Helvetica", 10)  
        self.submitButton.setFont(font)

        # Add widgets to the layout
        layout.addWidget(self.text)
        layout.addWidget(self.pw)
        layout.addWidget(self.submitButton)

        # Set the layout on the QWidget
        self.setLayout(layout)

class newUser(QWidget):
    def __init__(self):
        super().__init__()
        self.setUpKeyUI()

    def setUpKeyUI(self):
        # Set size and layout
        self.setFixedSize(480, 540)       
        layout = QVBoxLayout()
        layout.setContentsMargins(120, 150, 120, 150) #left, top, right, bot
        # Enter your name
        # Master password
        # Generates a key
        # add homescreen widgets
        
        # Name for user UI
        self.nameText = QLabel("Enter your name: ", self)
        self.nameText.setAlignment(Qt.AlignCenter)
        font = QFont("Helvetica", 11)
        self.nameText.setFont(font)
        self.name = QLineEdit(self)
        self.name.setFont(font)

        # Master Password, maybe make it output it onto a text document.
        # Make sure contains capital and numbers/symbols,
        # Make button to generate a random password
        self.passText = QLabel("Enter your password: ", self)
        self.passText.setAlignment(Qt.AlignCenter)
        font = QFont("Helvetica", 11)
        self.passText.setFont(font)
        self.pw = QLineEdit(self)
        self.pw.setEchoMode(QLineEdit.Password)
        self.pw.setToolTip("Password must:\n - Be longer than 6 characters\n - Contain at least one uppercase letter \n - Contain at least one number")

        #Repeat Master password
        self.passText2 = QLabel("Re-enter your password: ", self)
        self.passText2.setAlignment(Qt.AlignCenter)
        font = QFont("Helvetica", 11)
        self.passText2.setFont(font)
        self.pw2 = QLineEdit(self)
        self.pw2.setEchoMode(QLineEdit.Password)
        self.pw2.setToolTip("Password must:\n - Be longer than 6 characters\n - Contain at least one uppercase letter \n - Contain at least one number")
        
        # Add wid to layout
        layout.addWidget(self.nameText)
        layout.addWidget(self.name)
        layout.addWidget(self.passText)
        layout.addWidget(self.pw)
        layout.addWidget(self.passText2)
        layout.addWidget(self.pw2)


         # Set the layout on the QWidget
        self.setLayout(layout)



class HomeScreen(QWidget):
    def __init__(self):
        super().__init__()
        # add homescreen widgets

    # Add a lost key file function... generate a new key!   
class passManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 480, 540) #xpos, ypos, width, height
        self.setWindowTitle("kofi's Password Manager")
        self.initUI()

    def initUI(self):
        self.status = self.keyExists()
        self.startScreen()

    def keyExists(self): #self?
        masterKeyPath = './masterKey.json'
        keyGenerated = False
        
        try:
            with open("credentials.json", "r") as f:
                if f.read(1):
                    keyGenerated = True
        except FileNotFoundError:
            keyGenerated = False  # Handle the file not being found

        if os.path.isfile(masterKeyPath) and keyGenerated:
            print("Key has been located.")
            return 1  
        elif not os.path.isfile(masterKeyPath) and keyGenerated:
            print("Let's locate the key.")
            return 2  
        else:
            print("Let's generate a key.")
            return 3   
           
    def startScreen(self):
        if self.status == 1:
            self.setCentralWidget(LockScreen())
        elif self.status == 2:
            self.label = QLabel("Let's locate the key.", self)
            # self.label.move(50, 50)
            # self.label.show()
        elif self.status == 3:
            self.setCentralWidget(newUser())
            # self.label.move(50, 50)
            # self.label.show()

def main():
    app = QApplication(sys.argv)
    win = passManager()
    win.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
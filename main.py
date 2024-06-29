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
        self.submitButton = QPushButton("Submit", self)
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
        layout.setContentsMargins(120, 50, 120, 50) #left, top, right, bot

        
        # Enter your name
        # Master password
        # Generates a key
        # add homescreen widgets


        # Name for user UI
        self.nameText = QLabel("Enter your name: ", self)
        self.nameText.setAlignment(Qt.AlignCenter)
        font = QFont("Helvetica", 11)
        self.nameText.setFont(font)
        self.name = QLineEdit("User", self)
        self.name.setMaxLength(13)
        self.name.setToolTip("Maximum length of 13 characters")
        self.name.setFont(font)

        # Master Password, maybe make it output it onto a text document.
        # Make sure contains capital and numbers/symbols,
        # Make button to generate a random password
        self.passText = QLabel("Enter your password: ", self)
        self.passText.setAlignment(Qt.AlignCenter)
        # font = QFont("Helvetica", 11)
        self.passText.setFont(font)
        self.pw = QLineEdit(self)
        self.pw.setEchoMode(QLineEdit.Password)
        self.pw.setToolTip("Password must:\n - Be longer than 6 characters\n - Contain at least one uppercase letter \n - Contain at least one number")

        # Repeat Master password
        self.passText2 = QLabel("Re-enter your password: ", self)
        self.passText2.setAlignment(Qt.AlignCenter)
        # font = QFont("Helvetica", 11)
        self.passText2.setFont(font)
        self.pw2 = QLineEdit(self)
        self.pw2.setEchoMode(QLineEdit.Password)
        self.pw2.setToolTip("Password must:\n - Be longer than 6 characters\n - Contain at least one uppercase letter \n - Contain at least one number")
        
        # Updated username function
        self.usernameUpdate = QLabel(self)
        formatted_text = f"Welcome, <span style='color: rgb(10, 186, 181);'>User</span>"
        self.usernameUpdate.setText(formatted_text)
        self.usernameUpdate.setAlignment(Qt.AlignCenter)
        fontUpdate = QFont("Helvetica", 15)
        self.usernameUpdate.setFont(fontUpdate)

        # Submit button
        self.submitButton = QPushButton("Submit", self)
        font = QFont("Helvetica", 10)  
        self.submitButton.setFont(font)
        # self.submitButton.setToolTip("Username must not be empty\nPassword must:\n - Be longer than 6 characters\n - Contain at least one uppercase letter \n - Contain at least one number")
        # Disable button until username is inputted and password match
        # self.submitButton.setEnabled(False)

        # Password Warning 
        self.passwordRules = QLabel(self)
        self.passwordRules.setFont(font)
        # self.passwordRules.setText("Passwords must:")
        # self.passwordRules.setStyleSheet("color: rgba(255, 255, 255, 160);")

        # Password Warning Non matching
        self.passwordRulesNonMatch = QLabel(self)
        self.passwordRulesNonMatch.setFont(font)
        # self.passwordRulesNonMatch.setText(" - Match")
        # self.passwordRulesNonMatch.setStyleSheet("color: rgba(255, 255, 255, 160);")

        # Password Warning less than 6 char
        self.passwordRulesLength = QLabel(self)
        self.passwordRulesLength.setFont(font)
        # self.passwordRulesLength.setText(" - Be at least 6 characters in length")
        # self.passwordRulesLength.setStyleSheet("color: rgba(255, 255, 255, 160);")

        # Password Warning no upper
        self.passwordRulesUpper = QLabel(self)
        self.passwordRulesUpper.setFont(font)
        # self.passwordRulesUpper.setText(" - Contain an uppercase letter")
        # self.passwordRulesUpper.setStyleSheet("color: rgba(255, 255, 255, 160);")

        # Password Warning message
        self.passwordRulesNum = QLabel(self)
        self.passwordRulesNum.setFont(font)
        # self.passwordRulesNum.setText(" - Contain a number")
        # self.passwordRulesNum.setStyleSheet("color: rgba(255, 255, 255, 160);")

        layout.addWidget(self.usernameUpdate)
        # Add wid to layout
        layout.addWidget(self.nameText)
        layout.addWidget(self.name)
        layout.addWidget(self.passText)
        layout.addWidget(self.pw)
        layout.addWidget(self.passText2)
        layout.addWidget(self.pw2)
        layout.addWidget(self.submitButton)
        # Password Rules
        layout.addWidget(self.passwordRules)
        layout.addWidget(self.passwordRulesNonMatch)
        layout.addWidget(self.passwordRulesLength)
        layout.addWidget(self.passwordRulesUpper)
        layout.addWidget(self.passwordRulesNum)

        self.name.textChanged.connect(self.updateUsername)
        self.name.textChanged.connect(self.checkUserAndPass)

        # # Send to see if passwords match (&username is not null)
        self.pw.textChanged.connect(self.passwordCriteriaTextInit)
        self.pw.textChanged.connect(self.checkUserAndPass)
        # # Send to see if passwords match (&username is not null)
        self.pw2.textChanged.connect(self.passwordCriteriaTextInit)
        self.pw2.textChanged.connect(self.checkUserAndPass)
        # Button press check
        self.submitButton.clicked.connect(self.checkUserAndPass)


        # Set the layout on the QWidget
        self.setLayout(layout)

    def updateUsername(self, text):
        # self.usernameUpdate.setText(f"Welcome, {text}")
        # self.usernameUpdate.setStyleSheet("color: rgb(10, 186, 181);")
        formatted_text = f"Welcome, <span style='color: rgb(10, 186, 181);'>{text}</span>"
        self.usernameUpdate.setText(formatted_text)

    # Determine what is missing, then add QLabel underneath submit button
    # This can be rewritting user any() for c in self.pw.text()

    def passwordCriteriaTextInit(self):
        # Password Warning 
        if self.pw.text() or self.pw2.text() != '':
            self.passwordRules.setText("Passwords must:")
            self.passwordRules.setStyleSheet("color: rgba(255, 255, 255, 160);")

            # Password Warning Non matching
            self.passwordRulesNonMatch.setText(" - Match")
            self.passwordRulesNonMatch.setStyleSheet("color: rgba(255, 255, 255, 160);")

            # Password Warning less than 6 char
            self.passwordRulesLength.setText(" - Be at least 6 characters in length")
            self.passwordRulesLength.setStyleSheet("color: rgba(255, 255, 255, 160);")

            # Password Warning no upper
            self.passwordRulesUpper.setText(" - Contain an uppercase letter")
            self.passwordRulesUpper.setStyleSheet("color: rgba(255, 255, 255, 160);")

            # Password Warning message
            self.passwordRulesNum.setText(" - Contain a number")
            self.passwordRulesNum.setStyleSheet("color: rgba(255, 255, 255, 160);")
        else:
            self.passwordRules.setText("")
            self.passwordRulesNonMatch.setText("")
            self.passwordRulesLength.setText("")
            self.passwordRulesUpper.setText("")
            self.passwordRulesNum.setText("")

    def checkUserAndPass(self):
        upperCase = False
        for character in self.pw.text():
            if character.isupper():
                upperCase = True
                break

        containsNumber = False
        for character in self.pw.text():
            if character.isdigit():
                containsNumber = True
                break

        upperCaseLower = False
        for character in self.pw2.text():
            if character.isupper():
                upperCaseLower = True
                break

        containsNumberLower = False
        for character in self.pw2.text():
            if character.isdigit():
                containsNumberLower = True
                break
        
        containsSpace = False
        for character3 in self.name.text():
            if character3.isspace():
                containsSpace = True
                break

        if self.pw.text() == self.pw2.text() and len(self.pw.text()) >= 6 and upperCase == True and containsNumber == True and len(self.name.text()) > 0:
            # self.submitButton.setEnabled(True)
            print("Move to next step")
        elif self.name.text() == '' or containsSpace == True and self.pw.text() != self.pw2.text() and len(self.pw.text()) >= 6 and upperCase == True and containsNumber == True:
            self.passwordRules.setText("Username is empty or contains spaces")
        
        # Need to fix this as once the setText username is empty is added.. i cant reset the test
        # elif self.name.text() != '' or containsSpace == False or self.pw.text() != self.pw2.text() or len(self.pw.text()) <= 6 and upperCase == False and containsNumber == False:
        #     self.passwordRules.setText("Passwords must:")
        # elif self.name.text() == '' or containsSpace == True or self.pw.text() != self.pw2.text() or len(self.pw.text()) <= 6 and upperCase == False and containsNumber == False:
        #     self.passwordRules.setText("Username is empty or contains spaces\nPasswords must:")


        # Strikethrough Font, ticking off criterias met:
        # strikeOutfont = QFont("Helvetica", 10)  
        # self.passwordRulesNonMatch.setFont(QFont.setStrikeOut(True))
        font = QFont("Helvetica", 10)  
        fontMeetCriteria = QFont("Helvetica", 10)
        
        fontMeetCriteria.setStrikeOut(True)

        if self.pw.text() == self.pw2.text() and self.pw.text() != '':
            self.passwordRulesNonMatch.setStyleSheet("color: rgba(255, 255, 255, 25);")
            self.passwordRulesNonMatch.setFont(fontMeetCriteria)
        else:
            self.passwordRulesNonMatch.setStyleSheet("color: rgba(255, 255, 255, 160);")
            self.passwordRulesNonMatch.setFont(font)
        # Update

        if len(self.pw.text()) >= 6 or len(self.pw2.text()) >= 6:
            self.passwordRulesLength.setStyleSheet("color: rgba(255, 255, 255, 25);")
            self.passwordRulesLength.setFont(fontMeetCriteria)
        else:
            self.passwordRulesLength.setStyleSheet("color: rgba(255, 255, 255, 160);")
            self.passwordRulesLength.setFont(font)
        
        # Uppercase will show if only the top password contains upercase, needs to do this for lower as well
        if upperCase == True or upperCaseLower == True:
            self.passwordRulesUpper.setStyleSheet("color: rgba(255, 255, 255, 25);")
            self.passwordRulesUpper.setFont(fontMeetCriteria)
        else:
            self.passwordRulesUpper.setStyleSheet("color: rgba(255, 255, 255, 160);")
            self.passwordRulesUpper.setFont(font)
        
        if containsNumber == True or containsNumberLower == True:
            self.passwordRulesNum.setStyleSheet("color: rgba(255, 255, 255, 25);")
            self.passwordRulesNum.setFont(fontMeetCriteria)
        else:
            self.passwordRulesNum.setStyleSheet("color: rgba(255, 255, 255, 160);")
            self.passwordRulesNum.setFont(font)

           # Uppercase for lower
        # if upperCaseLower == True:
        #     self.passwordRulesUpper.setStyleSheet("color: rgba(255, 255, 255, 25);")
        #     self.passwordRulesUpper.setFont(fontMeetCriteria)
        # else:
        #     self.passwordRulesUpper.setStyleSheet("color: rgba(255, 255, 255, 160);")
        #     self.passwordRulesUpper.setFont(font)
        
        # if containsNumberLower == True:
        #     self.passwordRulesNum.setStyleSheet("color: rgba(255, 255, 255, 25);")
        #     self.passwordRulesNum.setFont(fontMeetCriteria)
        # else:
        #     self.passwordRulesNum.setStyleSheet("color: rgba(255, 255, 255, 160);")
        #     self.passwordRulesNum.setFont(font)
        # else:
        #     self.passwordRules.setText("Password must be 6 characters minimum")
        #     self.passwordRules2.setText("Password must contain 1 uppercase minimum")
        #     self.passwordRules3.setText("Password must contain 1 number minimum")
        #     print("There is an issue")


    #Generate key
    # On button click
        # if checkbox is ticked, ask user to choose a path to generate a text file
    # Generate master key and fill in credentials
    # Move onto next layout

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
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from database import Database
from time import sleep

database = Database()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(-30, -10, 861, 591))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("assets/background.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.mainTitle = QtWidgets.QLabel(self.centralwidget)
        self.mainTitle.setGeometry(QtCore.QRect(220, 50, 371, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.mainTitle.setFont(font)
        self.mainTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.mainTitle.setObjectName("mainTitle")
        self.usernameTitle = QtWidgets.QLabel(self.centralwidget)
        self.usernameTitle.setGeometry(QtCore.QRect(70, 180, 371, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.usernameTitle.setFont(font)
        self.usernameTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.usernameTitle.setObjectName("usernameTitle")
        self.passwordTitle = QtWidgets.QLabel(self.centralwidget)
        self.passwordTitle.setGeometry(QtCore.QRect(60, 260, 371, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.passwordTitle.setFont(font)
        self.passwordTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordTitle.setObjectName("passwordTitle")
        self.usernameTextEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameTextEdit.setGeometry(QtCore.QRect(370, 190, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.usernameTextEdit.setFont(font)
        self.usernameTextEdit.setObjectName("usernameTextEdit")
        self.passwordTextEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordTextEdit.setGeometry(QtCore.QRect(370, 270, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(18)
        self.passwordTextEdit.setFont(font)
        self.passwordTextEdit.setObjectName("passwordTextEdit")
        self.joinButton = QtWidgets.QPushButton(self.centralwidget)
        self.joinButton.setGeometry(QtCore.QRect(430, 350, 161, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.joinButton.setFont(font)
        self.joinButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.joinButton.setStyleSheet("background-color: white;")
        self.joinButton.setObjectName("joinButton")
        self.dontHaveAccountLabal = QtWidgets.QLabel(self.centralwidget)
        self.dontHaveAccountLabal.setGeometry(QtCore.QRect(160, 470, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(16)
        self.dontHaveAccountLabal.setFont(font)
        self.dontHaveAccountLabal.setObjectName("dontHaveAccountLabal")
        self.createAccountButton = QtWidgets.QPushButton(self.centralwidget)
        self.createAccountButton.setGeometry(QtCore.QRect(510, 470, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.createAccountButton.setFont(font)
        self.createAccountButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.createAccountButton.setStyleSheet("background-color: white;")
        self.createAccountButton.setObjectName("createAccountButton")
        self.createFinalButton = QtWidgets.QPushButton(self.centralwidget)
        self.createFinalButton.setGeometry(QtCore.QRect(430, 350, 161, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.createFinalButton.setFont(font)
        self.createFinalButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.createFinalButton.setStyleSheet("background-color: white;")
        self.createFinalButton.setObjectName("createFinalButton")
        self.goToJoinButton = QtWidgets.QPushButton(self.centralwidget)
        self.goToJoinButton.setGeometry(QtCore.QRect(510, 470, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.goToJoinButton.setFont(font)
        self.goToJoinButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.goToJoinButton.setStyleSheet("background-color: white;")
        self.goToJoinButton.setObjectName("goToJoinButton")
        self.alreadyHaveAccountLabel = QtWidgets.QLabel(self.centralwidget)
        self.alreadyHaveAccountLabel.setGeometry(QtCore.QRect(230, 470, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(16)
        self.alreadyHaveAccountLabel.setFont(font)
        self.alreadyHaveAccountLabel.setObjectName("alreadyHaveAccountLabel")
        self.welcomeLabel = QtWidgets.QLabel(self.centralwidget)
        self.welcomeLabel.setGeometry(QtCore.QRect(0, 220, 801, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.backToJoinLabel = QtWidgets.QLabel(self.centralwidget)
        self.backToJoinLabel.setGeometry(QtCore.QRect(230, 470, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(16)
        self.backToJoinLabel.setFont(font)
        self.backToJoinLabel.setObjectName("backToJoinLabel")
        self.detailsWongLabel = QtWidgets.QLabel(self.centralwidget)
        self.detailsWongLabel.setGeometry(QtCore.QRect(340, 150, 331, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.detailsWongLabel.setFont(font)
        self.detailsWongLabel.setStyleSheet("")
        self.detailsWongLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.detailsWongLabel.setObjectName("detailsWongLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.joinWinLabels = [self.joinButton, self.createAccountButton, self.dontHaveAccountLabal, self.usernameTextEdit, self.usernameTitle, self.passwordTextEdit, self.passwordTitle]
        self.createWinLabels = [self.goToJoinButton, self.createFinalButton, self.alreadyHaveAccountLabel, self.usernameTextEdit, self.usernameTitle, self.passwordTextEdit, self.passwordTitle]
        self.welcomeWinLabels = [self.welcomeLabel, self.backToJoinLabel, self.goToJoinButton]

        self.joinButton.clicked.connect(self.joinClicked)
        self.createAccountButton.clicked.connect(self.goToCreateClicked)
        self.goToJoinButton.clicked.connect(self.goToJoinClicked)
        self.createFinalButton.clicked.connect(self.createAccountClicked)
        
        for label in self.createWinLabels:
            label.setHidden(True)
        for label in self.welcomeWinLabels:
            label.setHidden(True)
        for label in self.joinWinLabels:
            label.setHidden(False)
        self.detailsWongLabel.setHidden(True)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainTitle.setText(_translate("MainWindow", "Login System"))
        self.usernameTitle.setText(_translate("MainWindow", "Username: "))
        self.passwordTitle.setText(_translate("MainWindow", "Password:"))
        self.joinButton.setText(_translate("MainWindow", "Join"))
        self.dontHaveAccountLabal.setText(_translate("MainWindow", "don\'t have an account? create one!"))
        self.createAccountButton.setText(_translate("MainWindow", "Create"))
        self.createFinalButton.setText(_translate("MainWindow", "Create"))
        self.goToJoinButton.setText(_translate("MainWindow", "Join"))
        self.alreadyHaveAccountLabel.setText(_translate("MainWindow", "already have an account? "))
        self.welcomeLabel.setText(_translate("MainWindow", "Welcome "))
        self.backToJoinLabel.setText(_translate("MainWindow", "Go Back To Join Page"))
        self.detailsWongLabel.setText(_translate("MainWindow", "Wrong Username Or Password, Try Again"))


    def joinClicked(self):
        username = self.usernameTextEdit.text()
        password = self.passwordTextEdit.text()
        if database.isAccountExists(username, password) == True:
            self.detailsWongLabel.setHidden(True)
            self.welcomeLabel.setText("Welcome " + username)
            for label in self.joinWinLabels:
                label.setHidden(True)
            for label in self.welcomeWinLabels:
                label.setHidden(False)
            self.goToJoinButton.setGeometry(QtCore.QRect(460, 470, 111, 31))
        else:
            self.detailsWongLabel.setHidden(False)
        self.usernameTextEdit.setText("")
        self.passwordTextEdit.setText("")



    def goToCreateClicked(self):
        self.usernameTextEdit.setText("")
        self.passwordTextEdit.setText("")
        for label in self.joinWinLabels:
            label.setHidden(True)
        for label in self.createWinLabels:
            label.setHidden(False)

    def goToJoinClicked(self):
        self.usernameTextEdit.setText("")
        self.passwordTextEdit.setText("")
        for label in self.createWinLabels:
            label.setHidden(True)
        for label in self.joinWinLabels:
            label.setHidden(False)
        for label in self.welcomeWinLabels:
            label.setHidden(True)

        
    def createAccountClicked(self):
        un = self.usernameTextEdit.text()
        pw = self.passwordTextEdit.text()
        if database.createAccount(un, pw) == "Username Exists":           
            print("Username Already Exists")
        else:
            print("account created")
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
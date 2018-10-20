#imported dependencies
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

#UI 
class SignUpForm(object):
    #sign up button method
    def signUp(self):
        print ("sign up button clicked")

    #exit button method
    def close(self):
        print ("exit button clicked")

    #Form layout for responsive design
    def setupUi(self, Form):
        #form
        Form.setObjectName("Form")
        Form.resize(513, 583)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.5221, y1:0.568, x2:1, y2:1, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(50, 100, 50, 100)

        #label
        self.label = QtWidgets.QLabel(Form)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(67, 67, 67);\n""background-color: rgba(255,255,255,0);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        #Employee ID text box
        self.txtEID = QtWidgets.QLineEdit(Form)
        self.txtEID.setMinimumSize(QtCore.QSize(0, 30))
        self.txtEID.setStyleSheet("background-color: rgba(255, 255, 255,1)")
        self.txtEID.setObjectName("txtEID")
        self.txtEID.setClearButtonEnabled(True)
        self.verticalLayout.addWidget(self.txtEID)

        #label 2
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(67, 67, 67);\n" "background-color: rgba(255,255,255,0);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        #First name text box
        self.txtFname = QtWidgets.QLineEdit(Form)
        self.txtFname.setMinimumSize(QtCore.QSize(0, 30))
        self.txtFname.setStyleSheet("background-color: rgba(255, 255, 255,.9)")
        self.txtFname.setObjectName("txtFname")
        self.txtFname.setClearButtonEnabled(True)
        self.verticalLayout.addWidget(self.txtFname)

        #label 3
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(67, 67, 67);\n" "background-color: rgba(255,255,255,0);\n" "")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        #Last name text box
        self.txtLname = QtWidgets.QLineEdit(Form)
        self.txtLname.setMinimumSize(QtCore.QSize(0, 30))
        self.txtLname.setStyleSheet("background-color: rgba(255, 255, 255,.8)")
        self.txtLname.setObjectName("txtLname")
        self.txtLname.setClearButtonEnabled(True)
        self.verticalLayout.addWidget(self.txtLname)

        #label 4
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(67, 67, 67);\n" "background-color: rgba(255,255,255,0);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)

        #E-mail text box
        self.txtEmail = QtWidgets.QLineEdit(Form)
        self.txtEmail.setMinimumSize(QtCore.QSize(0, 30))
        self.txtEmail.setStyleSheet("background-color: rgba(255, 255, 255,.7)")
        self.txtEmail.setObjectName("txtEmail")
        self.txtEmail.setClearButtonEnabled(True)
        self.verticalLayout.addWidget(self.txtEmail)

        #label 5
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(67, 67, 67);\n" "background-color: rgba(255,255,255,0);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)

        #password text box
        self.txtPW = QtWidgets.QLineEdit(Form)
        self.txtPW.setMinimumSize(QtCore.QSize(0, 30))
        self.txtPW.setStyleSheet("background-color: rgba(255, 255, 255,.6)")
        self.txtPW.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPW.setObjectName("txtPW")
        self.txtPW.setClearButtonEnabled(True)
        self.verticalLayout.addWidget(self.txtPW)

        #sign up button
        self.btnSignUp = QtWidgets.QPushButton(Form)
        self.btnSignUp.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.btnSignUp.setFont(font)
        self.btnSignUp.setAutoFillBackground(False)
        self.btnSignUp.setStyleSheet("color: rgb(255, 255, 255);\n" "background-color: rgb(109, 109, 109);")
        self.btnSignUp.setFlat(True)
        self.btnSignUp.setObjectName("btnSignUp")
        self.verticalLayout.addWidget(self.btnSignUp)
        # button click event for sign up
        self.btnSignUp.clicked.connect(self.signUp) 

        #exit button 
        self.btnEXIT = QtWidgets.QPushButton(Form)
        self.btnEXIT.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.btnEXIT.setFont(font)
        self.btnEXIT.setStyleSheet("color: rgb(109, 109, 109);\n" "background-color: rgb(255, 255, 255);")
        self.btnEXIT.setFlat(True)
        self.btnEXIT.setObjectName("btnEXIT")
        #exit button click event
        self.btnEXIT.clicked.connect(self.close) 
        self.verticalLayout.addWidget(self.btnEXIT)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        #Form controls
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    #setting texts for UI elements
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sign Up"))
        self.label.setText(_translate("Form", "Employee ID:"))
        self.label_2.setText(_translate("Form", "First Name:"))
        self.label_3.setText(_translate("Form", "Last Name:"))
        self.label_4.setText(_translate("Form", "E-mail:"))
        self.label_5.setText(_translate("Form", "Password"))
        self.btnSignUp.setText(_translate("Form", "Sign Up"))
        self.btnEXIT.setText(_translate("Form", "Exit"))

#main argument to launch the page
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = SignUpForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
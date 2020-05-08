from PyQt5 import QtCore, QtGui, QtWidgets
from g2_screen import Ui_MainWindow_g2
from p2_screen import Ui_MainWindow_p2

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.foto1 = QtWidgets.QLabel(self.centralwidget)
        self.foto1.setGeometry(QtCore.QRect(10, 40, 541, 351))
        self.foto1.setText("")
        self.foto1.setPixmap(QtGui.QPixmap("../test/108389_04.JPG"))
        self.foto1.setScaledContents(True)
        self.foto1.setObjectName("foto1")

        #en-ger button
        self.truck_2 = QtWidgets.QPushButton(self.centralwidget)
        self.truck_2.setGeometry(QtCore.QRect(100, 150, 150, 50))
        self.truck_2.setObjectName("truck_2")

        #ger-en button
        self.sky = QtWidgets.QPushButton(self.centralwidget)
        self.sky.setGeometry(QtCore.QRect(260, 150, 150, 50))
        self.sky.setObjectName("sky")
        
        #pic-ger button
        self.pic_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pic_1.setGeometry(QtCore.QRect(100, 225, 150, 50))
        self.pic_1.setObjectName("pic_1")

        #pic-en button
        self.pic_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pic_2.setGeometry(QtCore.QRect(260, 225, 150, 50))
        self.pic_2.setObjectName("pic_1")


        #exit button
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(200, 350, 151, 31))
        self.exit_button.setObjectName("sky")


        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(85, 25, 400, 91))
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(36)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.sky.clicked.connect(self.g2_scr_1)
        self.sky.clicked.connect(lambda:self.closescr(MainWindow))
        self.truck_2.clicked.connect(self.g2_scr_2)
        self.truck_2.clicked.connect(lambda:self.closescr(MainWindow))

        
        self.pic_1.clicked.connect(self.p2_scr_1)
        self.pic_1.clicked.connect(lambda:self.closescr(MainWindow))
        self.pic_2.clicked.connect(self.p2_scr_2)
        self.pic_2.clicked.connect(lambda:self.closescr(MainWindow))


        #0041close
        self.exit_button.clicked.connect(lambda:self.closescr(MainWindow))

    #0041close
    def closescr(self, MainWindow):
        MainWindow.hide()

    def g2_scr_1(self):
        self.MainWindow_g2 = QtWidgets.QMainWindow()
        self.message_g2 = 1 #se_deen_1
        self.ui = Ui_MainWindow_g2(self.message_g2) #se_deen_1
        self.ui.setupUi(self.MainWindow_g2)
        self.MainWindow_g2.show()

    def g2_scr_2(self):
        self.MainWindow_g2 = QtWidgets.QMainWindow()
        self.message_g2 = 0 #se_deen_1
        self.ui = Ui_MainWindow_g2(self.message_g2) #se_deen_1
        self.ui.setupUi(self.MainWindow_g2)
        self.MainWindow_g2.show()

    #connect with screen to enter number (pic-ger)
    def p2_scr_1(self):
        self.MainWindow_p2 = QtWidgets.QMainWindow()
        self.message_p2 = 1 #se_deen_1
        self.ui = Ui_MainWindow_p2(self.message_p2) #se_deen_1
        self.ui.setupUi(self.MainWindow_p2)
        self.MainWindow_p2.show()
        
    #connect with screen to enter number (pic-en)
    def p2_scr_2(self):
        self.MainWindow_p2 = QtWidgets.QMainWindow()
        self.message_p2 = 0 #se_deen_1
        self.ui = Ui_MainWindow_p2(self.message_p2) #se_deen_1
        self.ui.setupUi(self.MainWindow_p2)
        self.MainWindow_p2.show()
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chose Language"))
        self.truck_2.setText(_translate("MainWindow", "English - German"))  
        self.pic_1.setText(_translate("MainWindow", "Pic - English"))  
        self.pic_2.setText(_translate("MainWindow", "Pic - German"))  
        self.sky.setText(_translate("MainWindow", "German - English"))
        self.exit_button.setText(_translate("MainWindow", "Back"))
        self.label1.setText(_translate("MainWindow", "Choose language"))
"""
#can stay for testing. needs prbly to be taken out when called  
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
"""

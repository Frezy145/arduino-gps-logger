# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):

    """
        Class to design Arduino Uno GPS extraction User Interface with PyQt5.
    """

    def setupUi(self, MainWindow):

        # main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(824, 618)
        MainWindow.setAcceptDrops(False)

        # central widget 
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # title label
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(200, 20, 71, 31))
        self.titleLabel.setObjectName("titleLabel")

        # title light: green if arduino is connect 
        self.titleLight = QtWidgets.QLabel(self.centralwidget)
        self.titleLight.setGeometry(QtCore.QRect(280, 25, 15, 15))
        self.titleLight.setStyleSheet("QLabel {\n"
            "    background-color: red;  \n"
            "    border-radius: 10px;    \n"
            "    min-width: 20px;         \n"
            "    min-height: 20px;  \n"
            "}"
        )
        self.titleLight.setText("")
        self.titleLight.setIndent(2)
        self.titleLight.setObjectName("titleLight")

        # ready label
        self.readyLabel = QtWidgets.QLabel(self.centralwidget)
        self.readyLabel.setGeometry(QtCore.QRect(390, 20, 121, 31))
        self.readyLabel.setObjectName("readyLabel")

        # ready light: green if arduino is returning lat and long 
        self.readyLight = QtWidgets.QLabel(self.centralwidget)
        self.readyLight.setGeometry(QtCore.QRect(520, 25, 15, 15))
        self.readyLight.setStyleSheet("QLabel {\n"
            "    background-color: red;  \n"
            "    border-radius: 10px;    \n"
            "    min-width: 20px;         \n"
            "    min-height: 20px;  \n"
            "}"
        )
        self.readyLight.setText("")
        self.readyLight.setIndent(2)
        self.readyLight.setObjectName("readyLight")

        # Latitude label
        self.latitude = QtWidgets.QLabel(self.centralwidget)
        self.latitude.setGeometry(QtCore.QRect(170, 150, 55, 16))
        self.latitude.setObjectName("latitude")

        # LCD Number to display current Latitude
        self.lat = QtWidgets.QLCDNumber(self.centralwidget)
        self.lat.setGeometry(QtCore.QRect(150, 172, 231, 81))
        self.lat.setSmallDecimalPoint(True)
        self.lat.setDigitCount(15)
        self.lat.setObjectName("lat")

        # Longitude label
        self.longitude = QtWidgets.QLabel(self.centralwidget)
        self.longitude.setGeometry(QtCore.QRect(420, 150, 61, 16))
        self.longitude.setObjectName("longitude")
        
        # LCD Number to display current Longitude
        self.long = QtWidgets.QLCDNumber(self.centralwidget)
        self.long.setGeometry(QtCore.QRect(400, 170, 231, 81))
        self.long.setSmallDecimalPoint(True)
        self.long.setDigitCount(15)
        self.long.setObjectName("long")

        # Slider label : show the speed
        self.sliderLabel = QtWidgets.QLabel(self.centralwidget)
        self.sliderLabel.setGeometry(QtCore.QRect(745, 238, 30, 10))
        self.sliderLabel.setObjectName("sliderLabel")

        # Vertical slider to select recording speed : defaut 1s, high 10s
        self.slider = QtWidgets.QSlider(self.centralwidget)
        self.slider.setGeometry(QtCore.QRect(720, 90, 22, 160))
        self.slider.setOrientation(QtCore.Qt.Vertical)
        self.slider.setObjectName("slider")
        self.slider.setMinimum(1)
        self.slider.setMaximum (10)
        self.slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.slider.setTickInterval(1)
        self.slider.setSingleStep(1)

        # Text displayer : to display any text
        self.displayLabel = QtWidgets.QLabel(self.centralwidget)
        self.displayLabel.setGeometry(QtCore.QRect(170, 60, 450, 80))
        self.displayLabel.setObjectName("displayLabel")
        self.displayLabel.setStyleSheet("QLabel {\n"
            "    border-radius: 10px;    \n"
            "    color: blue;           \n"
            "}"
        )
        self.displayLabel.setAlignment(QtCore.Qt.AlignCenter) # alignment style 

        # save button to save data
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(450, 460, 93, 28))
        self.saveButton.setObjectName("saveButton")

        # start button: start, pause and continue recording
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(350, 460, 93, 28))
        self.startButton.setObjectName("startButtuon")

        # clear button: clear data and stop recording
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(550, 460, 93, 28))
        self.clearButton.setObjectName("clearButton")


        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(250, 460, 93, 28))
        self.stopButton.setObjectName("stopButton")

        self.restartButton = QtWidgets.QPushButton(self.centralwidget)
        self.restartButton.setGeometry(QtCore.QRect(150, 460, 93, 28))
        self.restartButton.setObjectName("restartButton")

        

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GPS ARDUINO"))
        self.titleLabel.setText(_translate("MainWindow", "ARDUINO :"))
        self.latitude.setText(_translate("MainWindow", "Latitude"))
        self.longitude.setText(_translate("MainWindow", "Longitude"))
        self.readyLabel.setText(_translate("MainWindow", "READY TO START :"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.restartButton.setText(_translate("MainWindow", "Restart"))
        self.sliderLabel.setText(_translate("MainWindow", "1s"))
        self.displayLabel.setText(_translate(
            "MainWindow", 
            "Welcome to GPS recording tool with ARDUINO. \n"
            "Click on \"Start\" to start."
        ))


# this is just for UI testing 
if __name__ == "__main__":
    print("UI testing")
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

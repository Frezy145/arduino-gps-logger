# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtWidgets

class Ui_Dialog(object):

    """
    Dialog window when saving recorded data.
    """

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(214, 258)

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(80, 130, 71, 81))
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")

        # Check Box for CSV file
        self.CSV = QtWidgets.QCheckBox(Dialog)
        self.CSV.setGeometry(QtCore.QRect(30, 30, 81, 20))
        self.CSV.setObjectName("CSV")

        # Check Box for EXCEL file
        self.Excel = QtWidgets.QCheckBox(Dialog)
        self.Excel.setGeometry(QtCore.QRect(30, 60, 81, 20))
        self.Excel.setObjectName("Excel")

        # Check Box for Shapefile 
        self.Shp = QtWidgets.QCheckBox(Dialog)
        self.Shp.setGeometry(QtCore.QRect(30, 90, 81, 20))
        self.Shp.setObjectName("Shp")


        # ESPG Label 
        self.espgLabel = QtWidgets.QLabel(Dialog)
        self.espgLabel.setGeometry(QtCore.QRect(120, 40, 81, 20))
        self.espgLabel.setObjectName("espgLabel")
        self.espgLabel.setText("ESPG")
        self.espgLabel.setVisible(False)

        # ESPG Input Line
        self.espgInput = QtWidgets.QLineEdit(Dialog)
        self.espgInput.setGeometry(QtCore.QRect(120, 70, 81, 20))
        self.espgInput.setObjectName("espgInput")
        self.espgInput.setText("4326")
        self.espgInput.setVisible(False)

        # retranslation 
        self.retranslateUi(Dialog)

        # buttons connections
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.Shp.toggled.connect(self.set_epsg) 
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def set_epsg(self, checked):

        self.espgInput.setVisible(checked)
        self.espgLabel.setVisible(checked)

    def retranslateUi(self, Dialog):
        """retranslation method."""
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Types"))
        self.CSV.setText(_translate("Dialog", "CSV"))
        self.Excel.setText(_translate("Dialog", "XLSX"))
        self.Shp.setText(_translate("Dialog", "SHP"))


# Just for testing 
if __name__ == "__main__":

    print("Save file Dialog UI tiesting ...")
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

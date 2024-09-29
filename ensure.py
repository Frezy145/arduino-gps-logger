
# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Ensure(object):
    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(214, 258)

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(80, 130, 71, 81))
        self.buttonBox.setAutoFillBackground(False)

        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")

        self.dialogLabel = QtWidgets.QLabel(Dialog)
        self.dialogLabel.setGeometry(QtCore.QRect(30, 30, 150, 20))
        self.dialogLabel.setObjectName("dialogLabel")
        self.dialogLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) 
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Types"))
        self.dialogLabel.setText(_translate("Dialog", "This will clear all data."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Ensure()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

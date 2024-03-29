# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Project/UIFiles/AppPageUI_CompoundInterest.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ModulePage(object):
    def setupUi(self, ModulePage):
        ModulePage.setObjectName("ModulePage")
        ModulePage.resize(305, 381)
        font = QtGui.QFont()
        font.setPointSize(12)
        ModulePage.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(ModulePage)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(ModulePage)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.resetButton = QtWidgets.QPushButton(ModulePage)
        self.resetButton.setObjectName("resetButton")
        self.gridLayout.addWidget(self.resetButton, 6, 0, 1, 1)
        self.calculateButton = QtWidgets.QPushButton(ModulePage)
        self.calculateButton.setObjectName("calculateButton")
        self.gridLayout.addWidget(self.calculateButton, 6, 1, 1, 1)
        self.input_2 = QtWidgets.QLineEdit(ModulePage)
        self.input_2.setObjectName("input_2")
        self.gridLayout.addWidget(self.input_2, 1, 1, 1, 1)
        self.input_1 = QtWidgets.QLineEdit(ModulePage)
        self.input_1.setObjectName("input_1")
        self.gridLayout.addWidget(self.input_1, 0, 1, 1, 1)
        self.input_3 = QtWidgets.QLineEdit(ModulePage)
        self.input_3.setObjectName("input_3")
        self.gridLayout.addWidget(self.input_3, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(ModulePage)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(ModulePage)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.input_4 = QtWidgets.QLineEdit(ModulePage)
        self.input_4.setObjectName("input_4")
        self.gridLayout.addWidget(self.input_4, 3, 1, 1, 1)
        self.label_1 = QtWidgets.QLabel(ModulePage)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.resultLabel = QtWidgets.QLabel(ModulePage)
        self.resultLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.resultLabel.setObjectName("resultLabel")
        self.gridLayout.addWidget(self.resultLabel, 5, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)

        self.retranslateUi(ModulePage)
        QtCore.QMetaObject.connectSlotsByName(ModulePage)

    def retranslateUi(self, ModulePage):
        _translate = QtCore.QCoreApplication.translate
        ModulePage.setWindowTitle(_translate("ModulePage", "Form"))
        self.label_3.setText(_translate("ModulePage", "Periods (t)"))
        self.resetButton.setText(_translate("ModulePage", "Reset"))
        self.calculateButton.setText(_translate("ModulePage", "Calculate"))
        self.label_2.setText(_translate("ModulePage", "Rate (%)"))
        self.label_4.setText(_translate("ModulePage", "Compounds per period (n)"))
        self.label_1.setText(_translate("ModulePage", "Principal ($)"))
        self.resultLabel.setText(_translate("ModulePage", "Your Result"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ModulePage = QtWidgets.QWidget()
    ui = Ui_ModulePage()
    ui.setupUi(ModulePage)
    ModulePage.show()
    sys.exit(app.exec_())

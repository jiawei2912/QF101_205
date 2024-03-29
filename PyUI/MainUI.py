# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Project/UIFiles/MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(300, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(300, 450))
        font = QtGui.QFont()
        font.setPointSize(16)
        MainWindow.setFont(font)
        MainWindow.setWindowOpacity(4.0)
        self.mainWidget = QtWidgets.QWidget(MainWindow)
        self.mainWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainWidget.sizePolicy().hasHeightForWidth())
        self.mainWidget.setSizePolicy(sizePolicy)
        self.mainWidget.setMinimumSize(QtCore.QSize(300, 450))
        self.mainWidget.setObjectName("mainWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setSpacing(6)
        self.mainLayout.setObjectName("mainLayout")
        self.headerWidget = QtWidgets.QWidget(self.mainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.headerWidget.sizePolicy().hasHeightForWidth())
        self.headerWidget.setSizePolicy(sizePolicy)
        self.headerWidget.setMinimumSize(QtCore.QSize(0, 40))
        self.headerWidget.setMaximumSize(QtCore.QSize(16777215, 35))
        self.headerWidget.setObjectName("headerWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.headerWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.header = QtWidgets.QHBoxLayout()
        self.header.setContentsMargins(0, 0, 0, 0)
        self.header.setSpacing(0)
        self.header.setObjectName("header")
        self.backButton = QtWidgets.QPushButton(self.headerWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy)
        self.backButton.setMinimumSize(QtCore.QSize(40, 0))
        self.backButton.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setKerning(True)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("background-color:#f8f8ff; \n"
"border: none;\n"
"")
        self.backButton.setFlat(False)
        self.backButton.setObjectName("backButton")
        self.header.addWidget(self.backButton)
        self.header_separator = QtWidgets.QFrame(self.headerWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header_separator.sizePolicy().hasHeightForWidth())
        self.header_separator.setSizePolicy(sizePolicy)
        self.header_separator.setMaximumSize(QtCore.QSize(16777215, 30))
        self.header_separator.setStyleSheet("color: black;")
        self.header_separator.setLineWidth(1)
        self.header_separator.setFrameShape(QtWidgets.QFrame.VLine)
        self.header_separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.header_separator.setObjectName("header_separator")
        self.header.addWidget(self.header_separator)
        self.headerLabel = QtWidgets.QLabel(self.headerWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.headerLabel.sizePolicy().hasHeightForWidth())
        self.headerLabel.setSizePolicy(sizePolicy)
        self.headerLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.headerLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.headerLabel.setFont(font)
        self.headerLabel.setStyleSheet("background-color: #f8f8ff; color: black;")
        self.headerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.headerLabel.setObjectName("headerLabel")
        self.header.addWidget(self.headerLabel)
        self.horizontalLayout.addLayout(self.header)
        self.mainLayout.addWidget(self.headerWidget)
        self.line_2 = QtWidgets.QFrame(self.mainWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.mainLayout.addWidget(self.line_2)
        self.bodyStackedWidget = QtWidgets.QStackedWidget(self.mainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bodyStackedWidget.sizePolicy().hasHeightForWidth())
        self.bodyStackedWidget.setSizePolicy(sizePolicy)
        self.bodyStackedWidget.setMinimumSize(QtCore.QSize(300, 300))
        self.bodyStackedWidget.setObjectName("bodyStackedWidget")
        self.landingPage = QtWidgets.QWidget()
        self.landingPage.setObjectName("landingPage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.landingPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.landingPageVLayout = QtWidgets.QVBoxLayout()
        self.landingPageVLayout.setObjectName("landingPageVLayout")
        self.verticalLayout_2.addLayout(self.landingPageVLayout)
        self.bodyStackedWidget.addWidget(self.landingPage)
        self.mainLayout.addWidget(self.bodyStackedWidget)
        self.verticalLayout.addLayout(self.mainLayout)
        MainWindow.setCentralWidget(self.mainWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Learning Cryptopgrahy"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.headerLabel.setText(_translate("MainWindow", "Main Menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

from __future__ import annotations
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic

from PyUI import MainUI, LandingPageButton
from AppModules import ExampleModule, SimpleInterest, CompoundInterest

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = MainUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self._setUpButtonCallbacks()
        self._loadAppModules()

    def _setUpButtonCallbacks(self):
        self.ui.backButton.clicked.connect(lambda : self.navigateTo(0))
        self.ui.backButton.setVisible(False)

    # Todo (if bothered enough): Make this dynamically load all modules in the AppModules folder
    def _loadAppModules(self):
        moduleWidgets = []
        moduleWidgets.append(ExampleModule.ExampleModule())
        moduleWidgets.append(SimpleInterest.SimpleInterestCalculator())
        moduleWidgets.append(CompoundInterest.CompoundInterestCalculator())
        for i, moduleWidget in enumerate(moduleWidgets):
            self.ui.bodyStackedWidget.addWidget(moduleWidget)
            LandingPagePushButton(self, moduleWidget.title, i+1)

    def navigateTo(self, stackedWidgetIndex:int, newHeaderLabel:str = "Module"):
        self.ui.bodyStackedWidget.setCurrentIndex(stackedWidgetIndex)
        if stackedWidgetIndex == 0:
            self.ui.backButton.setVisible(False)
            self.ui.headerLabel.setText("Main Menu")
        else:
            self.ui.backButton.setVisible(True)
            self.ui.headerLabel.setText(newHeaderLabel)

class LandingPagePushButton(QtWidgets.QWidget):
    def __init__(self, mainWindow:MainWindow, appName:str, appIndex:int) -> None:
        super().__init__()
        mainWindow.ui.landingPageVLayout.addWidget(self)
        self.ui = LandingPageButton.Ui_LandingPageButton()
        self.ui.setupUi(self)
        self.ui.appButton1.setText(appName)
        self.ui.appButton1.clicked.connect(lambda : mainWindow.navigateTo(appIndex, appName))


def main():
    qApp = QtWidgets.QApplication(sys.argv)
    qWin = MainWindow()
    qWin.show()
    sys.exit(qApp.exec_())
    pass

if __name__ == '__main__':
    main()
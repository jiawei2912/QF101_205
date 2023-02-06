from __future__ import annotations
import sys, inspect
from PyQt5 import QtCore, QtGui, QtWidgets, uic

from PyUI import MainUI, LandingPageButton
import AppModules
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

    # ToDo: Add error handling
    def _loadAppModules(self):
        sub_modules = inspect.getmembers(AppModules, inspect.ismodule)
        sub_modules = [sub_module[1] for sub_module in sub_modules]
        moduleWidgetClasses = []
        for sub_module in sub_modules:
            classes = inspect.getmembers(sub_module, inspect.isclass)
            classes = [cls[1] for cls in classes]
            moduleWidgetClasses.extend(list(filter(lambda cls: issubclass(cls, QtWidgets.QWidget), classes)))
        for i, moduleWidgetClass in enumerate(moduleWidgetClasses):
            moduleWidget = moduleWidgetClass()
            self.ui.bodyStackedWidget.addWidget(moduleWidget)
            LandingPagePushButton(self, moduleWidget.title, i+1)

    # Old (can delete if the method above does not cause any problems)
    def _loadAppModules_OLD(self):
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
from __future__ import annotations
import sys, inspect
from PyQt5 import QtCore, QtGui, QtWidgets

from PyUI import MainUI, LandingPageButton
import AppModules

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = MainUI.Ui_MainWindow()
        self.ui.setupUi(self)
        #self.ui.landingPageVLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop)
        self.ui.landingPageVLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self._setUpButtonCallbacks()
        self._loadAppModules()

        # jank ass resizing
        largest_width = 0
        for lppButtonIdx in range(self.ui.landingPageVLayout.count()):
            lppButton = self.ui.landingPageVLayout.itemAt(lppButtonIdx).widget()
            largest_width = max(largest_width, lppButton.width())
        for lppButtonIdx in range(self.ui.landingPageVLayout.count()):
            lppButton = self.ui.landingPageVLayout.itemAt(lppButtonIdx).widget()
            lppButton.resize(largest_width, lppButton.height())
            lppButton.ui.appButton1.resize(largest_width, lppButton.height())
        # Slightly dangerous, as a module with a too long name might result in a window that
        # is too large and which cannot be shurnk
        self.setMinimumWidth(int(largest_width*1.1))
            
        
    # def resizeEvent(self, event:QtGui.QResizeEvent) -> None:
    #     old_size = event.oldSize()
    #     new_size = QtCore.QSize(self.geometry().width(), self.geometry().height())
    #     print(old_size, new_size)
    #     QtWidgets.QMainWindow.resizeEvent(self, event)

    def _setUpButtonCallbacks(self):
        self.ui.backButton.clicked.connect(lambda : self.navigateTo(0))
        self.ui.backButton.setVisible(False)
        self.ui.header_separator.setVisible(False)

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
            print(moduleWidget.title, 'loaded')

    def navigateTo(self, stackedWidgetIndex:int, newHeaderLabel:str = "Module"):
        self.ui.bodyStackedWidget.setCurrentIndex(stackedWidgetIndex)
        if stackedWidgetIndex == 0:
            self.ui.backButton.setVisible(False)
            self.ui.headerLabel.setText("Main Menu")
            self.ui.header_separator.setVisible(False)
        else:
            self.ui.backButton.setVisible(True)
            self.ui.headerLabel.setText(newHeaderLabel)
            self.ui.header_separator.setVisible(True)

# Consider adding either a maximum length ot the appName or enforcing wordwrap past a certain length
class LandingPagePushButton(QtWidgets.QWidget):
    def __init__(self, mainWindow:MainWindow, appName:str, appIndex:int) -> None:
        super().__init__()
        mainWindow.ui.landingPageVLayout.addWidget(self, stretch=1)
        self.ui = LandingPageButton.Ui_LandingPageButton()
        self.ui.setupUi(self)
        self.ui.appButton1.setText(appName)
        self.ui.appButton1.clicked.connect(lambda : mainWindow.navigateTo(appIndex, appName))
        self.ui.appButton1.adjustSize()
        self.adjustSize()
    # Needed for the widgets to appear; 
    # supposedly because the main widget does not have an activated layout
    def sizeHint(self):
        #return QtCore.QSize(int(self.parent().width()), self.ui.appButton1.height())
        return self.ui.appButton1.size()


def main():
    qApp = QtWidgets.QApplication(sys.argv)
    qWin = MainWindow()
    qWin.adjustSize()
    qWin.show()
    sys.exit(qApp.exec_())
    

if __name__ == '__main__':
    main()
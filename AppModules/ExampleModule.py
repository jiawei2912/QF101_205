from __future__ import annotations
from PyQt5 import QtWidgets

from PyUI import AppPageUI

# Each AppModule needs to have:
#   self.title: display name of the module
class ExampleModule(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.title:str = "Example Module"
        self.ui = AppPageUI.Ui_ModulePage()
        self.ui.setupUi(self)
        self._setUpButtonCallbacks()
    
    def _setUpButtonCallbacks(self):
        self.ui.calculateButton.clicked.connect(self._calculateButtonClickedCallback)
        self.ui.resetButton.clicked.connect(self._resetButtonClickedCallback)
        pass

    def _calculateButtonClickedCallback(self):
        a:float
        b:float
        try:
            a = float(self.ui.input_1.text())
            b = float(self.ui.input_2.text())
            self.ui.resultLabel.setText(str(a+b))
        except:
            self.ui.resultLabel.setText("Error!")
        pass

    def _resetButtonClickedCallback(self):
        self.ui.input_1.setText("")
        self.ui.input_2.setText("")
        self.ui.resultLabel.setText("Your Result")
    pass
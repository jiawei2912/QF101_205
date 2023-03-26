from __future__ import annotations
from PyQt5 import QtWidgets

from PyUI import AppPageUI_CompoundInterest

# Each AppModule needs to have:
#   self.title: display name of the module
class CompoundInterestCalculator(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.title:str = "Compound Interest"
        self.ui = AppPageUI_CompoundInterest.Ui_ModulePage()
        self.ui.setupUi(self)
        self._setUpButtonCallbacks()
    
    def _setUpButtonCallbacks(self):
        self.ui.calculateButton.clicked.connect(self._calculateButtonClickedCallback)
        self.ui.resetButton.clicked.connect(self._resetButtonClickedCallback)
        pass

    def _calculateButtonClickedCallback(self):
        try:
            principal = float(self.ui.input_1.text())
            rate = float(self.ui.input_2.text())
            numPeriods = int(self.ui.input_3.text())
            numCompoundsPerPeriod = int(self.ui.input_4.text())
            finalPrincipal = principal*(1+(rate/numPeriods))**(numCompoundsPerPeriod*numPeriods)

            totalInterest = round(finalPrincipal-principal, 2)
            finalPrincipal = round(finalPrincipal, 2)
            outputStr:str = "Interest: $" + str(totalInterest)\
                            + "\nTotal: $" + str(finalPrincipal)
            self.ui.resultLabel.setText(outputStr)
        except Exception as e:
            print(e)
            self.ui.resultLabel.setText("Error!")
        pass

    def _resetButtonClickedCallback(self):
        self.ui.input_1.setText("")
        self.ui.input_2.setText("")
        self.ui.input_3.setText("")
        self.ui.input_4.setText("")
        self.ui.resultLabel.setText("Your Result")
    pass
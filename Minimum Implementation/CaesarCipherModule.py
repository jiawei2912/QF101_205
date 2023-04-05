from __future__ import annotations
from typing import List
from PyQt5 import QtWidgets

from PyUI import CaesarCipherUI

# Todo: 1) Remove the use of the Class and the GUI
#       2) You can use functions
#       3) Simplify this into a standalone file

# Each AppModule needs to have:
#   title: display name of the module
#   order: ordering priority; lower numbers will be displayed higher up
class CaesarCipherModule(QtWidgets.QWidget):
    title:str = "Caesar Cipher"
    order:int = 10
    def __init__(self) -> None:
        super().__init__()
        self.ui = CaesarCipherUI.Ui_ModulePage()
        self.ui.setupUi(self)
        self._setUpButtonCallbacks()
        self._resetButtonClickedCallback()
    
    def _setUpButtonCallbacks(self):
        self.ui.encodeButton.clicked.connect(lambda: self._cipher())
        self.ui.decodeButton.clicked.connect(lambda: self._cipher(1))
        self.ui.resetButton.clicked.connect(self._resetButtonClickedCallback)
        pass

    # Todo: 1) Make a CLI copy of this function in 'Improved Implementation' that 'teaches' List
    #       2) Write a simplified CLI version of this in 'Minimum Implementation' that illustrates the use of a List
    
    # 0 for encode, 1 for decode
    def _cipher(self, mode=0):
        # Input Validation
        alphabet:str = self.ui.input_alphabet.text()
        if not len(alphabet) > 0:
            self.ui.output_ciphertext.setText("Error. Please provide an alphabet.")
            return
        if len(set(alphabet)) != len(alphabet):
            self.ui.output_ciphertext.setText("Error. Letters in the alphabet must be unique.")
            return
        shift = self.ui.input_shift.text()
        try:
            int_shift = int(shift)
            if int_shift != float(shift):
                raise ValueError
        except ValueError:
            self.ui.output_ciphertext.setText("Error. Please provide an integer for shift.")
            return
        shift = int(shift)

        # Mode Switching
        if mode == 1:
            shift = -shift

        # The Validated Parameters
        alphabet:List[str] = list(alphabet)
        shift:int = shift%len(alphabet)

        # Ciphering...
        plain_text = self.ui.input_plaintext.toPlainText()
        cipher_text = []
        for char in plain_text:
            if char in alphabet:
                cipher_text.append(alphabet[(alphabet.index(char)+shift)%len(alphabet)])
            else:
                cipher_text.append(char)
        self.ui.output_ciphertext.setText(''.join(cipher_text))

    def _resetButtonClickedCallback(self):
        self.ui.input_alphabet.setText('abcdefghijklmnopqrstuvwxyz')
        self.ui.input_shift.setText('7')
        self.ui.input_plaintext.clear()
        self.ui.output_ciphertext.clear()
    pass


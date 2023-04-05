from __future__ import annotations
from typing import List
from PyQt5 import QtWidgets
from math import gcd

from PyUI import AffineCipherUI

# Each AppModule needs to have:
#   title: display name of the module
#   order: ordering priority; lower numbers will be displayed higher up
class AffineCipherModule(QtWidgets.QWidget):
    title:str = "Affine Cipher"
    order:int = 40
    def __init__(self) -> None:
        super().__init__()
        self.ui = AffineCipherUI.Ui_ModulePage()
        self.ui.setupUi(self)
        self._setUpButtonCallbacks()
        self._resetButtonClickedCallback()
    
    def _setUpButtonCallbacks(self):
        self.ui.encodeButton.clicked.connect(lambda: self._cipher())
        self.ui.decodeButton.clicked.connect(lambda: self._cipher(1))
        self.ui.resetButton.clicked.connect(self._resetButtonClickedCallback)
        pass

    # Todo: 1) Make a CLI copy of this in 'Improved Implementation' that 'teaches' basic arithemtic operators
    #       2) Write a simplified CLI version of this in 'Minimum Implementation' that illustrates the use of arithmetic operators

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
        key_a = self.ui.input_a.text()
        key_b = self.ui.input_b.text()
        for key in key_a, key_b:
            try:
                int_key = int(key)
                if int_key != float(key):
                    raise ValueError
            except ValueError:
                self.ui.output_ciphertext.setText("Error. Please provide integers for the keys.")
                return
        key_a = int(key_a)
        if gcd(key_a, len(alphabet)) > 1:
            self.ui.output_ciphertext.setText("Error. The key_a and the length of the alphabet provided must be coprime.")
            return

        # The Validated Parameters
        alphabet:List[str] = list(alphabet)
        key_a:int = int(key_a)
        key_b:int = int(key_b)

        # Ciphering...
        plain_text = self.ui.input_plaintext.toPlainText()
        cipher_text = []
        for char in plain_text:
            if char in alphabet:
                if mode == 0:
                    cipher_text.append(alphabet[(key_a*alphabet.index(char)+key_b)%len(alphabet)])
                else:
                    modinv = pow(key_a, -1, len(alphabet)) #Note: requires Python 3.8+
                    cipher_text.append(alphabet[(modinv*(alphabet.index(char)-key_b))%len(alphabet)])

            else:
                cipher_text.append(char)
        self.ui.output_ciphertext.setText(''.join(cipher_text))

    def _resetButtonClickedCallback(self):
        self.ui.input_alphabet.setText('abcdefghijklmnopqrstuvwxyz')
        self.ui.input_a.setText('7')
        self.ui.input_b.setText('5')
        self.ui.input_plaintext.clear()
        self.ui.output_ciphertext.clear()
    pass


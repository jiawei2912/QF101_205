from __future__ import annotations
from typing import List
from PyQt5 import QtWidgets
from PyUI import XOREncryptionUI

# Todo: 1) Create a heavily simplified version of this module 
#       2) This implementation should have a 'problem' that is resolved
#           by the 'Improved Implementation'

# Each AppModule needs to have:
#   title: display name of the module
#   order: ordering priority; lower numbers will be displayed higher up
class XOREncryptionModule(QtWidgets.QWidget):
    title:str = "XOR Encryption"
    order:int = 60
    def __init__(self) -> None:
        super().__init__()
        self.ui = XOREncryptionUI.Ui_ModulePage()
        self.ui.setupUi(self)
        self._setUpButtonCallbacks()
        self._setUpRadioButtons()
        self._resetButtonClickedCallback()

    def _setUpButtonCallbacks(self):
        self.ui.encodeButton.clicked.connect(lambda: self._cipher())
        self.ui.resetButton.clicked.connect(self._resetButtonClickedCallback)
        pass

    def _setUpRadioButtons(self):
        self.mode_rb_group = QtWidgets.QButtonGroup(self)
        self.mode_rb_group.addButton(self.ui.radioButton_Binary)
        self.mode_rb_group.addButton(self.ui.radioButton_ASCII)

    # Todo: 1) Make a CLI copy of this in 'Improved Implementation' that 'teaches' bitwise operators
    #       2) Write a simplified CLI version of this in 'Minimum Implementation' that illustrates the use of bitwise operators

    # 0 for encode, 1 for decode
    def _cipher(self):
        # Input Validation
        key = self.ui.input_key.text()
        if not len(key) > 0:
            self.ui.output_ciphertext.setText("Error. Please provide a key.")
            return
        if self.ui.radioButton_Binary.isChecked():
            for char in set(key).union(set(self.ui.input_plaintext.toPlainText())):
                if not char in ['0','1']:
                    self.ui.output_ciphertext.setText("Error. In binary mode, the key and input must be binary.")
                    return
        else:
            for char in set(key).union(set(self.ui.input_plaintext.toPlainText())):
                if not ord(char) < 128:
                    self.ui.output_ciphertext.setText("Error. In binary mode, the key and input must be binary.")
                    return

        # The Validated Parameters
        key:List[str] = list(key)

        # Ciphering...
        plain_text = self.ui.input_plaintext.toPlainText()
        cipher_text = []
        key_idx = 0
        for char in plain_text:
            if self.ui.radioButton_ASCII.isChecked():
                cipher_text.append(chr(ord(char)^ord(key[key_idx])))
            else:
                cipher_text.append('0' if char == key[key_idx] else '1')
            key_idx = (key_idx+1)%len(key)
        self.ui.output_ciphertext.setText(''.join(cipher_text))

    def _resetButtonClickedCallback(self):
        self.ui.radioButton_ASCII.setChecked(True)
        self.ui.input_key.setText('QF205ComputingTechnology')
        self.ui.input_plaintext.clear()
        self.ui.output_ciphertext.clear()
    pass


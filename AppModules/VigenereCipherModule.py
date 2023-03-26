from __future__ import annotations
from typing import List
from PyQt5 import QtWidgets

from PyUI import VigenereCipherUI

# Each AppModule needs to have:
#   self.title: display name of the module
#   self.order: ordering priority; lower numbers will be displayed higher up
class VigenereCipherModule(QtWidgets.QWidget):
    title:str = "Vigenere Cipher"
    order:int = 30
    def __init__(self) -> None:
        super().__init__()
        self.ui = VigenereCipherUI.Ui_ModulePage()
        self.ui.setupUi(self)
        self._setUpButtonCallbacks()
        self._resetButtonClickedCallback()
    
    def _setUpButtonCallbacks(self):
        self.ui.encodeButton.clicked.connect(lambda: self._cipher())
        self.ui.decodeButton.clicked.connect(lambda: self._cipher(1))
        self.ui.resetButton.clicked.connect(self._resetButtonClickedCallback)
        pass

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
        key:str = self.ui.input_key.text()
        if not len(key) > 0:
            self.ui.output_ciphertext.setText("Error. Please provide a key.")
            return
        for char in key:
            if not char in alphabet:
                self.ui.output_ciphertext.setText("Error. Letters in the key must exist in the alphabet.")
                return

        # The Validated Parameters
        alphabet:List[str] = list(alphabet)
        key:List[str] = list(key)

        # plaintext letter coresponds to row
        # key letter corresponds to column
        # Ciphering...
        plain_text = self.ui.input_plaintext.toPlainText()
        cipher_text = []
        key_idx = 0
        for i in range(len(plain_text)):
            char = plain_text[i]
            key_char = key[key_idx%len(key)]
            if char in alphabet:
                if mode == 0:
                    cipher_text.append(alphabet[(alphabet.index(char)+alphabet.index(key_char))%len(alphabet)])
                else:
                    # to decode, find where you are in the column and minus by idx of key_char in alphabet
                    cipher_text.append(alphabet[(alphabet.index(char)-alphabet.index(key_char))])
                key_idx+=1
            else:
                cipher_text.append(char)
        self.ui.output_ciphertext.setText(''.join(cipher_text))

    def _resetButtonClickedCallback(self):
        self.ui.input_alphabet.setText('abcdefghijklmnopqrstuvwxyz')
        self.ui.input_key.setText('computingtechnologies')
        self.ui.input_plaintext.clear()
        self.ui.output_ciphertext.clear()
    pass


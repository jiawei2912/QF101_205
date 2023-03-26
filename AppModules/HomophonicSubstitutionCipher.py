from __future__ import annotations
from typing import List
from PyQt5 import QtWidgets

from PyUI import HomophonicSubstitutionCipherUI

# Each AppModule needs to have:
#   self.title: display name of the module
#   self.order: ordering priority; lower numbers will be displayed higher up
class HomophonicSubstitutionCipherModule(QtWidgets.QWidget):
    title:str = "Homophonic Substitution"
    order:int = 20
    def __init__(self) -> None:
        super().__init__()
        self.ui = HomophonicSubstitutionCipherUI.Ui_ModulePage()
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
        pt_alphabet:str = self.ui.input_plaintext_alphabet.text()
        ct_alphabet:str = self.ui.input_ciphertext_alphabet.text()
        if not len(pt_alphabet) > 0 or not len(ct_alphabet) > 0:
            self.ui.output_ciphertext.setText("Error. Please provide plaintext and ciphertext alphabets.")
            return
        if len(pt_alphabet) != len(ct_alphabet):
            self.ui.output_ciphertext.setText("Error. The two alphabets must of of equal length.")
            return
        if len(set(pt_alphabet)) != len(pt_alphabet) or len(set(ct_alphabet)) != len(ct_alphabet):
            self.ui.output_ciphertext.setText("Error. Letters in the provided alphabets must be unique.")
            return


        # Mode Switching
        if mode == 1:
            pt_alphabet, ct_alphabet = ct_alphabet, pt_alphabet

        # The Validated Parameters
        pt_alphabet:List[str] = list(pt_alphabet)
        ct_alphabet:List[str] = list(ct_alphabet)

        # Ciphering...
        plain_text = self.ui.input_plaintext.toPlainText()
        cipher_text = []
        for char in plain_text:
            if char in pt_alphabet:
                cipher_text.append(ct_alphabet[(pt_alphabet.index(char))])
            else:
                cipher_text.append(char)
        self.ui.output_ciphertext.setText(''.join(cipher_text))

    def _resetButtonClickedCallback(self):
        self.ui.input_plaintext_alphabet.setText('abcdefghijklmnopqrstuvwxyz')
        self.ui.input_ciphertext_alphabet.setText('zyxwvutsrqponmlkjihgfedcba')
        self.ui.input_plaintext.clear()
        self.ui.output_ciphertext.clear()
    pass


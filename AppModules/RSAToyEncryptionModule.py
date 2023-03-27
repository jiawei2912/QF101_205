from __future__ import annotations
from typing import List
from PyQt5 import QtWidgets
import random
from PyUI import RSAToyEncryptionUI
from math import gcd

# <><> Utility Function <><>
def _isPrime(n):
    if n == 2 or n == 3:
        return True
    if n%2 == 0 or n < 2:
        return False
    # Worst case scenario: n = n^0.5 X n^0.5 => No need to check beyond sqrt
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False
    return True


# Each AppModule needs to have:
#   title: display name of the module
#   order: ordering priority; lower numbers will be displayed higher up
class RSAToyEncryptionModule(QtWidgets.QWidget):
    title:str = "RSA Encryption (Toy)"
    order:int = 70
    min_pq:int = 100
    max_pq:int = 10_000
    primes:List[int] = [i for i in range(min_pq, max_pq+1) if _isPrime(i)]
    min_n:int = 10000
    max_n:int = 1_000_000

    def __init__(self) -> None:
        super().__init__()
        self.ui = RSAToyEncryptionUI.Ui_ModulePage()
        self.ui.setupUi(self)
        self._setUpButtonCallbacks()
        self._resetButtonClickedCallback()
    
    def _setUpButtonCallbacks(self):
        self.ui.encodeButton.clicked.connect(lambda: self._cipher())
        self.ui.decodeButton.clicked.connect(lambda: self._cipher(1))
        self.ui.resetButton.clicked.connect(self._resetButtonClickedCallback)
        self.ui.generateKeyPairButton.clicked.connect(self._generate_rsa_key_pair)
        # textChanged is emitted whenever the text changes
        # textEdited is emitted only when its edited by the user using keyboard/mouse
        self.ui.input_n_1.textEdited.connect(lambda: self.ui.input_n_2.setText(self.ui.input_n_1.text()))
        self.ui.input_n_2.textEdited.connect(lambda: self.ui.input_n_1.setText(self.ui.input_n_2.text()))
        
        pass

    # Realistically, this only needs to be greater than 128
    # since I'm only allowing ASCII. However, this default
    # range allows a greater variety of keys.
    def _generate_rsa_key_pair(self):
        # Draw 2 random primes
        p = q = -1
        while p == q:
            p, q = random.choices(RSAToyEncryptionModule.primes, k=2)
            if p*q < self.min_n or p*q > self.max_n:
                p = q = -1
        # Calculate n, e, and d
        n = p*q
        phi = (p-1)*(q-1)
        e = -1
        for i in range(2, n):
            if gcd(i, phi) == 1:
                e = i
                break
        d = -1
        for i in range(2, n):
            if i*e % phi == 1:
                d = i
                break
        # Output to UI
        self.ui.input_n_1.setText(str(n))
        self.ui.input_n_2.setText(str(n))
        self.ui.input_e.setText(str(e))
        self.ui.input_d.setText(str(d))

    # 0 for encode, 1 for decode
    def _cipher(self, mode=0):
        # Input Validation
        inputs = [self.ui.input_n_1.text(), self.ui.input_e.text(), self.ui.input_d.text()]
        errText = "Error. Please provide integers only for n and e."
        if mode == 0: #encrypt
            inputs.pop(2)
        elif mode == 1: #decrypt
            inputs.pop(1)
            errText = "Error. Please provide integers only for n and d."
        for input in inputs:
            try:
                if int(input) != float(input):
                    raise ValueError
            except ValueError:
                self.ui.output_ciphertext.setText(errText)
                return
        for char in self.ui.input_plaintext.toPlainText():
            if ord(char) > 128:
                self.ui.output_ciphertext.setText('Error! This implementation only accepts ASCII-characters in its input.')
                return
        if mode == 1:
            for char in self.ui.input_plaintext.toPlainText().split(' '):
                try:
                    int(char, 16)
                except ValueError:
                    self.ui.output_ciphertext.setText('Error! The input should be hexadecimal.')
                    return

        # The Validated Parameters
        n = int(self.ui.input_n_1.text())
        e = int(self.ui.input_e.text())
        d = int(self.ui.input_d.text())

        # Ciphering...
        plain_text = self.ui.input_plaintext.toPlainText()
        cipher_text = []
        if mode == 0:
            for char in plain_text:
                cipher_hex = hex((ord(char)**e)%n)
                cipher_text.append(str(cipher_hex)[2:])       
            self.ui.output_ciphertext.setText(' '.join(cipher_text))    
        else:
            for char in plain_text.split(' '):
                plain_dec = (int(char, 16)**d)%n
                cipher_text.append(chr(plain_dec))
            self.ui.output_ciphertext.setText(''.join(cipher_text))  
        

    def _resetButtonClickedCallback(self):
        self.ui.input_e.clear()
        self.ui.input_d.clear()      
        self.ui.input_n_1.clear()
        self.ui.input_n_2.clear()  
        self.ui.input_plaintext.clear()
        self.ui.output_ciphertext.clear()



from __future__ import annotations
from typing import List
from PyQt5 import QtWidgets

from PyUI import MorseCodeUI

# Todo: 1) Remove the use of the Class and the GUI
#       2) You can use functions
#       3) Simplify this into a standalone file

# Each AppModule needs to have:
#   self.title: display name of the module
#   self.order: ordering priority; lower numbers will be displayed higher up
class MorseCodeModule(QtWidgets.QWidget):
    title:str = "Morse Code"
    order:int = 50
    def __init__(self) -> None:
        super().__init__()
        self.ui = MorseCodeUI.Ui_ModulePage()
        self.ui.setupUi(self)
        self._setUpButtonCallbacks()
        self._resetButtonClickedCallback()
    
    def _setUpButtonCallbacks(self):
        self.ui.encodeButton.clicked.connect(lambda: self._encode())
        self.ui.decodeButton.clicked.connect(lambda: self._decode())
        self.ui.resetButton.clicked.connect(self._resetButtonClickedCallback)
        pass

    #ord('a') = 97
    ALPHABET_MORSE_CODE = [
        '.-',
        '-...',
        '-.-.',
        '-..',
        '.',
        '..-.',
        '--.',
        '....',
        '..',
        '.---',
        '-.-',
        '.-..',
        '--',
        '-.',
        '---',
        '.--.',
        '--.-',
        '.-.',
        '...',
        '-',
        '..-',
        '...-',
        '.--',
        '-..-',
        '-.--',
        '--..'
    ]

    #ord(0) = 48
    NUMBER_MORSE_CODE = [
        '-----',
        '.----',
        '..---',
        '...--',
        '....-',
        '.....',
        '-....',
        '--...',
        '---..',
        '----.'
    ]

    # Todo: 1) Make a CLI copy of this in 'Improved Implementation' that 'teaches' Dict
    #       2) Write a simplified CLI version of this in 'Minimum Implementation' that illustrates the use of a Dict

    def _encode(self):
        plain_text = self.ui.input_plaintext.toPlainText()
        cipher_text = []
        for char in plain_text:
            if ord(char) >= 97 and ord(char) < 97+26:
                cipher_text.append(MorseCodeModule.ALPHABET_MORSE_CODE[ord(char)-97])
            elif ord(char) >= 48 and ord(char) < 48+10:
                cipher_text.append(MorseCodeModule.NUMBER_MORSE_CODE[ord(char)-48])
            elif char == ' ':
                cipher_text.append(' / ')
            else:
                cipher_text.append(char)
        self.ui.output_ciphertext.setText(' '.join(cipher_text))

    def _decode(self):
        plain_text = self.ui.input_plaintext.toPlainText().split(' ')
        cipher_text = []
        for char in plain_text:
            if char in MorseCodeModule.ALPHABET_MORSE_CODE:
                cipher_text.append(chr(MorseCodeModule.ALPHABET_MORSE_CODE.index(char) + 97))
            elif char in MorseCodeModule.NUMBER_MORSE_CODE:
                cipher_text.append(chr(MorseCodeModule.NUMBER_MORSE_CODE.index(char) + 48))
            elif char == '/':
                cipher_text.append(' ')
            else:
                cipher_text.append(char)
        self.ui.output_ciphertext.setText(''.join(cipher_text))


    def _resetButtonClickedCallback(self):
        self.ui.input_plaintext.clear()
        self.ui.output_ciphertext.clear()
    pass


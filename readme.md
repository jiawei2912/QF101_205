# QF205 Python Project: Python and Its Applications in Ciphers
## Aim of the Project
This project is a part of the SMU QF205 Computing Technology for Finance course, and as prescribed, this report is written with the aim of teaching Python basics and some intermediate-level Python concepts. This will be done through the implementation of introductory encryption methods. 
The report will use various ciphers, from the Caesar cipher to RSA encryption, to demonstrate the features, data structures, and user-friendliness of Python when implementing fundamental encryption concepts. We will also explore fundamental programming concepts such as variables, data types, loops, conditional logic, functions, and bitwise operations. Finally, we will also delve into some advanced topics such as classes, modularization, and a graphical user interface (GUI) implementation using the PyQt5 library.
Overall, this report aims to be a guide for anyone interested in learning the basics of Python through an introductory application of it to ciphers and encryption.

# Structure of the code
1) The main entry point of the code is main.py
2) The modules used for the program are stored in AppModules
3) The PyQt5 Python GUI files, used by the AppModules and by main.py, are stored in PyUI
4) The Qt Designer files are in UIFiles

## Instructions
# Running the program
Execute main.py using Python.
```
python main.py
```
# How to create and add a new module to the program
## 1) Create a new .ui file for the module via Qt Designer. Alternatively, duplicate and modify an existing UI file. 
### After creating the .ui file, run the following command to convert the .ui file into a PyQt5 Class .py file.
```
python -m PyQt5.uic.pyuic -x [FILENAME].ui -o [FILENAME].py
```
## 3) Create a .py file for the module in the AppModules folder. Alternatively, duplicate and modify an existing AppModules .py file. 
- Ensure that the class of the new module contains a title:str and an order:int class attributes. The former defines the module's name of the main program and the letter defines its ordering priority on the main menu.
- The class of the new module must also inherit QtWidgets.QWidget.
- Ensure that this class is located in a .py file within the AppModules folder.
### If you duplicated an existing file: 
- Modify _setUpButtonCallbacks(self) to connect the GUI buttons to various functions within the .py class.
- Modify resetButtonClickedCallback(self) to set suitable default values for the GUI elements.


# Etc
## List of Current Modules
1) Caesar Cipher
2) Monoalphabetic Substition
3) Vigenere Cipher
4) Affine Cipher
5) Morse Code
6) XOR Encryption
7) RSA Encryption (Toy)

## Commands to regenerate the existing PyQt5 Python Class Files 
```
python -m PyQt5.uic.pyuic -x Project/UIFiles/MainUI.ui -o Project/PyUI/MainUI.py
python -m PyQt5.uic.pyuic -x Project/UIFiles/LandingPageButton.ui -o Project/PyUI/LandingPageButton.py
python -m PyQt5.uic.pyuic -x Project/UIFiles/CaesarCipherUI.ui -o Project/PyUI/CaesarCipherUI.py
python -m PyQt5.uic.pyuic -x Project/UIFiles/MonoalphabeticSubstitutionCipherUI.ui -o Project/PyUI/MonoalphabeticSubstitutionCipherUI.py
python -m PyQt5.uic.pyuic -x Project/UIFiles/VigenereCipherUI.ui -o Project/PyUI/VigenereCipherUI.py
python -m PyQt5.uic.pyuic -x Project/UIFiles/MorseCodeUI.ui -o Project/PyUI/MorseCodeUI.py
python -m PyQt5.uic.pyuic -x Project/UIFiles/AffineCipherUI.ui -o Project/PyUI/AffineCipherUI.py
python -m PyQt5.uic.pyuic -x Project/UIFiles/XOREncryptionUI.ui -o Project/PyUI/XOREncryptionUI.py
python -m PyQt5.uic.pyuic -x Project/UIFiles/RSAToyEncryptionUI.ui -o Project/PyUI/RSAToyEncryptionUI.py
```
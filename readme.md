# QF205 Python Project: Python and Its Applications in Ciphers
## Aim of the Project
This project is a part of the SMU QF205 Computing Technology for Finance course, and as prescribed, this report is written with the aim of teaching Python basics and some intermediate-level Python concepts. This will be done through the implementation of introductory encryption methods. 
The report will use various ciphers, from the Caesar cipher to RSA encryption, to demonstrate the features, data structures, and user-friendliness of Python when implementing fundamental encryption concepts. We will also explore fundamental programming concepts such as variables, data types, loops, conditional logic, functions, and bitwise operations. Finally, we will also delve into some advanced topics such as classes, modularization, and a graphical user interface (GUI) implementation using the PyQt5 library.
Overall, this report aims to be a guide for anyone interested in learning the basics of Python through an introductory application of it to ciphers and encryption.

# Structure of the code
1) The main entry point of the code is main.py
2) The modules used for the program are stored in AppModules
3) The PyQt5 Python GUI files are stored in PyUI
4) The Qt Designer files are in UIFiles

# Usage of UI Files
## 1) Suggestion: Avoid loading .ui files directly.
When a .ui file is loaded, all objects within it become direct class attributes of the main window.
This makes the app difficult to manage.
It also hurts code reusability. For eg: 5 tabs that are only slightly dissimilar must be made such that each element must have a unique names across the entire app. This prevents easy templation.

## 2) Note: It is possible to load and unload .ui files during runtime.
This may be useful in some situations? But it then means that the .ui files must be available throughout the app's execution.
Additionally, swapping .ui files also implies that the mainwindow needs to be coded to handed each .ui file, which leads to class bloat.

## 3) "The standard way to interact with a UI file is to generate a Python class from it." - https://doc.qt.io/qtforpython/tutorials/basictutorial/uifiles.html
This effectively means that mini .ui files can be created as templates and loaded as classes.
This is superb for code-reusability. 
```
python -m PyQt5.uic.pyuic -x [FILENAME].ui -o [FILENAME].py

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

## 4) Steps to add a module
1) Create a new .ui file for the module. Duplicate the ExampleModule.py for convenience.
2) Modify the .ui file for your usage; make sure to label the inputs you need later.
3) Create a .py file for the module in the AppModules folder. Duplicate the ExampleModule.py for convenience.
4) Modify _setUpButtonCallbacks(self) if you added new buttons.
5) Implement the relevant calculation in _calculateButtonClickedCallback(self)
6) Modify _resetButtonClickedCallback(self) if necessary.
7) Import the new module in main.py
8) Add a instance of the new module to the moduleWidgets list in _loadAppModules(self) 


## Idea - Applications in Cryptography
1) Caesar Cipher
--> Requires a shift, alphabet, and input
--> Has a single output
2) Homophonic Substition Cipher
--> Need inputs for inputs
3) Vigenere Cipher
4) Morse Code
5) XOR Encryption
6) Timing Side Channel Demo?
7) Base 64 Encoder and Decoder
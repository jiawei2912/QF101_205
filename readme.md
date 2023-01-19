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
python -m PyQt5.uic.pyuic -x Project/UIFiles/AppPageUI_SimpleInterest.ui -o Project/PyUI/AppPageUI_SimpleInterest.py
python -m PyQt5.uic.pyuic -x Project/UIFiles/AppPageUI_CompoundInterest.ui -o Project/PyUI/AppPageUI_CompoundInterest.py

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
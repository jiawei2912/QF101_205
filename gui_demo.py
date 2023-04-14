import sys
from PyQt5 import QtCore, QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # This sets the title of the GUI window
        self.setWindowTitle("Graphical Interface")

        # PyQt5 Main windows require a Central/main widget
        # An 'empty' widget
        central_widget = QtWidgets.QWidget(self)    
        # Sets the central widget of the PyQt5 window
        self.setCentralWidget(central_widget)       

        # The central widget should contain a layout
        # Layout that organises children in a grid
        grid_layout = QtWidgets.QGridLayout(self)   
        # Sets this layout as the central widget's layout
        central_widget.setLayout(grid_layout)       

        # Add a title widget that says "Hello World!"
        # The QLabel widget displays text
        title = QtWidgets.QLabel(self)  
        # Set the text of the QLabel
        title.setText("Hello World!")   
        # Center align the text
        title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
        # Add the QLabel widget to grid_layout
        grid_layout.addWidget(title)    

def main():
    # The following two lines initialise the PyQt5 main window
    qApp = QtWidgets.QApplication(sys.argv)
    qWin = MainWindow()
    # Display the main window
    qWin.show()
    # Gracefully terminate the program when it is closed
    sys.exit(qApp.exec_())
    
if __name__ == '__main__':
    main()
import sys  # Import the sys module for system-specific parameters and functions

from PyQt5.QtWidgets import (  # Import necessary widgets and layout classes from PyQt5
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout
)

class Window(QWidget):  #QWidget acts as the base class for all visible UI elements in PyQt5 applications. It provides essential functionalities inherited by all widgets like labels, buttons, text boxes, and more.
    def __init__(self):
        super().__init__()  # Call the parent class constructor (QWidget)

        # Create widgets
        self.label1 = QLabel("Name:")  # Create a label for "Name"
        self.lineEdit1 = QLineEdit()  # Create a line edit for user input (name)
        self.label2 = QLabel("Age:")   # Create a label for "Age"
        self.lineEdit2 = QLineEdit()  # Create a line edit for user input (age)
        self.button = QPushButton("Submit")  # Create a button with text "Submit"

        # Create layouts
        hbox = QHBoxLayout()  # Create a horizontal box layout
        hbox.addWidget(self.label1)  # Add the "Name:" label to the hbox
        hbox.addWidget(self.lineEdit1)  # Add the name line edit to the hbox

        hbox2 = QHBoxLayout()  # Create another horizontal box layout
        hbox2.addWidget(self.label2)  # Add the "Age:" label to hbox2
        hbox2.addWidget(self.lineEdit2)  # Add the age line edit to hbox2

        vbox = QVBoxLayout()  # Create a vertical box layout
        vbox.addLayout(hbox)  # Add the first horizontal layout (name) to the vbox
        vbox.addLayout(hbox2)  # Add the second horizontal layout (age) to the vbox
        vbox.addWidget(self.button)  # Add the submit button to the vbox

        self.setLayout(vbox)  # Set the main layout for the window to the vbox
        self.setWindowTitle("Simple Form")  # Set the window title

if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create a QApplication object
    window = Window()  # Create an instance of the Window class
    window.show()  # Show the window
    sys.exit(app.exec_())  # Start the event loop and exit when closed

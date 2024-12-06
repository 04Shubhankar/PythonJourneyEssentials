# Import necessary modules
import sys
from PyQt5.QtWidgets import QApplication, QWidget

def main():
    # Create a QApplication object
    app = QApplication(sys.argv)

    # Create a QWidget object
    w = QWidget()

    # Set the size and position of the window
    w.resize(250, 150)
    w.move(300, 300)

    # Set the window title
    w.setWindowTitle("Simple")

    # Show the window
    w.show()

    # Start the application event loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap

# Create the main application window
def window():
    app = QApplication(sys.argv)
    win = QWidget()

    # Create a label to display the image
    l1 = QLabel()
    l1.setPixmap(QPixmap("Python.png"))  # Set the image path

    # Create a vertical layout to arrange the label
    vbox = QVBoxLayout()
    vbox.addWidget(l1)

    # Set the layout for the main window
    win.setLayout(vbox)
    win.setWindowTitle("QPixmap Demo")
    win.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    window()

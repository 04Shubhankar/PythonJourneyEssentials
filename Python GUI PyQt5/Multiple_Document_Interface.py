import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QTextEdit

class MdiWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.mdiArea = QMdiArea()
        self.setCentralWidget(self.mdiArea)

        # Create a new MDI child window
        subwindow = QMdiSubWindow()
        subwindow.setWidget(QTextEdit())
        self.mdiArea.addSubWindow(subwindow)
        subwindow.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MdiWindow()
    window.show()
    sys.exit(app.exec_())

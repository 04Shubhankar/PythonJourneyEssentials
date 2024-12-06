import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QTextEdit, QWidget, QVBoxLayout
from PyQt5.QtGui import QClipboard

class ClipboardExample(QWidget):
    def __init__(self):
        super().__init__()

        self.textEdit = QTextEdit()
        self.copyButton = QPushButton("Copy")
        self.pasteButton = QPushButton("Paste")

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.copyButton)
        layout.addWidget(self.pasteButton)
        self.setLayout(layout)

        self.copyButton.clicked.connect(self.copyText)
        self.pasteButton.clicked.connect(self.pasteText)

    def copyText(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.textEdit.toPlainText())

    def pasteText(self):
        clipboard = QApplication.clipboard()
        self.textEdit.setText(clipboard.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ClipboardExample()
    window.show()
    sys.exit(app.exec_())

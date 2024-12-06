import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QPixmap, QDrag  # Corrected import for QDrag

class DragDropWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)  # Enable drag and drop

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            mimeData = QMimeData()
            mimeData.setText("Hello, World!")

            drag = QDrag(self)
            drag.setMimeData(mimeData)
            drag.setPixmap(QPixmap('drag_icon.png'))
            drag.exec_(Qt.CopyAction | Qt.MoveAction)

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('text/plain'):
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasFormat('text/plain'):
            event.setDropAction(Qt.CopyAction)
            event.accept()
            text = event.mimeData().text()
            print("Dropped text:", text)  # For demonstration
        else:
            event.ignore()

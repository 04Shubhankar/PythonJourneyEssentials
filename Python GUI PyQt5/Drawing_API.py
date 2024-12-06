import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush

class DrawingWidget(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(QColor(255, 0, 0), 2))
        painter.drawLine(20, 20, 200, 20)

        painter.setBrush(QBrush(QColor(0, 0, 255)))
        painter.drawRect(50, 50, 100, 100)

        painter.setPen(QPen(QColor(0, 255, 0)))
        painter.drawEllipse(150, 150, 50, 50)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DrawingWidget()
    window.show()
    sys.exit(app.exec_())

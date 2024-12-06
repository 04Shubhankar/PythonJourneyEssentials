import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QBrush, QColor

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setGeometry(300, 300, 350, 280)
        self.setWindowTitle('Brushes')
        self.show()
        
    def paintEvent(self, event):
        
        qp = QPainter()
        qp.begin(self)
        
        brush = QBrush(Qt.Dense6Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 105, 90, 60)

        brush = QBrush(Qt.Dense7Pattern)
        qp.setBrush(brush)
        qp.drawRect(10, 195, 90, 60)

        brush = QBrush(Qt.HorPattern)
        qp.setBrush(brush)
        qp.drawRect(130, 195, 90, 60)

        brush = QBrush(Qt.VerPattern)
        qp.setBrush(brush)
        qp.drawRect(250, 195, 90, 60)

        qp.end()
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

#!/usr/bin/env python3
from math import sin, cos, radians
import sys
from os import path, remove
from time import sleep
from PyQt5.QtGui import (QPainter,
                         QPalette,
                         QPen,
                         QColor,
                         QBrush,
                         QIcon)
from PyQt5.QtWidgets import (QWidget,
                             QMainWindow,
                             QFrame,
                             QHBoxLayout,
                             QVBoxLayout,
                             QFormLayout,
                             QSizePolicy,
                             QApplication,
                             QSlider,
                             QLabel,
                             QPushButton,
                             QCheckBox,
                             QFileDialog,
                             QMessageBox,
                             QProgressDialog,
                             QColorDialog)
from PyQt5.QtCore import (QSize,
                          QTimer,
                          QPointF,
                          Qt,
                          QLineF,
                          QByteArray,
                          QBuffer,
                          QIODevice)

W = 256
H = 256

def paintEvent(self, *_):
    """
    This is called on self.update() and on resize.
    """
    painter = QPainter(self)
    painter.setRenderHint(QPainter.Antialiasing, True)
    painter.translate(self.width() / 2, self.height() / 2)  # Make Cartesian
    
class TarskisWorld(QWidget):
    def __init__(self):
        super().__init__(None)
        self.setWindowTitle("Tarskis World")
        self.setWindowFlags(Qt.Dialog)  # Make it start in floating mode on tiling WMs
        # self.setWindowIcon(QIcon(resource_path("icon.png")))

def main():
    """
    Run the world
    """
    app = QApplication([])
    win = TarskisWorld()
    win.resize(W, H)
    win.show()
    return app.exec()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import pyqtSlot



if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    
    button = QPushButton('PyQt5 button', w)
    button.setToolTip('This is an example button')
    button.move(100,70)
    
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple. Test' )
    w.show()

    sys.exit(app.exec_())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtCore import pyqtSlot


class MyWidget(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button example '
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(100,70) 
        button.clicked.connect(self.on_click)
        
        self._label = QLabel("Label-text", self)
        self._label.move(100,150)
        
        self.show()
        
        
 
    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click. Test')
        self._label.setText("Hello")
        #self._label.adjustSize()
        #self._label.show()
        #self.show()
        self._label.repaint()
        
        px = self._label.x()
        py = self._label.y()
        
        self._label.move(px+10, py)
        
        
        #QWidget.update(self)    
        self.repaint()
      
        
        
        
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.exit(app.exec_())    
    

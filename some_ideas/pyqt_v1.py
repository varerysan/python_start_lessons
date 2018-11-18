#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtCore import pyqtSlot

from threading import Thread
import time


class MyWidget(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button example '
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self._count = 0
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
        
    def set_info(self):
        text = str(self._count)
        self._count += 1
        self._label.setText(text)
        
        
        
      

class Worker(Thread):
    def __init__(self, name, widget):
        """Инициализация потока"""
        Thread.__init__(self)
        self.name = name
        self._widget = widget
    
    def run(self):
        """Запуск потока"""
        #amount = random.randint(3, 15)
        
        for n in range(500):
            time.sleep(0.2)
            self._widget.set_info()
        
        
 
if __name__ == '__main__':
    print("Test-1")
    app = QApplication(sys.argv)
    print("Test-2")
    ex = MyWidget()
    print("Test-3")
    wrk = Worker("aaa", ex)
    wrk.start()
    
    
    
    sys.exit(app.exec_())    
    




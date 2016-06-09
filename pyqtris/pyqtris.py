""" A convenience startup file for the game. 
"""
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication

from tetrisgame import TetrisMainWindow


app = QApplication(sys.argv)
form = TetrisMainWindow()
form.show()
app.exec_()



'''
Created on Jul 8, 2018

@author: Miguel RT
'''
import sys
import os
from PyQt5 import uic, QtWidgets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui


from click._compat import raw_input
#from Loan import principalM, monthlyInstallmentM
import matplotlib.pyplot as plt         
import numpy as np
import SolarProductionN
import csv  
import datetime
import EnergyPriceN
import Loan
import ExchangeRate
import Distribution
import MainGUI

from gra import Ui_answer
#import Ui_MainWindow


#qtCreatorFile = "proyecto.ui" # Nombre del archivo aquí.

#Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_answer):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_answer.__init__(self)
        self.setupUi(self)
        self.button.clicked.connect(self.postal)  
        #self.button2.clicked.connect(self.graph)
        self.button2.clicked.connect(self.erase)
        #self.matplotlibwidget.axes.plot(x, y)
    
    def postal(self):
        area=int(self.area.toPlainText())
        cp=int(self.pc.toPlainText())
        months=int(self.period.toPlainText())
        tof=str(self.comboBox.currentText()) # Type of user
        MainGUI.Main(area,cp,months,tof)
        #self.df=self.comboBox.parse(self.combox.currentText())
        
            
        
        
    def erase(self):
        self.ans.setText('erase')
        
        #self.ans2.setText('')
      
    

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
     

'''
Created on Jul 8, 2018

@author: Miguel RT
'''
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


from gra import Ui_answer
#import Ui_MainWindow





#----------*****----------*****----------*****----------*****----------*****----------*****----------*****----------*****----------

# Inputs

# Ratio of KWp by area [KWP/m2], value obtained from the manufacturer technical sheet
wp=0.145 # ratio in [kwp/m2]

#Area of the solar panels in [m2]
area=80 #m2
#solar production year estimate_bandwidth    kw*h/yr
#estimated with a function

#print(solarP) 
#Total cost of install  $
iInv=15265
#Energy price per $/KW*h
energyP=0.25
#electricity price increase per year    1/yr
electricityI=0.02
#solar panel yearly degradation 1/yr
panelD=0.005
#number of months
months=250

#Cash flow model
vTime=[]
vTimeY=[]
mEProduction=[]
vDegradation=[]
eGeneration=[]
cashFlow=[]
netCashFlow=[]
netCashFlowY=[]
cashFlow.append(-iInv)
netCashFlow.append(-iInv)


#----------*****----------*****----------*****----------*****----------*****----------*****----------*****----------*****----------
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
        
        #read data
        area=int(self.area.toPlainText())
        postcode=int(self.pc.toPlainText())
        months=int(self.period.toPlainText())
        
        
        df=pd.read_excel('DB.xlsx')
        row=(df[df.PC==postcode])
        row_st=str(row)
        ratio=row.iat[0,2]
        solarP=ratio*area
        ratio_st=str(ratio)
        self.ans.setText(ratio_st)
        
        for i in range(months+1):
            vTime.append(i)
            
            
        for i in range(1,months+1):
    
            mProduction=round(solarP/12,3) # delete round
            mEProduction.append(mProduction)
    
            degradation=round(100*i*panelD/12,3) # delete round 
            vDegradation.append(degradation)
    
            generation=round(mProduction*(1-degradation/100),3)# delete round
            eGeneration.append(generation)
    
            #cash=round(generation*energyP*(1+i*electricityI/(100*12)),3) # aqui esta el peine
            cash=round(generation*energyP*(1+i*electricityI/(12)),3) # aqui esta el peine
            cashFlow.append(cash)
    
            net=round(sum(cashFlow),0)
            netCashFlow.append(net)    
            
        irr=np.irr(cashFlow)
        vTime_st=str(vTime)
        netCashFlow_st=str(netCashFlow)
        #self.ans.setText('ddd')
        self.ans.setText(vTime_st)
        #self.ans2.setText(netCashFlow_st)
        
        plt.plot(vTime,netCashFlow)
        
        plt.show()
        self.graphicsView.plot(vTime,netCashFlow)
        self.graphicsView.plot
              
        return(months,netCashFlow)
    
    def erase(self):
        self.ans.setText('')
        #self.ans2.setText('')
      


    

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
     

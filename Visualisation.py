import sys
import random
import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import numpy as np
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject 

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Signal(QObject):
    signal = pyqtSignal()    
    
    def emit_signal(self):
        self.signal.emit()

class TransferedData():

    frequency_min = 5000000
    frequency_max = 30000000
    #by default linsteps is 1000
    lin_steps = 1000
    frequency_domain = np.linspace(frequency_min, frequency_max, lin_steps) 
    load_domain = np.ones(lin_steps)
    impedance_domain = np.ones(lin_steps)
    condensator_prefix = 1e-12
    coil_prefix = 1e-6    
 
    #the following four entities are impedance values of the corresponding network components 
    c_load = np.ones(lin_steps)
    l_load = np.ones(lin_steps)
    c_tune = np.ones(lin_steps)
    l_tune = np.ones(lin_steps)

    @staticmethod
    def set_impedance_domain():
        term_1  = np.power(TransferedData.c_load + TransferedData.l_load + TransferedData.load_domain, -1) 
        term_2 = np.power(TransferedData.c_tune + TransferedData.l_tune)
        TransferedData.set_impedance_domain = np.power((TransferedData.term_1 + TransferedData.term_2), -1)

    @staticmethod
    def get_freueny_domain():
        return TransferedData.frequency_domain
    @staticmethod
    def set_frequency_domain():
        TransferedData.frequency_domain = np.linspace(TransferedData.set_frequency_min, TransferedData.set_frequency_maxfrequency_max, TransferedData.lin_steps) 
    @staticmethod
    def set_load_domain(real, imag): 
        TransferedData.load_domain = (real + imag * 1j) * np.ones(TransferedData.lin_steps)
    @staticmethod
    def get_load_domain():
        return TransferedData.load_domain
    @staticmethod
    def set_c_load(value):
        TransferedData.c_load = np.power(TransferedData.condensator_prefix * value * TransferedData.frequency_domain * 1j, -1)
    @staticmethod
    def get_c_load():
        return TransferedData.c_load    
    @staticmethod
    def set_l_load(value):
        TransferedData.l_load = TransferedData.coil_prefix * value * TransferedData.frequency_domain * 1j
    @staticmethod
    def get_l_load():
        return TransferedData.l_load    
    @staticmethod
    def set_c_tune(value):
        TransferedData.c_tune = np.power(TransferedData.condensator_prefix * value * TransferedData.frequency_domain * 1j, -1)
    @staticmethod
    def get_c_tune(value):
        return TransferedData.c_tune    
    @staticmethod
    def set_l_tune(value):
        TransferedData.l_tune = TransferedData.coil_prefix * value * TransferedData.frequency_domain * 1j
    @staticmethod
    def get_l_tune():
        return TransferedData.l_tune
    @staticmethod
    def set_frequency_min(value):
        TransferedData.frequency_min = value
    @staticmethod
    def get_frequency_min():
        return TransferedData.frequency_min
    @staticmethod
    def set_frequency_max(value):
        TransferedData.frequency_max = value
    @staticmethod
    def get_frequency_max():
        return TransferedData.frequency_max

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=3, height=1, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)

class VisualWindow(object):

    def __init__(self):
        self.signal = Signal()
        self.frequency_min = 5000000
        self.frequency_max = 30000000
        #by default linsteps is 1000
        self.lin_steps = 1000
        self.frequency_domain = np.linspace(self.frequency_min, self.frequency_max, self.lin_steps) 
        self.load_domain = np.ones(self.lin_steps)
        self.impedance_domain = np.ones(self.lin_steps)
        self.condensator_prefix = 1e-12
        self.coil_prefix = 1e-6 
        self.c_load = np.ones(self.lin_steps)
        self.l_load = np.ones(self.lin_steps)
        self.c_tune = np.ones(self.lin_steps)
        self.l_tune = np.ones(self.lin_steps)

    def setUi(self, qWindow):
        qWindow.setObjectName("qWindow")
        qWindow.setWindowTitle("Visualisation")
        qWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(qWindow)        
        self.canvas = MplCanvas(self, width=5, height=4, dpi=80)
        qWindow.setCentralWidget(self.canvas)    
                
        self.xdata = TransferedData.frequency_domain
        self.ydata = TransferedData.impedance_domain
        self.update_plot()        

    def update_plot(self):
        self.canvas.axes.cla()  # Clear the canvas.
        self.canvas.axes.plot(self.xdata, self.ydata, 'r')
        # Trigger the canvas to update and redraw.
        self.canvas.draw()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qWindow = QMainWindow()
    ui = VisualWindow()
    ui.setUi(qWindow)    
    qWindow.show()
    sys.exit(app.exec_())
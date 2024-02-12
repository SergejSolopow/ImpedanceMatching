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

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=3, height=1, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)

class VisualWindow(object):
    def __init__(self):
        #create instace signal and connect it to the method update_plote. 
        #every time the esignal is emited by any other instance, it will be cached and the plote will be updated 
        self.signal = Signal()
        self.signal.signal.connect(self.update_plot)        
        
        self.frequency_min = 5000000
        self.frequency_max = 30000000
        #by default linsteps is 1000
        self.lin_steps = 1000
        self.frequency_domain = np.linspace(self.frequency_min, self.frequency_max, self.lin_steps) 
        self.load_domain = np.ones(self.lin_steps)
        self.impedance_domain = np.ones(self.lin_steps) + np.ones(self.lin_steps)*1j
        #modul is the mathematic expression for |z * z*|^0.5
        self.modul_impedance = np.ones(self.lin_steps)
        #normalized modul
        self.normalized_modul =  np.ones(self.lin_steps)
        #for the picofarad condensator
        self.condensator_prefix = 1e-12
        #for the microhenry coils
        self.coil_prefix = 1e-6 
        self.c_load = np.ones(self.lin_steps)
        self.l_load = np.ones(self.lin_steps)
        self.c_tune = np.ones(self.lin_steps)
        self.l_tune = np.ones(self.lin_steps)

    def set_impedance_domain(self):
        term_1  = np.power(self.c_load + self.l_load + self.load_domain, -1) 
        term_2 = np.power(self.c_tune + self.l_tune, -1)
        self.impedance_domain = np.power((term_1 + term_2), -1)
        self.modul_impedance = np.power(self.impedance_domain * np.conj(self.impedance_domain), .5)
        self.normalized_modul = self.modul_impedance/np.max(self.modul_impedance)
        self.signal.emit_signal()

    def get_freueny_domain(self):
        return self.frequency_domain
    
    def set_frequency_domain(self):
        self.frequency_domain = np.linspace(self.get_frequency_min(), self.get_frequency_max(), self.lin_steps) 
        self.signal.emit_signal()
    
    def set_load_domain(self, real = 0, imag = -100): 
        self.load_domain = (real + imag * 1j) * np.ones(self.lin_steps)
        self.set_impedance_domain()
        self.signal.emit_signal()
    
    def get_load_domain(self):
        return self.load_domain
    
    def set_c_load(self, value):
        self.c_load = np.power(self.condensator_prefix * value * self.frequency_domain * 1j, -1)
        self.set_impedance_domain()
        self.signal.emit_signal()

    def get_c_load(self):
        return self.c_load    
    
    def set_l_load(self, value):
        self.l_load = self.coil_prefix * value * self.frequency_domain * 1j
        self.set_impedance_domain()
        self.signal.emit_signal()
    
    def get_l_load(self):
        return self.l_load    
    
    def set_c_tune(self, value):
        self.c_tune = np.power(self.condensator_prefix * value * self.frequency_domain * 1j, -1)
        self.set_impedance_domain()
        self.signal.emit_signal()
    
    def get_c_tune(self):
        return self.c_tune    
    
    def set_l_tune(self, value):
        self.l_tune = self.coil_prefix * value * self.frequency_domain * 1j
        self.set_impedance_domain()
        self.signal.emit_signal()
    
    def get_l_tune(self):
        return self.l_tune
    
    def set_frequency_min(self, value):
        self.frequency_min = value
        self.signal.emit_signal()
    
    def get_frequency_min(self):
        return self.frequency_min
    
    def set_frequency_max(self, value):
        self.frequency_max = value
        self.signal.emit_signal()
    
    def get_frequency_max(self):
        return self.frequency_max
    
    def setUi(self, qWindow):
        qWindow.setObjectName("qWindow")
        qWindow.setWindowTitle("Visualisation")
        qWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(qWindow)        
        self.canvas = MplCanvas(self, width=5, height=4, dpi=80)
        qWindow.setCentralWidget(self.canvas)    
        #plot data
        self.update_plot()        

    def update_plot(self):
        self.canvas.axes.cla()  # Clear the canvas.
        #self.canvas.axes.plot(self.frequency_domain, self.modul_impedance, 'r')
        self.canvas.axes.plot(self.frequency_domain, self.normalized_modul, 'r')
        # Trigger the canvas to update and redraw.
        self.canvas.draw()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qWindow = QMainWindow()
    ui = VisualWindow()
    ui.setUi(qWindow)    
    qWindow.show()
    sys.exit(app.exec_())
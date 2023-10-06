import sys
import random
import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class TrasferedData():
    frequency_range_min = 5000000
    frequency_range_max = 30000000
    c_load = 0
    l_load = 0
    c_tune = 0 
    l_tune = 0

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=3, height=1, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)

class VisualWindow(object):
    def setUi(self, qWindow):
        qWindow.setObjectName("qWindow")
        qWindow.setWindowTitle("Visualisation")
        qWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(qWindow)
        
        self.canvas = MplCanvas(self, width=5, height=4, dpi=80)
        qWindow.setCentralWidget(self.canvas)
        
        n_data = 50
        self.xdata = list(range(n_data))
        self.ydata = [random.randint(0, 10) for i in range(n_data)]
        self.update_plot()
        

    def update_plot(self):
        # Drop off the first y element, append a new one.
        self.ydata = self.ydata[1:] + [random.randint(0, 10)]
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
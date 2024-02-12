import numpy as np
import matplotlib.pyplot as plt

class Plot3D():
    def __init__(self) -> None:       
        self.frequency_min = 5000000
        self.frequency_max = 30000000
        #by default linsteps is 1000
        self.lin_steps = 1000
        self.frequency_domain = np.linspace(self.frequency_min, self.frequency_max, self.lin_steps) 
        self.load_domain = np.ones(self.lin_steps) * (1 + 1000j)
        self.impedance_domain = []
        self.modul_impedance = []
        self.condensator_prefix = 1e-12
        self.coil_prefix = 1e-6 
        self.c_load = (np.power(200 * self.condensator_prefix *1j, -1)) * self.frequency_domain
        self.l_load = 10 * self.coil_prefix * 1j * self.frequency_domain
        self.c_tune = (np.power(68 * self.condensator_prefix *1j, -1)) * self.frequency_domain
        self.l_tune =  10 * self.coil_prefix *1j * self.frequency_domain
        
        #self.plot3D()
        self.plot()

    def impedance_function(self, c_load, c_tune):
        term_1  = np.power(c_load + self.l_load + self.load_domain, -1) 
        term_2 = np.power(c_tune + self.l_tune, -1)
        self.impedance_domain = np.power((term_1 + term_2), -1)
        self.modul_impedance = np.power(self.impedance_domain * np.conj(self.impedance_domain), .5)
        return self.modul_impedance 

    def plot3D(self):
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        X, Y = np.meshgrid(self.c_load, self.c_tune)
        Z = self.impedance_function(X, Y)
        ax.contour3D(X, Y, Z, 80, cmap='binary')
        plt.show()
    
    def plot(self):
        self.impedance_function(self.c_load, self.c_tune)
        fig = plt.figure()
        plt.plot(self.frequency_domain, np.imag(self.c_load), 'r')
        plt.show()

if __name__ == "__main__":
    plot = Plot3D()
    
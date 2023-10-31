import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

class DataVisualisation():
    def __init__(self):
        self.path = "V:\\Persönliche Ordner\\Solopow\\03_Projekte\\03_FloateFaradaySchirm\\Python\\"
        self.file = "fingerprint_short_SF6_with_Faraday_Type1_Ecoflex9.3m_3Pa@231010-140802.csv"
        self.data = []
        self.x = []
        self.y = []
        self.z = []
        self.y1 = []
        self.z1 = []
        self.panda_csv()
        self.plot_data()
    
    def set_path(self, path):
        self.path = path

    def get_path(self):
        return self.path

    def set_fail(self, fail):
        self.fail = fail

    def get_fail(self):
        return self.fail

    def read_csv(self):
         with open(self.file) as file:
            reader = csv.reader(file, delimiter = ";")
            for x in range(2):
                line = file.readline()
                new_line = line.replace(",", ".")
                arr = new_line.split(";")
                print(line)
                print(arr)
    
    def panda_csv(self):
        data_frame = pd.read_csv(self.file, sep = ";")
        data_frame = data_frame.replace(",", ".", regex=True)
        print(data_frame.head(0))
        self.x = data_frame["time(ms)"].astype(float)
        self.y = data_frame["Source.Matchbox.Load"].astype(float)
        self.z = data_frame["Source.Matchbox.Tune"].astype(float)
        self.y1 = data_frame["Source.Generator.Power"].astype(float)
        self.z1 = data_frame["Source.Generator.PowerReflected"].astype(float)

    def plot_data(self):
        fig, ax = plt.subplots()
        fig1, ax1 = plt.subplots()
        ax.plot(self.x, self.y, self.x, self.z, linewidth = "0.3")
        ax1.plot(self.x, self.y1, self.x, self.z1, linewidth = "0.3")
        #ax1.plot(self.x, self.z1, linewidth = "0.3")
        #ax.plot(self.x, self.z, linewidth = "0.2")
       # ax.set_yticklabels([])
        ax.set_xticklabels([])
        #ax1.set_yticklabels([])
        ax1.set_xticklabels([])
        plt.show()

if __name__ == "__main__":
    my_dv = DataVisualisation()
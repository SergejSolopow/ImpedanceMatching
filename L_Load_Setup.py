from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_L_Load_Setup(object):
    
    def setupUi(self, L_Load_Setup):
        L_Load_Setup.setObjectName("L_Load_Setup")
        L_Load_Setup.resize(313, 364)
        self.centralwidget = QtWidgets.QWidget(L_Load_Setup)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 261, 91))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.min_value_edit = QtWidgets.QLineEdit(self.groupBox)
        self.min_value_edit.setGeometry(QtCore.QRect(10, 40, 113, 20))
        self.min_value_edit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.min_value_edit.setObjectName("min_value_edit")
        self.min_value_edit.returnPressed.connect(lambda: self.get_min_value())

        self.max_value_edit = QtWidgets.QLineEdit(self.groupBox)
        self.max_value_edit.setGeometry(QtCore.QRect(140, 40, 113, 20))
        self.max_value_edit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.max_value_edit.setObjectName("max_value_edit")
        self.max_value_edit.returnPressed.connect(lambda: self.get_max_value())

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 140, 261, 80))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.step_size_edit = QtWidgets.QLineEdit(self.groupBox_2)
        self.step_size_edit.setGeometry(QtCore.QRect(80, 30, 113, 20))
        self.step_size_edit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.step_size_edit.setObjectName("step_size_edit")
        self.step_size_edit.returnPressed.connect(lambda: self.get_step_size())

        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 250, 261, 80))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.start_value_edit = QtWidgets.QLineEdit(self.groupBox_3)
        self.start_value_edit.setGeometry(QtCore.QRect(80, 30, 113, 20))
        self.start_value_edit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.start_value_edit.setObjectName("start_value_edit")
        self.start_value_edit.returnPressed.connect(lambda: self.get_start_value())

        L_Load_Setup.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(L_Load_Setup)
        self.statusbar.setObjectName("statusbar")
        L_Load_Setup.setStatusBar(self.statusbar)

        self.retranslateUi(L_Load_Setup)
        QtCore.QMetaObject.connectSlotsByName(L_Load_Setup)

    def retranslateUi(self, L_Load_Setup):
        _translate = QtCore.QCoreApplication.translate
        L_Load_Setup.setWindowTitle(_translate("L_Load_Setup", "C Load"))
        self.groupBox.setTitle(_translate("L_Load_Setup", "Range"))
        self.groupBox_2.setTitle(_translate("L_Load_Setup", "Step size"))
        self.groupBox_3.setTitle(_translate("L_Load_Setup", "Start value"))
    
    def get_min_value(self):
        text = self.min_value_edit.text()
        self.min_value = text
    
    def get_max_value(self):
        text = self.max_value_edit.text()
        self.max_value = text

    def get_step_size(self):
        text = self.step_size_edit.text()
        self.step_size = text    

    def get_start_value(self):
        text = self.start_value_edit.text()
        Ui_L_Load_Setup.start_value = text

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    L_Load_Setup = QtWidgets.QMainWindow()
    ui = Ui_L_Load_Setup()
    ui.setupUi(L_Load_Setup)
    L_Load_Setup.show()
    sys.exit(app.exec_())
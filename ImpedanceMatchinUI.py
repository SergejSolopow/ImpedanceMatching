from C_Load_Setup import Ui_C_Load_Setup
from L_Load_Setup import Ui_L_Load_Setup
from C_Tune_Setup import Ui_C_Tune_Setup
from L_Tune_Setup import Ui_L_Tune_Setup
from PyQt5 import QtCore, QtGui, QtWidgets
from Visualisation import VisualWindow
import sys


class Ui_MainWindow(object):
    def __init__(self):
        self.c_load_min_value = 0
        self.c_load_max_value = 0
        self.c_load_start_value = 0
        self.c_load_step_size = 0
        
        self.l_load_min_value = 0
        self.l_load_max_value = 0
        self.l_load_start_value = 0
        self.l_load_step_size = 0
        
        self.c_tune_min_value = 0
        self.c_tune_max_value = 0
        self.c_tune_start_value = 0
        self.c_tune_step_size = 0
        
        self.l_tune_min_value = 0
        self.l_tune_max_value = 0
        self.l_tune_start_value = 0
        self.l_tune_step_size = 0

        self.real_part_load = 0
        self.imag_part_load = 0
        self.visualisation = VisualWindow()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1126, 864)
        MainWindow.setDocumentMode(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(90, 115, 301, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(570, 115, 51, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(260, 124, 20, 65))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(260, 276, 20, 82))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(90, 520, 761, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(260, 445, 20, 115))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(80, 421, 20, 111))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(80, 125, 20, 103))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(800, 110, 51, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(240, 560, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_6.setObjectName("label_6")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(840, 120, 20, 411))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(180, 180, 182, 95))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.groupBox.setObjectName("groupBox")
       
        self.c_tune_slider = QtWidgets.QSlider(self.groupBox)
        self.c_tune_slider.setGeometry(QtCore.QRect(10, 70, 160, 20))
        self.c_tune_slider.setOrientation(QtCore.Qt.Horizontal)
        self.c_tune_slider.setObjectName("c_tune_slider")
        self.c_tune_slider.valueChanged.connect(self.change_c_tune_lcd)
        self.c_tune_lcd = QtWidgets.QLCDNumber(self.groupBox)
        self.c_tune_lcd.setGeometry(QtCore.QRect(110, 20, 60, 30))
        self.c_tune_lcd.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.c_tune_lcd.setDigitCount(4)
        self.c_tune_lcd.setObjectName("c_tune_lcd")
        self.c_tune_edit = QtWidgets.QLineEdit(self.groupBox)
        self.c_tune_edit.setGeometry(QtCore.QRect(10, 20, 60, 30))
        self.c_tune_edit.setObjectName("c_tune_edit")
        self.c_tune_edit.returnPressed.connect(lambda: self.set_c_tune_lcd())
        self.c_tune_button = QtWidgets.QPushButton(self.groupBox)
        self.c_tune_button.setGeometry(QtCore.QRect(80, 20, 21, 23))
        self.c_tune_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.c_tune_button.setText("")
        self.c_tune_button.setObjectName("c_tune_button")
        self.c_tune_button.clicked.connect(self.call_c_tune_setup)

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(390, 70, 182, 95))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.groupBox_2.setObjectName("groupBox_2")
        
        self.c_load_slider = QtWidgets.QSlider(self.groupBox_2)
        self.c_load_slider.setGeometry(QtCore.QRect(10, 70, 160, 20))
        self.c_load_slider.setOrientation(QtCore.Qt.Horizontal)
        self.c_load_slider.setObjectName("c_load_slider")
        self.c_load_slider.valueChanged.connect(self.change_c_load_lcd)
        self.c_load_lcd = QtWidgets.QLCDNumber(self.groupBox_2)
        self.c_load_lcd.setGeometry(QtCore.QRect(110, 20, 60, 30))
        self.c_load_lcd.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.c_load_lcd.setDigitCount(4)
        self.c_load_lcd.setObjectName("c_load_lcd")
        self.c_load_edit = QtWidgets.QLineEdit(self.groupBox_2)
        self.c_load_edit.setGeometry(QtCore.QRect(10, 20, 60, 30))
        self.c_load_edit.setObjectName("c_load_edit")
        self.c_load_edit.returnPressed.connect(lambda: self.set_c_load_lcd())
        self.c_load_button = QtWidgets.QPushButton(self.groupBox_2)
        self.c_load_button.setGeometry(QtCore.QRect(79, 23, 21, 23))
        self.c_load_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.c_load_button.setText("")
        self.c_load_button.setObjectName("c_load_button")
        self.c_load_button.clicked.connect(self.call_c_load_setup)

        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(620, 70, 182, 95))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.groupBox_3.setObjectName("groupBox_3")
        
        self.l_load_slider = QtWidgets.QSlider(self.groupBox_3)
        self.l_load_slider.setGeometry(QtCore.QRect(10, 70, 160, 20))
        self.l_load_slider.setOrientation(QtCore.Qt.Horizontal)
        self.l_load_slider.setObjectName("l_load_slider")
        self.l_load_slider.valueChanged.connect(self.change_l_load_lcd)
        self.l_load_lcd = QtWidgets.QLCDNumber(self.groupBox_3)
        self.l_load_lcd.setGeometry(QtCore.QRect(110, 20, 60, 30))
        self.l_load_lcd.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.l_load_lcd.setDigitCount(4)
        self.l_load_lcd.setObjectName("l_load_lcd")        
        self.l_load_edit = QtWidgets.QLineEdit(self.groupBox_3)
        self.l_load_edit.setGeometry(QtCore.QRect(10, 20, 60, 30))
        self.l_load_edit.setObjectName("l_load_edit")
        self.l_load_edit.returnPressed.connect(lambda: self.set_l_load_lcd())
        self.l_load_button = QtWidgets.QPushButton(self.groupBox_3)
        self.l_load_button.setGeometry(QtCore.QRect(80, 20, 21, 23))
        self.l_load_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.l_load_button.setText("")
        self.l_load_button.setObjectName("l_load_button")
        self.l_load_button.clicked.connect(self.call_l_load_setup)

        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(180, 350, 182, 95))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.groupBox_4.setObjectName("groupBox_4")
        
        self.l_tune_slider = QtWidgets.QSlider(self.groupBox_4)
        self.l_tune_slider.setGeometry(QtCore.QRect(10, 70, 160, 20))
        self.l_tune_slider.setOrientation(QtCore.Qt.Horizontal)
        self.l_tune_slider.setObjectName("l_tune_slider")
        self.l_tune_slider.valueChanged.connect(self.change_l_tune_lcd)
        self.l_tune_lcd = QtWidgets.QLCDNumber(self.groupBox_4)
        self.l_tune_lcd.setGeometry(QtCore.QRect(110, 20, 60, 30))
        self.l_tune_lcd.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.l_tune_lcd.setDigitCount(4)
        self.l_tune_lcd.setObjectName("l_tune_lcd")
        self.l_tune_edit = QtWidgets.QLineEdit(self.groupBox_4)
        self.l_tune_edit.setGeometry(QtCore.QRect(10, 20, 60, 30))
        self.l_tune_edit.setObjectName("l_tune_edit")
        self.l_tune_edit.returnPressed.connect(lambda: self.set_l_tune_lcd())
        self.l_tune_button = QtWidgets.QPushButton(self.groupBox_4)
        self.l_tune_button.setGeometry(QtCore.QRect(80, 20, 21, 23))
        self.l_tune_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.l_tune_button.setText("")
        self.l_tune_button.setObjectName("l_tune_button")
        self.l_tune_button.clicked.connect(self.call_l_tune_setup)

        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(710, 180, 281, 331))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.groupBox_5.setObjectName("groupBox_5")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 30, 120, 281))
        self.groupBox_7.setObjectName("groupBox_7")

        self.lineRealPart = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineRealPart.setGeometry(QtCore.QRect(0, 60, 113, 31))
        self.lineRealPart.setObjectName("lineRealPart")
        self.lineRealPart.returnPressed.connect(lambda: self.set_real_value())

        self.lineImagPart = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineImagPart.setGeometry(QtCore.QRect(0, 150, 113, 31))
        self.lineImagPart.setObjectName("lineImagPart")
        self.lineImagPart.returnPressed.connect(lambda: self.set_imag_value())

        self.label = QtWidgets.QLabel(self.groupBox_7)
        self.label.setGeometry(QtCore.QRect(0, 40, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_7)
        self.label_2.setGeometry(QtCore.QRect(0, 130, 81, 20))
        self.label_2.setObjectName("label_2")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 220, 161, 201))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_6)
        self.tabWidget.setGeometry(QtCore.QRect(16, 40, 141, 141))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 113, 20))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 40, 113, 20))
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1126, 21))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuProperties = QtWidgets.QMenu(self.menubar)
        self.menuProperties.setObjectName("menuProperties")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuSetup = QtWidgets.QMenu(self.menubar)
        self.menuSetup.setObjectName("menuSetup")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionImport_data = QtWidgets.QAction(MainWindow)
        self.actionImport_data.setObjectName("actionImport_data")
        self.actionSave_data = QtWidgets.QAction(MainWindow)
        self.actionSave_data.setObjectName("actionSave_data")
        self.menuOptions.addAction(self.actionNew)
        self.menuProperties.addAction(self.actionImport_data)
        self.menuProperties.addAction(self.actionSave_data)
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuProperties.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuSetup.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Impedance matching tool"))
        self.label_6.setText(_translate("MainWindow", "Ground"))
        self.groupBox.setTitle(_translate("MainWindow", "C Tune"))
        self.groupBox_2.setTitle(_translate("MainWindow", "C Load"))
        self.groupBox_3.setTitle(_translate("MainWindow", "L Load"))
        self.groupBox_4.setTitle(_translate("MainWindow", "L Tune"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Load"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Impedance"))
        self.label.setText(_translate("MainWindow", "Real"))
        self.label_2.setText(_translate("MainWindow", "Imagenary"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Generator"))
        self.lineEdit.setText(_translate("MainWindow", "13.56 MHz"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Frequency"))
        self.lineEdit_2.setText(_translate("MainWindow", "50 Ohm"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "resistance"))
        self.menuOptions.setTitle(_translate("MainWindow", "File"))
        self.menuProperties.setTitle(_translate("MainWindow", "Edit"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuSetup.setTitle(_translate("MainWindow", "Setup"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionImport_data.setText(_translate("MainWindow", "Import data"))
        self.actionSave_data.setText(_translate("MainWindow", "Save data"))
    
    def start_visualisation(self):     
        self.window = QtWidgets.QMainWindow()
        self.ui = VisualWindow()
        self.ui.setUi(self.window)    
        self.window.show()
    
    #set imagenary part for the impedance of the load
    def set_imag_value(self):
        text = self.lineImagPart.text()
        self.imag_part_load = float(text)
        self.visualisation.set_load_domain(imag = float(text))

    #set real part for the impedance of the load
    def set_real_value(self):
        text = self.lineRealPart.text()
        self.real_part_load = float(text)
        self.visualisation.set_load_domain(real = float(text))
        
    def change_c_load_lcd(self):
        slider_value = self.c_load_slider.value()
        self.c_load_lcd.display(slider_value)
        self.visualisation.set_c_load(slider_value)

    def change_l_load_lcd(self):
        slider_value = self.l_load_slider.value()
        self.l_load_lcd.display(slider_value)
        self.visualisation.set_l_load(slider_value)
    
    def change_c_tune_lcd(self):
       slider_value = self.c_tune_slider.value()
       self.c_tune_lcd.display(slider_value)
       self.visualisation.set_c_tune(slider_value)
    
    def change_l_tune_lcd(self):
       slider_value = self.l_tune_slider.value()
       self.l_tune_lcd.display(slider_value)
       self.visualisation.set_l_tune(slider_value)

    def set_c_load_lcd(self):
        str_value = self.c_load_edit.text()
        self.c_load_start_value = int(str_value)
        self.c_load_lcd.display(self.c_load_start_value)
        self.c_load_slider.setValue(self.c_load_start_value)

    def call_c_load_setup(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_C_Load_Setup()
        self.ui.setupUi(self.window)
        self.ui.start_value_edit.returnPressed.connect(lambda: set_start_value())
        self.ui.min_value_edit.returnPressed.connect(lambda: set_min_value())
        self.ui.max_value_edit.returnPressed.connect(lambda: set_max_value())
        self.ui.step_size_edit.returnPressed.connect(lambda: set_step_size())
        def set_start_value():
            str_value = self.ui.start_value_edit.text()
            self.c_load_start_value = int(str_value)
            self.c_load_edit.setText(str_value)
            self.c_load_lcd.display(self.c_load_start_value)
            self.c_load_slider.setValue(self.c_load_start_value)
        def set_min_value():
            str_value = self.ui.min_value_edit.text()
            self.c_load_min_value = int(str_value)
            self.c_load_slider.setMinimum(self.c_load_min_value)
        def set_max_value():
            str_value = self.ui.max_value_edit.text()
            self.c_load_max_value = int(str_value)
            self.c_load_slider.setMaximum(self.c_load_max_value)
        def set_step_size():
            str_value = self.ui.step_size_edit.text()
            self.c_load_step_size = int(str_value)
            self.c_load_slider.setSingleStep(self.c_load_step_size)
        self.window.show()

    def set_l_load_lcd(self):
        str_value = self.l_load_edit.text()
        self.l_load_start_value = int(str_value)
        self.l_load_lcd.display(self.l_load_start_value)
        self.l_load_slider.setValue(self.l_load_start_value)
    
    def call_l_load_setup(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_L_Load_Setup()
        self.ui.setupUi(self.window)
        self.ui.start_value_edit.returnPressed.connect(lambda: set_start_value())
        self.ui.min_value_edit.returnPressed.connect(lambda: set_min_value())
        self.ui.max_value_edit.returnPressed.connect(lambda: set_max_value())
        self.ui.step_size_edit.returnPressed.connect(lambda: set_step_size())
        def set_start_value():
            str_value = self.ui.start_value_edit.text()
            self.l_load_start_value = int(str_value)
            self.l_load_edit.setText(str_value)
            self.l_load_lcd.display(self.l_load_start_value)
            self.l_load_slider.setValue(self.l_load_start_value)
        def set_min_value():
            str_value = self.ui.min_value_edit.text()
            self.l_load_min_value = int(str_value)
            self.l_load_slider.setMinimum(self.l_load_min_value)
        def set_max_value():
            str_value = self.ui.max_value_edit.text()
            self.l_load_max_value = int(str_value)
            self.l_load_slider.setMaximum(self.l_load_max_value)
        def set_step_size():
            str_value = self.ui.step_size_edit.text()
            self.l_load_step_size = int(str_value)
            self.l_load_slider.setSingleStep(self.l_load_step_size)
        self.window.show()

    def set_c_tune_lcd(self):
        str_value = self.c_tune_edit.text()
        self.c_tune_start_value = int(str_value)
        self.c_tune_lcd.display(self.c_tune_start_value)
        self.c_tune_slider.setValue(self.c_tune_start_value)

    def call_c_tune_setup(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_C_Tune_Setup()
        self.ui.setupUi(self.window)
        self.ui.start_value_edit.returnPressed.connect(lambda: set_start_value())
        self.ui.min_value_edit.returnPressed.connect(lambda: set_min_value())
        self.ui.max_value_edit.returnPressed.connect(lambda: set_max_value())
        self.ui.step_size_edit.returnPressed.connect(lambda: set_step_size())
        def set_start_value():
            str_value = self.ui.start_value_edit.text()
            self.c_tune_start_value = int(str_value)
            self.c_tune_edit.setText(str_value)
            self.c_tune_lcd.display(self.c_tune_start_value)
            self.c_tune_slider.setValue(self.c_tune_start_value)
        def set_min_value():
            str_value = self.ui.min_value_edit.text()
            self.c_tune_min_value = int(str_value)
            self.c_tune_slider.setMinimum(self.c_tune_min_value)
        def set_max_value():
            str_value = self.ui.max_value_edit.text()
            self.c_tune_max_value = int(str_value)
            self.c_tune_slider.setMaximum(self.c_tune_max_value)
        def set_step_size():
            str_value = self.ui.step_size_edit.text()
            self.c_tune_step_size = int(str_value)
            self.c_tune_slider.setSingleStep(self.c_tune_step_size)
        self.window.show()    

    def set_l_tune_lcd(self):
        str_value = self.l_tune_edit.text()
        self.l_tune_start_value = int(str_value)
        self.l_tune_lcd.display(self.l_tune_start_value)
        self.l_tune_slider.setValue(self.l_tune_start_value)

    def call_l_tune_setup(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_L_Tune_Setup()
        self.ui.setupUi(self.window)
        self.ui.start_value_edit.returnPressed.connect(lambda: set_start_value())
        self.ui.min_value_edit.returnPressed.connect(lambda: set_min_value())
        self.ui.max_value_edit.returnPressed.connect(lambda: set_max_value())
        self.ui.step_size_edit.returnPressed.connect(lambda: set_step_size())
        def set_start_value():
            str_value = self.ui.start_value_edit.text()
            self.l_tune_start_value = int(str_value)
            self.l_tune_edit.setText(str_value)
            self.l_tune_lcd.display(self.l_tune_start_value)
            self.l_tune_slider.setValue(self.l_tune_start_value)
        def set_min_value():
            str_value = self.ui.min_value_edit.text()
            self.l_tune_min_value = int(str_value)
            self.l_tune_slider.setMinimum(self.l_tune_min_value)
        def set_max_value():
            str_value = self.ui.max_value_edit.text()
            self.l_tune_max_value = int(str_value)
            self.l_tune_slider.setMaximum(self.l_tune_max_value)
        def set_step_size():
            str_value = self.ui.step_size_edit.text()
            self.l_tune_step_size = int(str_value)
            self.l_tune_slider.setSingleStep(self.l_tune_step_size)
        self.window.show()    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #open window with settings
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()    
    ui.setupUi(MainWindow)        
    MainWindow.show()
    
    #open window with visualization
    vis_window = QtWidgets.QMainWindow()
    #vis = VisualWindow()
    #vis.setUi(vis_window)
    ui.visualisation.setUi(vis_window)    
    vis_window.show()
    
    sys.exit(app.exec_())   
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../include/mainwindow.ui'
#
# Created: Fri Feb 19 16:22:21 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(771, 517)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.lcdNumberGiven = QtGui.QLCDNumber(self.tab)
        self.lcdNumberGiven.setGeometry(QtCore.QRect(620, 150, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumberGiven.setFont(font)
        self.lcdNumberGiven.setObjectName(_fromUtf8("lcdNumberGiven"))
        self.lcdNumberTresure = QtGui.QLCDNumber(self.tab)
        self.lcdNumberTresure.setGeometry(QtCore.QRect(370, 300, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumberTresure.setFont(font)
        self.lcdNumberTresure.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumberTresure.setAutoFillBackground(False)
        self.lcdNumberTresure.setProperty("intValue", 10)
        self.lcdNumberTresure.setObjectName(_fromUtf8("lcdNumberTresure"))
        self.btnConfirm = QtGui.QPushButton(self.tab)
        self.btnConfirm.setGeometry(QtCore.QRect(500, 130, 91, 91))
        self.btnConfirm.setObjectName(_fromUtf8("btnConfirm"))
        self.horizontalSlider = QtGui.QSlider(self.tab)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 160, 471, 39))
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setProperty("value", 5)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.horizontalSlider.setTickInterval(1)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.btnStartExperiment = QtGui.QPushButton(self.tab)
        self.btnStartExperiment.setGeometry(QtCore.QRect(18, 300, 341, 81))
        self.btnStartExperiment.setObjectName(_fromUtf8("btnStartExperiment"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.groupBox = QtGui.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(20, 150, 261, 151))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEditNaoIP = QtGui.QLineEdit(self.groupBox)
        self.lineEditNaoIP.setGeometry(QtCore.QRect(10, 50, 151, 27))
        self.lineEditNaoIP.setObjectName(_fromUtf8("lineEditNaoIP"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 151, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.btnConnectToNao = QtGui.QPushButton(self.groupBox)
        self.btnConnectToNao.setGeometry(QtCore.QRect(10, 80, 241, 61))
        self.btnConnectToNao.setObjectName(_fromUtf8("btnConnectToNao"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(170, 30, 61, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEditNaoPort = QtGui.QLineEdit(self.groupBox)
        self.lineEditNaoPort.setGeometry(QtCore.QRect(170, 50, 81, 27))
        self.lineEditNaoPort.setInputMask(_fromUtf8(""))
        self.lineEditNaoPort.setObjectName(_fromUtf8("lineEditNaoPort"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 30, 261, 101))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 151, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textEditXML = QtGui.QTextEdit(self.groupBox_2)
        self.textEditXML.setGeometry(QtCore.QRect(0, 50, 211, 41))
        self.textEditXML.setReadOnly(True)
        self.textEditXML.setObjectName(_fromUtf8("textEditXML"))
        self.btnBrowse = QtGui.QPushButton(self.groupBox_2)
        self.btnBrowse.setGeometry(QtCore.QRect(210, 50, 41, 41))
        self.btnBrowse.setObjectName(_fromUtf8("btnBrowse"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(320, 30, 261, 181))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.btnWakeUp = QtGui.QPushButton(self.groupBox_3)
        self.btnWakeUp.setEnabled(False)
        self.btnWakeUp.setGeometry(QtCore.QRect(10, 30, 241, 61))
        self.btnWakeUp.setObjectName(_fromUtf8("btnWakeUp"))
        self.btnRest = QtGui.QPushButton(self.groupBox_3)
        self.btnRest.setEnabled(False)
        self.btnRest.setGeometry(QtCore.QRect(10, 100, 241, 61))
        self.btnRest.setObjectName(_fromUtf8("btnRest"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 771, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "---", None))
        self.btnConfirm.setText(_translate("MainWindow", "CONFIRM", None))
        self.btnStartExperiment.setText(_translate("MainWindow", "START", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Exp", None))
        self.groupBox.setTitle(_translate("MainWindow", "Connection Box", None))
        self.lineEditNaoIP.setInputMask(_translate("MainWindow", "000.000.000.000", None))
        self.lineEditNaoIP.setText(_translate("MainWindow", "192.168.0.1", None))
        self.label.setText(_translate("MainWindow", "NAO IP Address:", None))
        self.btnConnectToNao.setText(_translate("MainWindow", "Connect", None))
        self.label_3.setText(_translate("MainWindow", "Port:", None))
        self.lineEditNaoPort.setText(_translate("MainWindow", "9559", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "XML file", None))
        self.label_2.setText(_translate("MainWindow", "XML path:", None))
        self.btnBrowse.setText(_translate("MainWindow", "...", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Robt Control", None))
        self.btnWakeUp.setText(_translate("MainWindow", "Wake Up", None))
        self.btnRest.setText(_translate("MainWindow", "Rest", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Admin", None))

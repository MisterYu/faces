# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'face_gui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(879, 669)
        self.face_gui_centralWidget = QtWidgets.QWidget(MainWindow)
        self.face_gui_centralWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.face_gui_centralWidget.setObjectName("face_gui_centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.face_gui_centralWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dispaly_verticalLayout = QtWidgets.QVBoxLayout()
        self.dispaly_verticalLayout.setSpacing(6)
        self.dispaly_verticalLayout.setObjectName("dispaly_verticalLayout")
        self.display_label = QtWidgets.QLabel(self.face_gui_centralWidget)
        self.display_label.setText("")
        self.display_label.setObjectName("display_label")
        self.dispaly_verticalLayout.addWidget(self.display_label)
        self.horizontalLayout.addLayout(self.dispaly_verticalLayout)
        self.control_info_Layout = QtWidgets.QVBoxLayout()
        self.control_info_Layout.setSpacing(6)
        self.control_info_Layout.setObjectName("control_info_Layout")
        self.info_label = QtWidgets.QLabel(self.face_gui_centralWidget)
        self.info_label.setText("")
        self.info_label.setObjectName("info_label")
        self.control_info_Layout.addWidget(self.info_label)
        self.start_pushButton = QtWidgets.QPushButton(self.face_gui_centralWidget)
        self.start_pushButton.setObjectName("start_pushButton")
        self.control_info_Layout.addWidget(self.start_pushButton)
        self.stop_pushButton = QtWidgets.QPushButton(self.face_gui_centralWidget)
        self.stop_pushButton.setObjectName("stop_pushButton")
        self.control_info_Layout.addWidget(self.stop_pushButton)
        self.end_pushButton = QtWidgets.QPushButton(self.face_gui_centralWidget)
        self.end_pushButton.setObjectName("end_pushButton")
        self.control_info_Layout.addWidget(self.end_pushButton)
        self.capture_pushButton = QtWidgets.QPushButton(self.face_gui_centralWidget)
        self.capture_pushButton.setObjectName("capture_pushButton")
        self.control_info_Layout.addWidget(self.capture_pushButton)
        self.horizontalLayout.addLayout(self.control_info_Layout)
        MainWindow.setCentralWidget(self.face_gui_centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 879, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_pushButton.setText(_translate("MainWindow", "Start"))
        self.stop_pushButton.setText(_translate("MainWindow", "Stop"))
        self.end_pushButton.setText(_translate("MainWindow", "End"))
        self.capture_pushButton.setText(_translate("MainWindow", "Capture"))


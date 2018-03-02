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
        self.gridLayout = QtWidgets.QGridLayout(self.face_gui_centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.video_frame_label = QtWidgets.QLabel(self.face_gui_centralWidget)
        self.video_frame_label.setText("")
        self.video_frame_label.setObjectName("video_frame_label")
        self.gridLayout.addWidget(self.video_frame_label, 0, 0, 1, 3)
        self.face_detect_checkBox = QtWidgets.QCheckBox(self.face_gui_centralWidget)
        self.face_detect_checkBox.setObjectName("face_detect_checkBox")
        self.gridLayout.addWidget(self.face_detect_checkBox, 3, 2, 1, 1)
        self.start_pushButton = QtWidgets.QPushButton(self.face_gui_centralWidget)
        self.start_pushButton.setObjectName("start_pushButton")
        self.gridLayout.addWidget(self.start_pushButton, 2, 0, 1, 1)
        self.stop_pushButton = QtWidgets.QPushButton(self.face_gui_centralWidget)
        self.stop_pushButton.setObjectName("stop_pushButton")
        self.gridLayout.addWidget(self.stop_pushButton, 3, 0, 1, 1)
        self.face_detect_label = QtWidgets.QLabel(self.face_gui_centralWidget)
        self.face_detect_label.setObjectName("face_detect_label")
        self.gridLayout.addWidget(self.face_detect_label, 3, 1, 1, 1)
        self.info_label = QtWidgets.QLabel(self.face_gui_centralWidget)
        self.info_label.setEnabled(True)
        self.info_label.setObjectName("info_label")
        self.gridLayout.addWidget(self.info_label, 2, 1, 1, 1)
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
        self.face_detect_checkBox.setText(_translate("MainWindow", "Face Detect"))
        self.start_pushButton.setText(_translate("MainWindow", "Start Camera"))
        self.stop_pushButton.setText(_translate("MainWindow", "Stop Camera"))
        self.face_detect_label.setText(_translate("MainWindow", "faces detected:"))
        self.info_label.setText(_translate("MainWindow", "info"))


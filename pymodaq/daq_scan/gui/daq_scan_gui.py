# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'daq_scan_gui_v2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(713, 485)
<<<<<<< HEAD
        self.gridLayout_4 = QtWidgets.QGridLayout(Form)
        self.gridLayout_4.setObjectName("gridLayout_4")
=======
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
>>>>>>> parent of b5f5983... many things
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.settings_layout = QtWidgets.QVBoxLayout()
        self.settings_layout.setObjectName("settings_layout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.quit_pb = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Icon_Library/close2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.quit_pb.setIcon(icon)
        self.quit_pb.setObjectName("quit_pb")
        self.horizontalLayout_2.addWidget(self.quit_pb)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.set_scan_pb = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.set_scan_pb.setObjectName("set_scan_pb")
        self.horizontalLayout_2.addWidget(self.set_scan_pb)
        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.set_ini_positions_pb = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.set_ini_positions_pb.setObjectName("set_ini_positions_pb")
        self.horizontalLayout_2.addWidget(self.set_ini_positions_pb)
        self.start_scan_pb = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.start_scan_pb.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/Icon_Library/run2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.start_scan_pb.setIcon(icon1)
        self.start_scan_pb.setObjectName("start_scan_pb")
        self.horizontalLayout_2.addWidget(self.start_scan_pb)
        self.stop_scan_pb = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.stop_scan_pb.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/Icon_Library/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop_scan_pb.setIcon(icon2)
        self.stop_scan_pb.setObjectName("stop_scan_pb")
        self.horizontalLayout_2.addWidget(self.stop_scan_pb)
        self.settings_layout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.settings_layout)
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_plot1D = QtWidgets.QWidget()
        self.tab_plot1D.setObjectName("tab_plot1D")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_plot1D)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.scan1D_layout = QtWidgets.QVBoxLayout()
        self.scan1D_layout.setObjectName("scan1D_layout")
        self.gridLayout.addLayout(self.scan1D_layout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_plot1D, "")
        self.tab_plot2D = QtWidgets.QWidget()
        self.tab_plot2D.setObjectName("tab_plot2D")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_plot2D)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scan2D_layout = QtWidgets.QVBoxLayout()
        self.scan2D_layout.setObjectName("scan2D_layout")
        self.gridLayout_2.addLayout(self.scan2D_layout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_plot2D, "")
        self.tab_navigator = QtWidgets.QWidget()
        self.tab_navigator.setObjectName("tab_navigator")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_navigator)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.navigator_layout = QtWidgets.QVBoxLayout()
        self.navigator_layout.setObjectName("navigator_layout")
        self.gridLayout_5.addLayout(self.navigator_layout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_navigator, "")
<<<<<<< HEAD
        self.gridLayout_4.addWidget(self.splitter, 0, 0, 1, 1)
        self.StatusBarLayout = QtWidgets.QHBoxLayout()
        self.StatusBarLayout.setObjectName("StatusBarLayout")
        self.gridLayout_4.addLayout(self.StatusBarLayout, 1, 0, 1, 1)
=======
        self.verticalLayout.addWidget(self.splitter)
        self.StatusBarLayout = QtWidgets.QHBoxLayout()
        self.StatusBarLayout.setObjectName("StatusBarLayout")
        self.verticalLayout.addLayout(self.StatusBarLayout)
>>>>>>> parent of b5f5983... many things

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.quit_pb.setToolTip(_translate("Form", "Stop Scan"))
        self.quit_pb.setText(_translate("Form", "Quit"))
        self.set_scan_pb.setToolTip(_translate("Form", "Process the scanner settings and prepare the modules for coming scan"))
        self.set_scan_pb.setText(_translate("Form", "Set Scan"))
        self.set_ini_positions_pb.setToolTip(_translate("Form", "Set Move Modules to their initial position as defined in the current scan"))
        self.set_ini_positions_pb.setText(_translate("Form", "Init Positions"))
        self.start_scan_pb.setToolTip(_translate("Form", "Start Scan"))
        self.stop_scan_pb.setToolTip(_translate("Form", "Stop Scan"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_plot1D), _translate("Form", "1D plot"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_plot2D), _translate("Form", "2D plot"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_navigator), _translate("Form", "Navigator"))
<<<<<<< HEAD
from pymodaq.QtDesigner_Ressources import QtDesigner_ressources_rc
=======
from pymodaq.QtDesigner_Ressources import  QtDesigner_ressources_rc
>>>>>>> parent of b5f5983... many things


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
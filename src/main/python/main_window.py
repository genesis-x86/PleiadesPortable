# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 500)
        MainWindow.setMinimumSize(QtCore.QSize(750, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.menu_bar = QtWidgets.QFrame(self.splitter)
        self.menu_bar.setStyleSheet("background-color: gray;")
        self.menu_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.menu_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_bar.setObjectName("menu_bar")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.menu_bar)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.menu_btn = QtWidgets.QPushButton(self.menu_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_btn.sizePolicy().hasHeightForWidth())
        self.menu_btn.setSizePolicy(sizePolicy)
        self.menu_btn.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.menu_btn.setFont(font)
        self.menu_btn.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 0px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #C681E6;\n"
"}")
        self.menu_btn.setObjectName("menu_btn")
        self.verticalLayout.addWidget(self.menu_btn)

#        self.CLUSTER_BTN = QtWidgets.QPushButton(self.menu_bar)
#        self.CLUSTER_BTN.setMinimumSize(QtCore.QSize(0, 40))
#        self.CLUSTER_BTN.setStyleSheet("QPushButton {\n"
#"    background-color: white;\n"
#"    border: 0px;\n"
#"}\n"
#"QPushButton:hover{\n"
#"    background-color: #C681E6;\n"
#"}")
#        self.CLUSTER_BTN.setObjectName("CLUSTER_BTN")
#        self.verticalLayout.addWidget(self.CLUSTER_BTN)

        
        spacerItem = QtWidgets.QSpacerItem(20, 425, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.content = QtWidgets.QFrame(self.splitter)
        self.content.setMinimumSize(QtCore.QSize(500, 0))
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.content)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.preferences_bar = QtWidgets.QStackedWidget(self.content)
        self.preferences_bar.setMinimumSize(QtCore.QSize(0, 52))
        self.preferences_bar.setMaximumSize(QtCore.QSize(16777215, 51))
        self.preferences_bar.setStyleSheet("background-color: white;")
        self.preferences_bar.setObjectName("preferences_bar")
        self.menu_preferences_2 = QtWidgets.QWidget()
        self.menu_preferences_2.setStyleSheet("")
        self.menu_preferences_2.setObjectName("menu_preferences_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.menu_preferences_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.menu_preferences_2)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.preferences_btn = QtWidgets.QToolButton(self.frame)
        self.preferences_btn.setMinimumSize(QtCore.QSize(90, 50))
        self.preferences_btn.setStyleSheet("QToolButton{\n"
"    background-color: white;\n"
"    border: 0px;\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"    background-color: lightgray;\n"
"    border: 0px;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.preferences_btn.setIcon(icon)
        self.preferences_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.preferences_btn.setObjectName("preferences_btn")
        self.horizontalLayout_2.addWidget(self.preferences_btn)
        self.add_cluster_btn = QtWidgets.QToolButton(self.frame)
        self.add_cluster_btn.setMinimumSize(QtCore.QSize(90, 50))
        self.add_cluster_btn.setStyleSheet("QToolButton{\n"
"    background-color: white;\n"
"    border: 0px;\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"    background-color: lightgray;\n"
"    border: 0px;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_cluster_btn.setIcon(icon1)
        self.add_cluster_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.add_cluster_btn.setObjectName("add_cluster_btn")
        self.horizontalLayout_2.addWidget(self.add_cluster_btn)
        self.import_cluster_btn = QtWidgets.QToolButton(self.frame)
        self.import_cluster_btn.setMinimumSize(QtCore.QSize(90, 50))
        self.import_cluster_btn.setStyleSheet("QToolButton{\n"
"    background-color: white;\n"
"    border: 0px;\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"    background-color: lightgray;\n"
"    border: 0px;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icons/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.import_cluster_btn.setIcon(icon2)
        self.import_cluster_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.import_cluster_btn.setObjectName("import_cluster_btn")
        self.horizontalLayout_2.addWidget(self.import_cluster_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addWidget(self.frame)
        self.preferences_bar.addWidget(self.menu_preferences_2)
        self.cluster_preferences_2 = QtWidgets.QWidget()
        self.cluster_preferences_2.setObjectName("cluster_preferences_2")
        self.preferences_bar.addWidget(self.cluster_preferences_2)
        self.verticalLayout_2.addWidget(self.preferences_bar)
        self.cluster_content = QtWidgets.QStackedWidget(self.content)
        self.cluster_content.setStyleSheet("background-color: white;")
        self.cluster_content.setObjectName("cluster_content")
        self.welcome_page = QtWidgets.QWidget()
        self.welcome_page.setStyleSheet("background-color: white;")
        self.welcome_page.setObjectName("welcome_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.welcome_page)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.welcome_page)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.verticalLayout_5.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5.addWidget(self.frame_4)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.cluster_content.addWidget(self.welcome_page)
        self.cluster_2 = QtWidgets.QWidget()
        self.cluster_2.setObjectName("cluster_2")
        self.cluster_content.addWidget(self.cluster_2)
        self.verticalLayout_2.addWidget(self.cluster_content)
        self.horizontalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuClusters = QtWidgets.QMenu(self.menubar)
        self.menuClusters.setObjectName("menuClusters")
        self.menuHeko = QtWidgets.QMenu(self.menubar)
        self.menuHeko.setObjectName("menuHeko")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuClusters.menuAction())
        self.menubar.addAction(self.menuHeko.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pleiades Portable"))
        self.menu_btn.setText(_translate("MainWindow", "Menu"))
        #self.CLUSTER_BTN.setText(_translate("MainWindow", "Test Cluster"))
        self.preferences_btn.setText(_translate("MainWindow", "Preferences"))
        self.add_cluster_btn.setText(_translate("MainWindow", "New Cluster"))
        self.import_cluster_btn.setText(_translate("MainWindow", "Import"))
        self.label.setText(_translate("MainWindow", "Welcome to Pleiades Portable!"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuClusters.setTitle(_translate("MainWindow", "Clusters"))
        self.menuHeko.setTitle(_translate("MainWindow", "Help"))

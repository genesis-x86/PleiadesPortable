# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_cluster_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_new_cluster_dialog(object):
    def setupUi(self, new_cluster_dialog):
        new_cluster_dialog.setObjectName("new_cluster_dialog")
        new_cluster_dialog.resize(350, 477)
        new_cluster_dialog.setMinimumSize(QtCore.QSize(350, 0))
        new_cluster_dialog.setMaximumSize(QtCore.QSize(350, 500))
        new_cluster_dialog.setModal(True)
        self.name_address_table = QtWidgets.QTableWidget(new_cluster_dialog)
        self.name_address_table.setGeometry(QtCore.QRect(10, 210, 331, 190))
        self.name_address_table.setMinimumSize(QtCore.QSize(0, 190))
        self.name_address_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.name_address_table.setObjectName("name_address_table")
        self.name_address_table.setColumnCount(2)
        self.name_address_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.name_address_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.name_address_table.setHorizontalHeaderItem(1, item)
        self.name_address_table.horizontalHeader().setCascadingSectionResizes(False)
        self.name_address_table.horizontalHeader().setStretchLastSection(True)
        self.name_address_table.verticalHeader().setCascadingSectionResizes(False)
        self.frame = QtWidgets.QFrame(new_cluster_dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 321, 45))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cluster_name = QtWidgets.QLineEdit(self.frame)
        self.cluster_name.setObjectName("cluster_name")
        self.horizontalLayout.addWidget(self.cluster_name)
        self.frame_2 = QtWidgets.QFrame(new_cluster_dialog)
        self.frame_2.setGeometry(QtCore.QRect(0, 50, 321, 45))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.username = QtWidgets.QLineEdit(self.frame_2)
        self.username.setObjectName("username")
        self.horizontalLayout_2.addWidget(self.username)
        self.frame_3 = QtWidgets.QFrame(new_cluster_dialog)
        self.frame_3.setGeometry(QtCore.QRect(0, 100, 321, 45))
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.password = QtWidgets.QLineEdit(self.frame_3)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.horizontalLayout_3.addWidget(self.password)
        self.frame_4 = QtWidgets.QFrame(new_cluster_dialog)
        self.frame_4.setGeometry(QtCore.QRect(0, 150, 321, 45))
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.confirm_password = QtWidgets.QLineEdit(self.frame_4)
        self.confirm_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_password.setObjectName("confirm_password")
        self.horizontalLayout_4.addWidget(self.confirm_password)
        self.add_node_btn = QtWidgets.QPushButton(new_cluster_dialog)
        self.add_node_btn.setGeometry(QtCore.QRect(280, 400, 30, 30))
        self.add_node_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.add_node_btn.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.add_node_btn.setFont(font)
        self.add_node_btn.setObjectName("add_node_btn")
        self.remove_node_btn = QtWidgets.QPushButton(new_cluster_dialog)
        self.remove_node_btn.setGeometry(QtCore.QRect(310, 400, 30, 30))
        self.remove_node_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.remove_node_btn.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.remove_node_btn.setFont(font)
        self.remove_node_btn.setObjectName("remove_node_btn")
        self.save_btn = QtWidgets.QPushButton(new_cluster_dialog)
        self.save_btn.setGeometry(QtCore.QRect(270, 440, 71, 25))
        self.save_btn.setObjectName("save_btn")
        self.abort_btn = QtWidgets.QPushButton(new_cluster_dialog)
        self.abort_btn.setGeometry(QtCore.QRect(200, 440, 71, 25))
        self.abort_btn.setObjectName("abort_btn")

        self.retranslateUi(new_cluster_dialog)
        QtCore.QMetaObject.connectSlotsByName(new_cluster_dialog)

    def retranslateUi(self, new_cluster_dialog):
        _translate = QtCore.QCoreApplication.translate
        new_cluster_dialog.setWindowTitle(_translate("new_cluster_dialog", "Dialog"))
        item = self.name_address_table.horizontalHeaderItem(0)
        item.setText(_translate("new_cluster_dialog", "Name"))
        item = self.name_address_table.horizontalHeaderItem(1)
        item.setText(_translate("new_cluster_dialog", "IP Address"))
        self.label.setText(_translate("new_cluster_dialog", "Cluster Name:"))
        self.label_2.setText(_translate("new_cluster_dialog", "User Name:"))
        self.label_3.setText(_translate("new_cluster_dialog", "Password:"))
        self.label_4.setText(_translate("new_cluster_dialog", "Confirm Password:"))
        self.add_node_btn.setText(_translate("new_cluster_dialog", "+"))
        self.remove_node_btn.setText(_translate("new_cluster_dialog", "-"))
        self.save_btn.setText(_translate("new_cluster_dialog", "Save"))
        self.abort_btn.setText(_translate("new_cluster_dialog", "Abort"))

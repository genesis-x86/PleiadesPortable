from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QDialog
from PySide2.QtWidgets import QMessageBox
from PySide2.QtWidgets import QPushButton
from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtCore, QtGui, QtWidgets


import sys
import os
import yaml
from pprint import pprint
from main_window import Ui_MainWindow
from new_cluster_dialog import Ui_new_cluster_dialog

_translate = QtCore.QCoreApplication.translate




class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.menu_buttons = []
        self.setupUi(self)
        self.load_config()
        self.load_cluster_config()

        self.add_cluster_btn.clicked.connect(self.add_cluster_dialog)
        self.menu_btn.clicked.connect(self.change_home)


    def change_home(self):
        self.content.setCurrentWidget(self.welcome_page)
        self.preferences_bar.setCurrentWidget(self.menu_preferences)


    # Remember to fill this out later
    def load_cluster_config(self):
        os.chdir(f'./config')

        if len(self.clusters) != len(os.listdir()):
            self.show_warning("Warning: App config file does not match with cluster config folder")

        if len(self.clusters) != 0:
            for cluster in self.clusters:
                self.add_config(cluster)

    def load_config(self):
        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath)
        os.chdir(dname)

        os.chdir(f'../../../etc')
        
        if os.path.exists(f'./app_config.yaml') is False:

            self.preferences = {
                "preferences": {
                    "clusters": []
                }
            }

            with open(f'./app_config.yaml', "x") as file:
                yaml.safe_dump(self.preferences, file)

        else:
            with open(f'./app_config.yaml', "r") as file:
                self.preferences = yaml.safe_load(file)

        self.clusters = self.preferences["preferences"]["clusters"]



    def add_cluster_dialog(self):
        dialog = QDialog(self)
        add_cluster = Ui_new_cluster_dialog()
        add_cluster.setupUi(dialog)

        add_cluster.add_node_btn.clicked.connect(lambda: self.add_node(add_cluster))
        add_cluster.remove_node_btn.clicked.connect(lambda: self.remove_node(add_cluster))

        add_cluster.save_btn.clicked.connect(lambda: self.check(add_cluster, dialog))
        add_cluster.abort_btn.clicked.connect(dialog.close)
        dialog.show()
        

    def check(self, dialog, qd):
        if not dialog.username.text():
            self.show_warning("Error: No username specified")
        elif not dialog.cluster_name.text():
            self.show_warning("Error: No cluster name specified")
        elif not dialog.password.text():
            self.show_warning("Error: No password specified")
        elif dialog.password.text() != dialog.confirm_password.text():
            self.show_warning("Error: Passwords do not match")
        
        table_data = self.read_table(dialog.name_address_table)
        if len(table_data) % 2 != 0 or len(table_data) == 0:
            self.show_warning("Error: Invalid input for nodes")
        else:
            qd.close()
            self.write_config(dialog.cluster_name.text(), dialog.username.text(), dialog.password.text(), table_data)
            self.add_config(dialog.cluster_name.text())

    def show_warning(self, error_message):
        msg = QMessageBox()
        msg.setModal(True)
        msg.setIcon(QMessageBox.Warning)
        msg.setText(error_message)
        msg.setWindowTitle("Error")
        msg.exec_()


    def write_config(self, cluster_name, username, password, nodes):
        print(os.getcwd())

        cluster_data = {
            cluster_name : {
                "username": username,
                "password": password,
                "nodes": nodes
            }
        }


        with open(f'./{cluster_name}.yaml', "x") as file:
            yaml.dump(cluster_data, file)

        with open(f'../app_config.yaml', "r") as file:
            config = yaml.safe_load(file)
            config["preferences"]["clusters"].append(cluster_name)
        with open(f'../app_config.yaml','w') as file:
            yaml.safe_dump(config, file)
        
        
    def add_config(self, config_path):

        page = ClusterPage(f'{config_path}.yaml', self.menu_bar)
        self.verticalLayout.insertWidget(1, page.cluster_btn)
        self.buttonGroup.addButton(page.cluster_btn)
        self.content.addWidget(page.cluster_page)
        self.menu_buttons.append(page.cluster_btn)

        for i, button in enumerate(self.menu_buttons):
            # Musicamante
            button.clicked.connect(lambda button=button, i=i: self.change_page(button, i))

    def change_page(self, page, index):
        
        self.content.setCurrentIndex(index+1)
        self.preferences_bar.setCurrentWidget(self.cluster_preferences)
        

    def add_node(self, dialog):
        table_rows = dialog.name_address_table.rowCount()
        dialog.name_address_table.insertRow(table_rows)
    def remove_node(self, dialog):
        if dialog.name_address_table.rowCount() > 0:
            dialog.name_address_table.removeRow(dialog.name_address_table.rowCount() - 1)
    def read_table(self, table):
        table_data = []
        for row in range(table.rowCount()):
            for column in range(table.columnCount()):
                if table.item(row, column) == None:
                    pass
                else:
                    table_data.append(table.item(row, column).text())
        return table_data
        
        


class ClusterPage(QtWidgets.QWidget):
    # Takes absolute path
    def __init__(self, config_path, parent):
        super().__init__()
        self.menu_bar = parent
        with open(config_path, "r") as file:
            self.config = yaml.safe_load(file)
            self.cluster_name = list(self.config.keys())[0]
            self.username = self.config[self.cluster_name]["username"]
            self.nodes = self.config[self.cluster_name]["nodes"]
            self.password = self.config[self.cluster_name]["password"]

        self.create_page(self.cluster_name, self.username, self.password, self.nodes)

    def create_page(self, cluster_name, mpi_username, password, nodes):

        self.cluster_btn = QPushButton(self.menu_bar)
        self.cluster_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.cluster_btn.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 0px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #C681E6;\n"
"}\n"
"QPushButton:checked{\n"
"    background-color: #C681E6;\n"
"}")
        self.cluster_btn.setObjectName(cluster_name)
        
        self.cluster_btn.setText(cluster_name)
        self.cluster_btn.setCheckable(True)


        self.cluster_page = QtWidgets.QWidget()
        self.cluster_page.setObjectName(f'{cluster_name}_page')
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.cluster_page)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(f'{cluster_name}_layout')
        self.cluster_title_frame = QtWidgets.QFrame(self.cluster_page)
        self.cluster_title_frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.cluster_title_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cluster_title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cluster_title_frame.setObjectName(f'{cluster_name}_title_frame')
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.cluster_title_frame)
        self.verticalLayout_8.setObjectName(f'{cluster_name}_layout_2')
        self.cluster_title = QtWidgets.QLabel(self.cluster_title_frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cluster_title.setFont(font)
        self.cluster_title.setObjectName(f'{cluster_name}_title')
        self.verticalLayout_8.addWidget(self.cluster_title)
        self.verticalLayout_7.addWidget(self.cluster_title_frame)
        self.cluster_page_content = QtWidgets.QFrame(self.cluster_page)
        self.cluster_page_content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cluster_page_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cluster_page_content.setObjectName(f'{cluster_name}_page_content')
        self.verticalLayout_7.addWidget(self.cluster_page_content)
        self.cluster_title.setText(cluster_name)
        



    


if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = MainWindow()
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)

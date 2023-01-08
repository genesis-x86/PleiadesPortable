from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QDialog
from PySide2.QtWidgets import QMessageBox
from PySide2.QtWidgets import QPushButton
from PySide2 import QtCore

import sys
from main_window import Ui_MainWindow
from new_cluster_dialog import Ui_new_cluster_dialog

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add_cluster_btn.clicked.connect(self.add_cluster_dialog)


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
            self.add_config(dialog.cluster_name.text(), dialog.username.text(), dialog.password.text(), table_data)

    def show_warning(self, error_message):
        msg = QMessageBox()
        msg.setModal(True)
        msg.setIcon(QMessageBox.Warning)
        msg.setText(error_message)
        msg.setWindowTitle("Error")
        msg.exec_()


    def add_config(self, cluster_name, username, password, nodes):
        self.CLUSTER_BTN = QPushButton(self.menu_bar)
        self.CLUSTER_BTN.setMinimumSize(QtCore.QSize(0, 40))
        self.CLUSTER_BTN.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 0px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #C681E6;\n"
"}")
        self.CLUSTER_BTN.setObjectName(cluster_name)
        self.verticalLayout.insertWidget(1, self.CLUSTER_BTN)
        self.CLUSTER_BTN.setText(cluster_name)




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
        
    


if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = MainWindow()
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
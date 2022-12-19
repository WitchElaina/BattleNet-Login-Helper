import account
import login
import settings
import sys
from mainwindow_ui import Ui_MainWindow
from add_dialog_ui import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem,  QDialog, QMessageBox, QHeaderView
from PyQt5.QtGui import QFont


def show_msg(content, title='Message'):
    msg = QMessageBox()
    msg.setText(content)
    msg.setWindowTitle(title)
    msg.exec()


class AddGUI(QDialog, Ui_Dialog):
    def __init__(self):
        super(AddGUI, self).__init__(parent=None)
        self.setupUi(self)

    def return_value(self):
        ret = [self.lineEdit_name.text(), self.lineEdit_acc.text(), self.lineEdit_pwd.text(),
               self.comboBox_class.currentText()]
        return ret


class MainWindowGUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # init
        super(MainWindowGUI, self).__init__(None)
        self.setupUi(self)
        # get version
        self.label_ver.setText(settings.VERSION)
        # bind
        self.checkBox_pwd.clicked.connect(self.pwd_checked)
        self.pushButton_add.clicked.connect(self.add_account)
        self.pushButton_delete.clicked.connect(self.delete_account)
        self.tableWidget.cellChanged.connect(self.edit_account)
        self.pushButton_login.clicked.connect(self.login)
        # init table
        self.tableWidget.setColumnCount(4)
        self.tableWidget.hideColumn(2)
        self.tableWidget.setHorizontalHeaderLabels(['Name', 'Account', 'Password', 'Area'])
        self.reload_table()
        self.tableWidget.selectRow(0)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def reload_table(self):
        self.tableWidget.cellChanged.disconnect()
        accounts = account.get_accounts()
        if len(accounts) != self.tableWidget.rowCount():
            self.tableWidget.setRowCount(len(accounts))
        cur_row = 0
        for acc in accounts:
            for i in range(4):
                self.tableWidget.setItem(cur_row, i, QTableWidgetItem(acc[i]))
            cur_row += 1
        self.tableWidget.cellChanged.connect(self.edit_account)

    def add_account(self):
        add_window = AddGUI()
        add_window.exec()
        args = add_window.return_value()
        try:
            account.add_account(args[0], args[1], args[2], args[3])
        except Exception as err:
            # show_msg(str(err))
            pass
        else:
            self.reload_table()

    def delete_account(self):
        row = self.tableWidget.currentRow()
        name = self.tableWidget.item(row, 0).text()
        account.delete_account(name)
        self.reload_table()

    def edit_account(self):
        row = self.tableWidget.currentRow()
        args = []
        name = self.tableWidget.item(row, 0).text()
        for i in range(4):
            args.append(self.tableWidget.item(row, i).text())
        account.edit_account(name, args)
        print(args)
        self.reload_table()

    def pwd_checked(self):
        if not self.checkBox_pwd.isChecked():
            self.tableWidget.hideColumn(2)
        else:
            self.tableWidget.showColumn(2)

    def login(self):
        row = self.tableWidget.currentRow()
        name = self.tableWidget.item(row, 0).text()
        login.login(account.get_login_args(name))


if __name__ == '__main__':
    app = QApplication([])
    f = QFont("Microsoft YaHei")
    app.setFont(f)
    window = MainWindowGUI()
    window.show()
    sys.exit(app.exec_())

import sys
import random
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('game_screen.ui', self)
        # self.btn_addtable.clicked.connect(self.addtable)
        # self.tableWidget.setColumnCount(5)
        # self.tableWidget.setRowCount(100)
        # self.tableWidget.setItem(0,0,QtWidgets.QTableWidgetItem("Hello (1,1)"))
        # self.tableWidget.setItem(0,1, QtWidgets.QTableWidgetItem("World (1,2)"))
        # self.tableWidget.setItem(1,0, QtWidgets.QTableWidgetItem("Issa (2,1)"))
        # self.tableWidget.setItem(1,1, QtWidgets.QTableWidgetItem("Mario (2,2)"))
        # self.tableWidget.setItem(2,0, QtWidgets.QTableWidgetItem("Neel (3,1)"))
        # self.tableWidget.setItem(2,1, QtWidgets.QTableWidgetItem("BHmani (3,2)"))
        # self.tableWidget.setItem(3,0, QtWidgets.QTableWidgetItem("is (4,1)"))
        # self.tableWidget.setItem(3,1, QtWidgets.QTableWidgetItem("ma (4,2)"))
        # self.tableWidget.setItem(4,0, QtWidgets.QTableWidgetItem("homi e(4,2)"))
        # self.tableWidget.setRowCount(4)
        # self.tableWidget.setColumnCount(4)
        self.setStyleSheet(" background-image: url(a.png);")
        self.show()

    def addtable(self):
        self.edittablename.setText("Do stuff")
        print(random.randint(1,100))
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
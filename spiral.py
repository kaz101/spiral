# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spiral.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(167, 637)
        MainWindow.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_item_box = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_item_box.sizePolicy().hasHeightForWidth())
        self.add_item_box.setSizePolicy(sizePolicy)
        self.add_item_box.setObjectName("add_item_box")
        self.verticalLayout.addWidget(self.add_item_box)
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setObjectName("add_button")
        self.verticalLayout.addWidget(self.add_button)
        self.remove_button = QtWidgets.QPushButton(self.centralwidget)
        self.remove_button.setObjectName("remove_button")
        self.verticalLayout.addWidget(self.remove_button)
        self.interests_list_box = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.interests_list_box.sizePolicy().hasHeightForWidth())
        self.interests_list_box.setSizePolicy(sizePolicy)
        self.interests_list_box.setObjectName("interests_list_box")
        self.verticalLayout.addWidget(self.interests_list_box)
        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button.setObjectName("next_button")
        self.verticalLayout.addWidget(self.next_button)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Spiral"))
        self.add_button.setText(_translate("MainWindow", "Add"))
        self.remove_button.setText(_translate("MainWindow", "Remove"))
        self.next_button.setText(_translate("MainWindow", "Next"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

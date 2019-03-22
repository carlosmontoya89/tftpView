# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os

def resource_path(relative_path):
  if hasattr(sys, '_MEIPASS'):
      return os.path.join(sys._MEIPASS, relative_path)
  return os.path.join(os.path.abspath('.'), relative_path)


class Ui_Consultar_Scripts(object):
    def setupUi(self, Consultar_Scripts):
        Consultar_Scripts.setObjectName("Consultar_Scripts")
        Consultar_Scripts.setEnabled(True)
        Consultar_Scripts.resize(718, 490)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("tso_mobile.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Consultar_Scripts.setWindowIcon(icon)
        Consultar_Scripts.setIconSize(QtCore.QSize(28, 28))
        self.centralwidget = QtWidgets.QWidget(Consultar_Scripts)
        self.centralwidget.setObjectName("centralwidget")
        self.assignedScripts = QtWidgets.QTableWidget(self.centralwidget)
        self.assignedScripts.setGeometry(QtCore.QRect(30, 220, 631, 201))
        self.assignedScripts.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.assignedScripts.setAlternatingRowColors(True)
        self.assignedScripts.setRowCount(0)
        self.assignedScripts.setColumnCount(0)
        self.assignedScripts.setObjectName("assignedScripts")
        self.assignedScripts.verticalHeader().setVisible(False)
        self.assignedScripts.verticalHeader().setHighlightSections(False)
        self.serialNumber = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.serialNumber.setGeometry(QtCore.QRect(30, 40, 151, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(12)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serialNumber.sizePolicy().hasHeightForWidth())
        self.serialNumber.setSizePolicy(sizePolicy)
        self.serialNumber.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhMultiLine)
        self.serialNumber.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.serialNumber.setObjectName("serialNumber")
        self.queryScripts = QtWidgets.QPushButton(self.centralwidget)
        self.queryScripts.setGeometry(QtCore.QRect(200, 40, 121, 23))
        self.queryScripts.setObjectName("queryScripts")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 201, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 200, 161, 20))
        self.label_2.setObjectName("label_2")
        Consultar_Scripts.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Consultar_Scripts)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 718, 31))
        self.menubar.setObjectName("menubar")
        Consultar_Scripts.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(Consultar_Scripts)
        self.statusBar.setObjectName("statusBar")
        Consultar_Scripts.setStatusBar(self.statusBar)
        self.retranslateUi(Consultar_Scripts)
        QtCore.QMetaObject.connectSlotsByName(Consultar_Scripts)

    def retranslateUi(self, Consultar_Scripts):
        _translate = QtCore.QCoreApplication.translate
        Consultar_Scripts.setWindowTitle(_translate("Consultar_Scripts", "SCRIPTS TSO MOBILE"))
        Consultar_Scripts.setAccessibleName(_translate("Consultar_Scripts", "Consultar Scripts"))
        self.assignedScripts.setAccessibleName(_translate("Consultar_Scripts", "showScripts"))
        self.serialNumber.setAccessibleName(_translate("Consultar_Scripts", "serialNumbers"))
        self.queryScripts.setText(_translate("Consultar_Scripts", "Consultar Script"))
        self.label.setText(_translate("Consultar_Scripts", "NUMEROS SERIALES"))
        self.label_2.setText(_translate("Consultar_Scripts", "SCRIPT ASIGNADOS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Consultar_Scripts = QtWidgets.QMainWindow()
    ui = Ui_Consultar_Scripts()
    ui.setupUi(Consultar_Scripts)
    Consultar_Scripts.show()
    sys.exit(app.exec_())


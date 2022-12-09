# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1141, 691)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tap_1 = QWidget()
        self.tap_1.setObjectName(u"tap_1")
        self.gridLayout_2 = QGridLayout(self.tap_1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.tap_1)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.OrigenY_spinBox = QSpinBox(self.groupBox)
        self.OrigenY_spinBox.setObjectName(u"OrigenY_spinBox")

        self.gridLayout.addWidget(self.OrigenY_spinBox, 7, 1, 1, 1)

        self.Red_spinBox = QSpinBox(self.groupBox)
        self.Red_spinBox.setObjectName(u"Red_spinBox")

        self.gridLayout.addWidget(self.Red_spinBox, 11, 1, 1, 1)

        self.Velocidad_spinBox = QSpinBox(self.groupBox)
        self.Velocidad_spinBox.setObjectName(u"Velocidad_spinBox")

        self.gridLayout.addWidget(self.Velocidad_spinBox, 10, 1, 1, 1)

        self.Green_spinBox = QSpinBox(self.groupBox)
        self.Green_spinBox.setObjectName(u"Green_spinBox")

        self.gridLayout.addWidget(self.Green_spinBox, 12, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 9, 0, 1, 1)

        self.DestinoX_spinBox = QSpinBox(self.groupBox)
        self.DestinoX_spinBox.setObjectName(u"DestinoX_spinBox")

        self.gridLayout.addWidget(self.DestinoX_spinBox, 8, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 11, 0, 1, 1)

        self.Id_spinBox = QSpinBox(self.groupBox)
        self.Id_spinBox.setObjectName(u"Id_spinBox")
        self.Id_spinBox.setCursor(QCursor(Qt.IBeamCursor))
        self.Id_spinBox.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.Id_spinBox, 2, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 8, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 10, 0, 1, 1)

        self.Agre_Final_buttom = QPushButton(self.groupBox)
        self.Agre_Final_buttom.setObjectName(u"Agre_Final_buttom")

        self.gridLayout.addWidget(self.Agre_Final_buttom, 17, 0, 1, 2)

        self.Mostrar_buttom = QPushButton(self.groupBox)
        self.Mostrar_buttom.setObjectName(u"Mostrar_buttom")

        self.gridLayout.addWidget(self.Mostrar_buttom, 19, 0, 1, 2)

        self.Agre_Inicio_Buttom = QPushButton(self.groupBox)
        self.Agre_Inicio_Buttom.setObjectName(u"Agre_Inicio_Buttom")

        self.gridLayout.addWidget(self.Agre_Inicio_Buttom, 18, 0, 1, 2)

        self.Blue_spinBox = QSpinBox(self.groupBox)
        self.Blue_spinBox.setObjectName(u"Blue_spinBox")

        self.gridLayout.addWidget(self.Blue_spinBox, 13, 1, 1, 1)

        self.OrigenX_spinBox = QSpinBox(self.groupBox)
        self.OrigenX_spinBox.setObjectName(u"OrigenX_spinBox")

        self.gridLayout.addWidget(self.OrigenX_spinBox, 6, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 12, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 13, 0, 1, 1)

        self.DestinoY_spinBox = QSpinBox(self.groupBox)
        self.DestinoY_spinBox.setObjectName(u"DestinoY_spinBox")

        self.gridLayout.addWidget(self.DestinoY_spinBox, 9, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 20, 0, 1, 2)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.salida = QPlainTextEdit(self.tap_1)
        self.salida.setObjectName(u"salida")

        self.gridLayout_2.addWidget(self.salida, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tap_1, "")
        self.tap_2 = QWidget()
        self.tap_2.setObjectName(u"tap_2")
        self.gridLayout_4 = QGridLayout(self.tap_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.txt_line = QLineEdit(self.tap_2)
        self.txt_line.setObjectName(u"txt_line")

        self.gridLayout_4.addWidget(self.txt_line, 1, 0, 1, 1)

        self.Buscar_Butonn = QPushButton(self.tap_2)
        self.Buscar_Butonn.setObjectName(u"Buscar_Butonn")

        self.gridLayout_4.addWidget(self.Buscar_Butonn, 1, 2, 1, 1)

        self.Mostrar_Dates = QPushButton(self.tap_2)
        self.Mostrar_Dates.setObjectName(u"Mostrar_Dates")

        self.gridLayout_4.addWidget(self.Mostrar_Dates, 1, 3, 1, 1)

        self.tabla = QTableWidget(self.tap_2)
        self.tabla.setObjectName(u"tabla")

        self.gridLayout_4.addWidget(self.tabla, 0, 0, 1, 4)

        self.Btn_Order = QPushButton(self.tap_2)
        self.Btn_Order.setObjectName(u"Btn_Order")

        self.gridLayout_4.addWidget(self.Btn_Order, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tap_2, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1141, 22))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Destino y:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Rojo:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Origen Y", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Destino x: ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.Agre_Final_buttom.setText(QCoreApplication.translate("MainWindow", u"Agregar FInal", None))
        self.Mostrar_buttom.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.Agre_Inicio_Buttom.setText(QCoreApplication.translate("MainWindow", u"Agregar inicio", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Verde:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Azul:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Origen X", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tap_1), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.txt_line.setText("")
        self.txt_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Id de particula", None))
        self.Buscar_Butonn.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.Mostrar_Dates.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.Btn_Order.setText(QCoreApplication.translate("MainWindow", u"Ordenar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tap_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi


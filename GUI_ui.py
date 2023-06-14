# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUIuEzNxj.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 550)
        MainWindow.setMaximumSize(QSize(16777215, 550))
        MainWindow.setStyleSheet(u"*{\n"
"	color: #000;\n"
"	border: none;\n"
"}\n"
"#centralwidget{\n"
"	background-color: rgb(250, 234, 249)\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(16777215, 550))
        self.centralwidget.setStyleSheet(u"#LeftMenu{\n"
"  background-color: #b29bfd\n"
"}\n"
"QLineEdit{\n"
"  background:transparent;\n"
"}\n"
"#SearchFrame{\n"
"  border-radius: 10px;\n"
"  border: 0.8px solid #572364;\n"
"}\n"
"#pushButton_3{\n"
"  background-color: #ffffff;\n"
"  padding: 10 px 5px;\n"
"  text-align: left;\n"
"  border-top-left-radius: 20px;\n"
"}\n"
"QPushButton{\n"
"	padding: 10px 5px;\n"
"}\n"
"#frame{\n"
"	background-color:#C8A2C8;\n"
"	border-top-left-radius: 20px;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftMenu = QCustomSlideMenu(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenu.sizePolicy().hasHeightForWidth())
        self.leftMenu.setSizePolicy(sizePolicy)
        self.leftMenu.setMinimumSize(QSize(200, 0))
        self.leftMenu.setMaximumSize(QSize(200, 550))
        self.leftMenu.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.leftMenu)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 9, 0, -1)
        self.frame = QFrame(self.leftMenu)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 550))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Button_1 = QPushButton(self.frame_2)
        self.Button_1.setObjectName(u"Button_1")
        font = QFont()
        font.setFamily(u"Bodoni MT")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Button_1.setFont(font)
        icon = QIcon()
        icon.addFile(u":/purple_icons/assets/purple/file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_1.setIcon(icon)
        self.Button_1.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.Button_1, 0, Qt.AlignVCenter)

        self.Button_2 = QPushButton(self.frame_2)
        self.Button_2.setObjectName(u"Button_2")
        self.Button_2.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/purple_icons/assets/purple/layers.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_2.setIcon(icon1)
        self.Button_2.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.Button_2)

        self.Button_5 = QPushButton(self.frame_2)
        self.Button_5.setObjectName(u"Button_5")
        self.Button_5.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/purple_icons/assets/purple/compass.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_5.setIcon(icon2)
        self.Button_5.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.Button_5)

        self.Button_3 = QPushButton(self.frame_2)
        self.Button_3.setObjectName(u"Button_3")
        font1 = QFont()
        font1.setFamily(u"Bodoni MT")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.Button_3.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/purple_icons/assets/purple/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_3.setIcon(icon3)
        self.Button_3.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.Button_3)

        self.Button_4 = QPushButton(self.frame_2)
        self.Button_4.setObjectName(u"Button_4")
        self.Button_4.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u":/purple_icons/assets/purple/codesandbox.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_4.setIcon(icon4)
        self.Button_4.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.Button_4)

        self.Button_6 = QPushButton(self.frame_2)
        self.Button_6.setObjectName(u"Button_6")
        self.Button_6.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u":/purple_icons/assets/purple/aperture.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_6.setIcon(icon5)
        self.Button_6.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.Button_6)

        self.Button_7 = QPushButton(self.frame_2)
        self.Button_7.setObjectName(u"Button_7")
        self.Button_7.setFont(font1)
        self.Button_7.setIcon(icon5)
        self.Button_7.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.Button_7)

        self.Button_8 = QPushButton(self.frame_2)
        self.Button_8.setObjectName(u"Button_8")
        self.Button_8.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u":/purple_icons/assets/purple/slack.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_8.setIcon(icon6)
        self.Button_8.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.Button_8)

        self.Button_9 = QPushButton(self.frame_2)
        self.Button_9.setObjectName(u"Button_9")
        self.Button_9.setFont(font1)
        self.Button_9.setIcon(icon6)
        self.Button_9.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.Button_9)

        self.Button_10 = QPushButton(self.frame_2)
        self.Button_10.setObjectName(u"Button_10")
        self.Button_10.setFont(font1)
        icon7 = QIcon()
        icon7.addFile(u":/purple_icons/assets/purple/figma.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_10.setIcon(icon7)
        self.Button_10.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.Button_10)

        self.Button_11 = QPushButton(self.frame_2)
        self.Button_11.setObjectName(u"Button_11")
        self.Button_11.setFont(font1)
        self.Button_11.setIcon(icon7)
        self.Button_11.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.Button_11)


        self.verticalLayout_4.addWidget(self.frame_2, 0, Qt.AlignTop)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.leftMenu)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        self.mainBody.setMaximumSize(QSize(16777215, 550))
        self.widget_3 = QWidget(self.mainBody)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(9, 9, 508, 171))
        self.header = QWidget(self.widget_3)
        self.header.setObjectName(u"header")
        self.header.setGeometry(QRect(9, -1, 491, 181))
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_9 = QWidget(self.header)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.menuBtn = QPushButton(self.widget_9)
        self.menuBtn.setObjectName(u"menuBtn")
        icon8 = QIcon()
        icon8.addFile(u":/purple_icons/assets/purple/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon8)
        self.menuBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.menuBtn)

        self.label_2 = QLabel(self.widget_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_2)


        self.horizontalLayout_2.addWidget(self.widget_9, 0, Qt.AlignTop)

        self.widget_10 = QWidget(self.header)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_6 = QVBoxLayout(self.widget_10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.SearchFrame = QFrame(self.widget_10)
        self.SearchFrame.setObjectName(u"SearchFrame")
        self.SearchFrame.setFrameShape(QFrame.StyledPanel)
        self.SearchFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.SearchFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.SearchFrame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(30, 30))
        self.label.setMaximumSize(QSize(30, 30))
        self.label.setPixmap(QPixmap(u":/purple_icons/assets/purple/folder.svg"))
        self.label.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label)

        self.filename = QLineEdit(self.SearchFrame)
        self.filename.setObjectName(u"filename")

        self.horizontalLayout_4.addWidget(self.filename)


        self.verticalLayout_6.addWidget(self.SearchFrame)

        self.browse = QPushButton(self.widget_10)
        self.browse.setObjectName(u"browse")
        self.browse.setFont(font1)
        icon9 = QIcon()
        icon9.addFile(u":/purple_icons/assets/purple/file-text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.browse.setIcon(icon9)
        self.browse.setIconSize(QSize(30, 30))

        self.verticalLayout_6.addWidget(self.browse)

        self.limpiar = QPushButton(self.widget_10)
        self.limpiar.setObjectName(u"limpiar")
        self.limpiar.setFont(font1)
        icon10 = QIcon()
        icon10.addFile(u":/purple_icons/assets/purple/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.limpiar.setIcon(icon10)
        self.limpiar.setIconSize(QSize(25, 25))

        self.verticalLayout_6.addWidget(self.limpiar)


        self.horizontalLayout_2.addWidget(self.widget_10, 0, Qt.AlignTop)

        self.stackedWidget = QStackedWidget(self.mainBody)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(9, 180, 518, 350))
        self.stackedWidget.setMaximumSize(QSize(16777215, 350))
        self.stackedWidget.setStyleSheet(u"QLineEdit{\n"
"  background:rgb(242, 175, 255);\n"
"}")
        self.page_0 = QWidget()
        self.page_0.setObjectName(u"page_0")
        self.verticalLayout_3 = QVBoxLayout(self.page_0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_7 = QWidget(self.page_0)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Datos = QLabel(self.widget_7)
        self.Datos.setObjectName(u"Datos")
        self.Datos.setFont(font1)

        self.horizontalLayout_3.addWidget(self.Datos)


        self.verticalLayout_3.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.page_0)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMaximumSize(QSize(16777215, 300))
        self.gridLayout_2 = QGridLayout(self.widget_8)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableWidget = QTableWidget(self.widget_8)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.widget_8)

        self.stackedWidget.addWidget(self.page_0)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_7 = QVBoxLayout(self.page_1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_6 = QWidget(self.page_1)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_12 = QWidget(self.widget_6)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setGeometry(QRect(10, 0, 471, 71))
        self.horizontalLayout_7 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.widget_17 = QWidget(self.widget_12)
        self.widget_17.setObjectName(u"widget_17")
        self.gridLayout_5 = QGridLayout(self.widget_17)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.calcular = QPushButton(self.widget_17)
        self.calcular.setObjectName(u"calcular")
        font2 = QFont()
        font2.setFamily(u"Bodoni MT")
        font2.setPointSize(14)
        self.calcular.setFont(font2)
        icon11 = QIcon()
        icon11.addFile(u":/purple_icons/assets/purple/zap.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.calcular.setIcon(icon11)
        self.calcular.setIconSize(QSize(25, 25))

        self.gridLayout_5.addWidget(self.calcular, 0, 0, 1, 1)


        self.horizontalLayout_7.addWidget(self.widget_17)

        self.widget_19 = QWidget(self.widget_12)
        self.widget_19.setObjectName(u"widget_19")
        self.gridLayout_6 = QGridLayout(self.widget_19)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.limpiar_2 = QPushButton(self.widget_19)
        self.limpiar_2.setObjectName(u"limpiar_2")
        font3 = QFont()
        font3.setFamily(u"Bodoni MT")
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setWeight(50)
        self.limpiar_2.setFont(font3)
        self.limpiar_2.setIcon(icon10)
        self.limpiar_2.setIconSize(QSize(25, 25))

        self.gridLayout_6.addWidget(self.limpiar_2, 0, 0, 1, 1)


        self.horizontalLayout_7.addWidget(self.widget_19)

        self.widget_111 = QWidget(self.widget_12)
        self.widget_111.setObjectName(u"widget_111")
        self.gridLayout_7 = QGridLayout(self.widget_111)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.guardar = QPushButton(self.widget_111)
        self.guardar.setObjectName(u"guardar")
        font4 = QFont()
        font4.setFamily(u"Bodoni MT")
        font4.setPointSize(12)
        self.guardar.setFont(font4)
        icon12 = QIcon()
        icon12.addFile(u":/purple_icons/assets/purple/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.guardar.setIcon(icon12)
        self.guardar.setIconSize(QSize(25, 25))

        self.gridLayout_7.addWidget(self.guardar, 0, 0, 1, 1)


        self.horizontalLayout_7.addWidget(self.widget_111)

        self.widget_13 = QWidget(self.widget_6)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setGeometry(QRect(10, 70, 471, 61))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_14 = QWidget(self.widget_13)
        self.widget_14.setObjectName(u"widget_14")
        self.label_8 = QLabel(self.widget_14)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 0, 61, 20))
        self.label_8.setFont(font4)
        self.Soporte = QLineEdit(self.widget_14)
        self.Soporte.setObjectName(u"Soporte")
        self.Soporte.setGeometry(QRect(30, 20, 81, 20))

        self.horizontalLayout_6.addWidget(self.widget_14)

        self.widget_15 = QWidget(self.widget_13)
        self.widget_15.setObjectName(u"widget_15")
        self.label_10 = QLabel(self.widget_15)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(40, 0, 71, 16))
        self.label_10.setFont(font4)
        self.Confianza = QLineEdit(self.widget_15)
        self.Confianza.setObjectName(u"Confianza")
        self.Confianza.setGeometry(QRect(30, 20, 81, 20))

        self.horizontalLayout_6.addWidget(self.widget_15)

        self.widget_16 = QWidget(self.widget_13)
        self.widget_16.setObjectName(u"widget_16")
        self.label_9 = QLabel(self.widget_16)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 0, 71, 20))
        self.label_9.setFont(font4)
        self.Elevacion = QLineEdit(self.widget_16)
        self.Elevacion.setObjectName(u"Elevacion")
        self.Elevacion.setGeometry(QRect(30, 20, 81, 20))

        self.horizontalLayout_6.addWidget(self.widget_16)

        self.widget_2 = QWidget(self.widget_6)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(9, 127, 472, 201))
        self.Resultados = QTextEdit(self.widget_2)
        self.Resultados.setObjectName(u"Resultados")
        self.Resultados.setGeometry(QRect(9, 9, 454, 191))

        self.verticalLayout_7.addWidget(self.widget_6)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_8 = QGridLayout(self.page_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.widget = QWidget(self.page_2)
        self.widget.setObjectName(u"widget")
        self.gridLayout_12 = QGridLayout(self.widget)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.widget_22 = QWidget(self.widget)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_23 = QWidget(self.widget_22)
        self.widget_23.setObjectName(u"widget_23")
        self.widget_23.setGeometry(QRect(-1, 3, 481, 31))
        self.horizontalLayout_9 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_3 = QLabel(self.widget_23)
        self.label_3.setObjectName(u"label_3")
        font5 = QFont()
        font5.setFamily(u"Bodoni MT")
        font5.setPointSize(10)
        self.label_3.setFont(font5)

        self.horizontalLayout_9.addWidget(self.label_3)

        self.varLine = QLineEdit(self.widget_23)
        self.varLine.setObjectName(u"varLine")

        self.horizontalLayout_9.addWidget(self.varLine)

        self.label_4 = QLabel(self.widget_23)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font5)

        self.horizontalLayout_9.addWidget(self.label_4)

        self.NoClusters = QLineEdit(self.widget_23)
        self.NoClusters.setObjectName(u"NoClusters")

        self.horizontalLayout_9.addWidget(self.NoClusters)

        self.widget_21 = QWidget(self.widget_22)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setGeometry(QRect(0, 60, 481, 51))
        self.gridLayout_9 = QGridLayout(self.widget_21)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.MCorr_Button = QPushButton(self.widget_21)
        self.MCorr_Button.setObjectName(u"MCorr_Button")
        self.MCorr_Button.setFont(font4)
        icon13 = QIcon()
        icon13.addFile(u":/purple_icons/assets/purple/sidebar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.MCorr_Button.setIcon(icon13)

        self.gridLayout_9.addWidget(self.MCorr_Button, 0, 1, 1, 1)

        self.EvalVis_Button = QPushButton(self.widget_21)
        self.EvalVis_Button.setObjectName(u"EvalVis_Button")
        self.EvalVis_Button.setFont(font4)
        icon14 = QIcon()
        icon14.addFile(u":/purple_icons/assets/purple/eye.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.EvalVis_Button.setIcon(icon14)

        self.gridLayout_9.addWidget(self.EvalVis_Button, 0, 0, 1, 1)

        self.Tree_Button = QPushButton(self.widget_21)
        self.Tree_Button.setObjectName(u"Tree_Button")
        self.Tree_Button.setFont(font4)
        icon15 = QIcon()
        icon15.addFile(u":/purple_icons/assets/purple/git-pull-request.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Tree_Button.setIcon(icon15)

        self.gridLayout_9.addWidget(self.Tree_Button, 0, 2, 1, 1)

        self.Centro_Button = QPushButton(self.widget_21)
        self.Centro_Button.setObjectName(u"Centro_Button")
        self.Centro_Button.setFont(font4)
        icon16 = QIcon()
        icon16.addFile(u":/purple_icons/assets/purple/disc.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Centro_Button.setIcon(icon16)

        self.gridLayout_9.addWidget(self.Centro_Button, 0, 3, 1, 1)

        self.widget_28 = QWidget(self.widget_22)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setGeometry(QRect(0, 98, 481, 221))
        self.tableWidget_3 = QTableWidget(self.widget_28)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(150, 0, 331, 221))
        self.ShowText = QTextEdit(self.widget_28)
        self.ShowText.setObjectName(u"ShowText")
        self.ShowText.setGeometry(QRect(4, -1, 141, 221))
        self.widget_26 = QWidget(self.widget_22)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setGeometry(QRect(0, 30, 481, 31))
        self.horizontalLayout_12 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_11 = QLabel(self.widget_26)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font5)

        self.horizontalLayout_12.addWidget(self.label_11)

        self.xLabel = QLineEdit(self.widget_26)
        self.xLabel.setObjectName(u"xLabel")

        self.horizontalLayout_12.addWidget(self.xLabel)

        self.label_12 = QLabel(self.widget_26)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font5)

        self.horizontalLayout_12.addWidget(self.label_12)

        self.YLabel = QLineEdit(self.widget_26)
        self.YLabel.setObjectName(u"YLabel")

        self.horizontalLayout_12.addWidget(self.YLabel)


        self.gridLayout_12.addWidget(self.widget_22, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.widget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.widget_20 = QWidget(self.page_3)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setGeometry(QRect(-1, 0, 511, 351))
        self.gridLayout_13 = QGridLayout(self.widget_20)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.widget_24 = QWidget(self.widget_20)
        self.widget_24.setObjectName(u"widget_24")
        self.widget_25 = QWidget(self.widget_24)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setGeometry(QRect(-1, 3, 481, 31))
        self.horizontalLayout_10 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_13 = QLabel(self.widget_25)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font5)

        self.horizontalLayout_10.addWidget(self.label_13)

        self.varLine_2 = QLineEdit(self.widget_25)
        self.varLine_2.setObjectName(u"varLine_2")

        self.horizontalLayout_10.addWidget(self.varLine_2)

        self.widget_27 = QWidget(self.widget_24)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setGeometry(QRect(0, 30, 481, 51))
        self.gridLayout_10 = QGridLayout(self.widget_27)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.MCorr_Button_2 = QPushButton(self.widget_27)
        self.MCorr_Button_2.setObjectName(u"MCorr_Button_2")
        self.MCorr_Button_2.setFont(font4)
        self.MCorr_Button_2.setIcon(icon13)

        self.gridLayout_10.addWidget(self.MCorr_Button_2, 0, 1, 1, 1)

        self.EvalVis_Button_2 = QPushButton(self.widget_27)
        self.EvalVis_Button_2.setObjectName(u"EvalVis_Button_2")
        self.EvalVis_Button_2.setFont(font4)
        self.EvalVis_Button_2.setIcon(icon14)

        self.gridLayout_10.addWidget(self.EvalVis_Button_2, 0, 0, 1, 1)

        self.Elbow_Button_2 = QPushButton(self.widget_27)
        self.Elbow_Button_2.setObjectName(u"Elbow_Button_2")
        self.Elbow_Button_2.setFont(font4)
        icon17 = QIcon()
        icon17.addFile(u":/purple_icons/assets/purple/git-branch.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Elbow_Button_2.setIcon(icon17)

        self.gridLayout_10.addWidget(self.Elbow_Button_2, 0, 2, 1, 1)

        self.Centro_Button_2 = QPushButton(self.widget_27)
        self.Centro_Button_2.setObjectName(u"Centro_Button_2")
        self.Centro_Button_2.setFont(font4)
        self.Centro_Button_2.setIcon(icon16)

        self.gridLayout_10.addWidget(self.Centro_Button_2, 0, 3, 1, 1)

        self.widget_29 = QWidget(self.widget_24)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setGeometry(QRect(2, 68, 485, 271))
        self.tableWidget_4 = QTableWidget(self.widget_29)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setGeometry(QRect(160, 0, 321, 261))
        self.ShowText_2 = QTextEdit(self.widget_29)
        self.ShowText_2.setObjectName(u"ShowText_2")
        self.ShowText_2.setGeometry(QRect(4, 0, 151, 261))

        self.gridLayout_13.addWidget(self.widget_24, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_6 = QLabel(self.page_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 0, 81, 21))
        self.label_6.setFont(font2)
        self.widget_5 = QWidget(self.page_4)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(10, 60, 491, 291))
        self.gridLayout_3 = QGridLayout(self.widget_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tableWidget_2 = QTableWidget(self.widget_5)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.gridLayout_3.addWidget(self.tableWidget_2, 0, 0, 1, 1)

        self.widget_18 = QWidget(self.page_4)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setGeometry(QRect(10, 10, 491, 51))
        self.horizontalLayout_8 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.Euclideana = QPushButton(self.widget_18)
        self.Euclideana.setObjectName(u"Euclideana")
        self.Euclideana.setFont(font4)
        icon18 = QIcon()
        icon18.addFile(u":/purple_icons/assets/purple/trello.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Euclideana.setIcon(icon18)

        self.horizontalLayout_8.addWidget(self.Euclideana)

        self.Chebyshev = QPushButton(self.widget_18)
        self.Chebyshev.setObjectName(u"Chebyshev")
        self.Chebyshev.setFont(font4)
        self.Chebyshev.setIcon(icon18)

        self.horizontalLayout_8.addWidget(self.Chebyshev)

        self.Manhattan = QPushButton(self.widget_18)
        self.Manhattan.setObjectName(u"Manhattan")
        self.Manhattan.setFont(font4)
        self.Manhattan.setIcon(icon18)

        self.horizontalLayout_8.addWidget(self.Manhattan)

        self.Minkowski = QPushButton(self.widget_18)
        self.Minkowski.setObjectName(u"Minkowski")
        self.Minkowski.setFont(font4)
        self.Minkowski.setIcon(icon18)

        self.horizontalLayout_8.addWidget(self.Minkowski)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.widget_11 = QWidget(self.page_5)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setGeometry(QRect(0, 0, 511, 351))
        self.widget_30 = QWidget(self.widget_11)
        self.widget_30.setObjectName(u"widget_30")
        self.widget_30.setGeometry(QRect(0, 0, 511, 351))
        self.widget_31 = QWidget(self.widget_30)
        self.widget_31.setObjectName(u"widget_31")
        self.widget_31.setGeometry(QRect(-1, 3, 511, 31))
        self.horizontalLayout_11 = QHBoxLayout(self.widget_31)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_14 = QLabel(self.widget_31)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font5)

        self.horizontalLayout_11.addWidget(self.label_14)

        self.varLine_3 = QLineEdit(self.widget_31)
        self.varLine_3.setObjectName(u"varLine_3")

        self.horizontalLayout_11.addWidget(self.varLine_3)

        self.label_15 = QLabel(self.widget_31)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font5)

        self.horizontalLayout_11.addWidget(self.label_15)

        self.NoClusters_2 = QLineEdit(self.widget_31)
        self.NoClusters_2.setObjectName(u"NoClusters_2")

        self.horizontalLayout_11.addWidget(self.NoClusters_2)

        self.widget_32 = QWidget(self.widget_30)
        self.widget_32.setObjectName(u"widget_32")
        self.widget_32.setGeometry(QRect(0, 20, 511, 51))
        self.gridLayout_11 = QGridLayout(self.widget_32)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.EvalVis_Button_3 = QPushButton(self.widget_32)
        self.EvalVis_Button_3.setObjectName(u"EvalVis_Button_3")
        self.EvalVis_Button_3.setFont(font4)
        self.EvalVis_Button_3.setIcon(icon14)

        self.gridLayout_11.addWidget(self.EvalVis_Button_3, 0, 0, 1, 1)

        self.MCorr_Button_3 = QPushButton(self.widget_32)
        self.MCorr_Button_3.setObjectName(u"MCorr_Button_3")
        self.MCorr_Button_3.setFont(font4)
        self.MCorr_Button_3.setIcon(icon13)

        self.gridLayout_11.addWidget(self.MCorr_Button_3, 0, 1, 1, 1)

        self.RL_Button = QPushButton(self.widget_32)
        self.RL_Button.setObjectName(u"RL_Button")
        self.RL_Button.setFont(font4)
        icon19 = QIcon()
        icon19.addFile(u":/purple_icons/assets/purple/divide.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.RL_Button.setIcon(icon19)

        self.gridLayout_11.addWidget(self.RL_Button, 0, 2, 1, 1)

        self.widget_33 = QWidget(self.widget_30)
        self.widget_33.setObjectName(u"widget_33")
        self.widget_33.setGeometry(QRect(0, 58, 511, 291))
        self.tableWidget_5 = QTableWidget(self.widget_33)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        self.tableWidget_5.setGeometry(QRect(240, 0, 271, 291))
        self.ShowText_3 = QTextEdit(self.widget_33)
        self.ShowText_3.setObjectName(u"ShowText_3")
        self.ShowText_3.setGeometry(QRect(4, -1, 231, 291))
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.widget_4 = QWidget(self.page_6)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(0, 10, 511, 341))
        self.widget_34 = QWidget(self.widget_4)
        self.widget_34.setObjectName(u"widget_34")
        self.widget_34.setGeometry(QRect(9, 9, 493, 251))
        self.widget_35 = QWidget(self.widget_34)
        self.widget_35.setObjectName(u"widget_35")
        self.widget_35.setGeometry(QRect(9, -1, 241, 251))
        self.horizontalLayout_13 = QHBoxLayout(self.widget_35)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.widget_38 = QWidget(self.widget_35)
        self.widget_38.setObjectName(u"widget_38")
        self.verticalLayout = QVBoxLayout(self.widget_38)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(self.widget_38)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.verticalLayout.addWidget(self.label_5)

        self.label_16 = QLabel(self.widget_38)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)

        self.verticalLayout.addWidget(self.label_16)

        self.label_18 = QLabel(self.widget_38)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font2)

        self.verticalLayout.addWidget(self.label_18)

        self.label_19 = QLabel(self.widget_38)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font2)

        self.verticalLayout.addWidget(self.label_19)


        self.horizontalLayout_13.addWidget(self.widget_38)

        self.widget_39 = QWidget(self.widget_35)
        self.widget_39.setObjectName(u"widget_39")
        self.ID_line = QLineEdit(self.widget_39)
        self.ID_line.setObjectName(u"ID_line")
        self.ID_line.setGeometry(QRect(10, 30, 87, 16))
        self.textura_line = QLineEdit(self.widget_39)
        self.textura_line.setObjectName(u"textura_line")
        self.textura_line.setGeometry(QRect(10, 80, 87, 16))
        self.Smoothness_line = QLineEdit(self.widget_39)
        self.Smoothness_line.setObjectName(u"Smoothness_line")
        self.Smoothness_line.setGeometry(QRect(10, 190, 87, 16))
        self.area_line = QLineEdit(self.widget_39)
        self.area_line.setObjectName(u"area_line")
        self.area_line.setGeometry(QRect(10, 140, 87, 16))

        self.horizontalLayout_13.addWidget(self.widget_39)

        self.widget_40 = QWidget(self.widget_34)
        self.widget_40.setObjectName(u"widget_40")
        self.widget_40.setGeometry(QRect(250, 0, 241, 251))
        self.horizontalLayout_14 = QHBoxLayout(self.widget_40)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.widget_41 = QWidget(self.widget_40)
        self.widget_41.setObjectName(u"widget_41")
        self.verticalLayout_8 = QVBoxLayout(self.widget_41)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_21 = QLabel(self.widget_41)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font2)

        self.verticalLayout_8.addWidget(self.label_21)

        self.label_24 = QLabel(self.widget_41)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font2)

        self.verticalLayout_8.addWidget(self.label_24)

        self.label_25 = QLabel(self.widget_41)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font2)

        self.verticalLayout_8.addWidget(self.label_25)


        self.horizontalLayout_14.addWidget(self.widget_41)

        self.widget_42 = QWidget(self.widget_40)
        self.widget_42.setObjectName(u"widget_42")
        self.sym_line = QLineEdit(self.widget_42)
        self.sym_line.setObjectName(u"sym_line")
        self.sym_line.setGeometry(QRect(0, 110, 89, 16))
        self.fractal_line = QLineEdit(self.widget_42)
        self.fractal_line.setObjectName(u"fractal_line")
        self.fractal_line.setGeometry(QRect(0, 180, 89, 16))
        self.Comp_line = QLineEdit(self.widget_42)
        self.Comp_line.setObjectName(u"Comp_line")
        self.Comp_line.setGeometry(QRect(0, 40, 89, 16))

        self.horizontalLayout_14.addWidget(self.widget_42)

        self.widget_37 = QWidget(self.widget_4)
        self.widget_37.setObjectName(u"widget_37")
        self.widget_37.setGeometry(QRect(9, 251, 491, 81))
        self.gridLayout_4 = QGridLayout(self.widget_37)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.Diagnosis_button = QPushButton(self.widget_37)
        self.Diagnosis_button.setObjectName(u"Diagnosis_button")
        self.Diagnosis_button.setFont(font2)
        icon20 = QIcon()
        icon20.addFile(u":/purple_icons/assets/purple/clipboard.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Diagnosis_button.setIcon(icon20)

        self.gridLayout_4.addWidget(self.Diagnosis_button, 0, 0, 1, 1)

        self.DiagnosisLineEdit = QLineEdit(self.widget_37)
        self.DiagnosisLineEdit.setObjectName(u"DiagnosisLineEdit")

        self.gridLayout_4.addWidget(self.DiagnosisLineEdit, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.widget_36 = QWidget(self.page_7)
        self.widget_36.setObjectName(u"widget_36")
        self.widget_36.setGeometry(QRect(0, 0, 511, 351))
        self.widget_43 = QWidget(self.widget_36)
        self.widget_43.setObjectName(u"widget_43")
        self.widget_43.setGeometry(QRect(0, 0, 511, 351))
        self.widget_47 = QWidget(self.widget_43)
        self.widget_47.setObjectName(u"widget_47")
        self.widget_47.setGeometry(QRect(-1, 0, 511, 31))
        font6 = QFont()
        font6.setFamily(u"Bodoni MT")
        self.widget_47.setFont(font6)
        self.horizontalLayout_16 = QHBoxLayout(self.widget_47)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_22 = QLabel(self.widget_47)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font5)

        self.horizontalLayout_16.addWidget(self.label_22)

        self.predictora = QLineEdit(self.widget_47)
        self.predictora.setObjectName(u"predictora")

        self.horizontalLayout_16.addWidget(self.predictora)

        self.label_28 = QLabel(self.widget_47)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font5)

        self.horizontalLayout_16.addWidget(self.label_28)

        self.numL = QLineEdit(self.widget_47)
        self.numL.setObjectName(u"numL")

        self.horizontalLayout_16.addWidget(self.numL)

        self.widget_48 = QWidget(self.widget_43)
        self.widget_48.setObjectName(u"widget_48")
        self.widget_48.setGeometry(QRect(0, 50, 511, 51))
        self.gridLayout_15 = QGridLayout(self.widget_48)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.TreeB = QPushButton(self.widget_48)
        self.TreeB.setObjectName(u"TreeB")
        self.TreeB.setFont(font4)
        icon21 = QIcon()
        icon21.addFile(u":/purple_icons/assets/purple/edit-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.TreeB.setIcon(icon21)

        self.gridLayout_15.addWidget(self.TreeB, 0, 0, 1, 1)

        self.widget_49 = QWidget(self.widget_43)
        self.widget_49.setObjectName(u"widget_49")
        self.widget_49.setGeometry(QRect(0, 88, 511, 261))
        self.ShowText_5 = QTextEdit(self.widget_49)
        self.ShowText_5.setObjectName(u"ShowText_5")
        self.ShowText_5.setGeometry(QRect(0, 0, 201, 261))
        self.ShowText_6 = QTextEdit(self.widget_49)
        self.ShowText_6.setObjectName(u"ShowText_6")
        self.ShowText_6.setGeometry(QRect(210, 0, 301, 261))
        self.widget_50 = QWidget(self.widget_43)
        self.widget_50.setObjectName(u"widget_50")
        self.widget_50.setGeometry(QRect(0, 30, 511, 31))
        self.horizontalLayout_17 = QHBoxLayout(self.widget_50)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_23 = QLabel(self.widget_50)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font5)

        self.horizontalLayout_17.addWidget(self.label_23)

        self.depth = QLineEdit(self.widget_50)
        self.depth.setObjectName(u"depth")

        self.horizontalLayout_17.addWidget(self.depth)

        self.label_26 = QLabel(self.widget_50)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font5)

        self.horizontalLayout_17.addWidget(self.label_26)

        self.minSplit = QLineEdit(self.widget_50)
        self.minSplit.setObjectName(u"minSplit")

        self.horizontalLayout_17.addWidget(self.minSplit)

        self.label_27 = QLabel(self.widget_50)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font5)

        self.horizontalLayout_17.addWidget(self.label_27)

        self.minleaf = QLineEdit(self.widget_50)
        self.minleaf.setObjectName(u"minleaf")

        self.horizontalLayout_17.addWidget(self.minleaf)

        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.widget_51 = QWidget(self.page_8)
        self.widget_51.setObjectName(u"widget_51")
        self.widget_51.setGeometry(QRect(0, 0, 511, 351))
        self.widget_52 = QWidget(self.widget_51)
        self.widget_52.setObjectName(u"widget_52")
        self.widget_52.setGeometry(QRect(0, 0, 511, 351))
        self.widget_53 = QWidget(self.widget_52)
        self.widget_53.setObjectName(u"widget_53")
        self.widget_53.setGeometry(QRect(9, 9, 493, 251))
        self.widget_54 = QWidget(self.widget_53)
        self.widget_54.setObjectName(u"widget_54")
        self.widget_54.setGeometry(QRect(9, -1, 241, 251))
        self.horizontalLayout_18 = QHBoxLayout(self.widget_54)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.widget_55 = QWidget(self.widget_54)
        self.widget_55.setObjectName(u"widget_55")
        self.verticalLayout_2 = QVBoxLayout(self.widget_55)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_7 = QLabel(self.widget_55)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_7)

        self.label_29 = QLabel(self.widget_55)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_29)

        self.label_30 = QLabel(self.widget_55)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_30)

        self.label_31 = QLabel(self.widget_55)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_31)


        self.horizontalLayout_18.addWidget(self.widget_55)

        self.widget_56 = QWidget(self.widget_54)
        self.widget_56.setObjectName(u"widget_56")
        self.ID_line_2 = QLineEdit(self.widget_56)
        self.ID_line_2.setObjectName(u"ID_line_2")
        self.ID_line_2.setGeometry(QRect(10, 30, 87, 16))
        self.textura_line_2 = QLineEdit(self.widget_56)
        self.textura_line_2.setObjectName(u"textura_line_2")
        self.textura_line_2.setGeometry(QRect(10, 80, 87, 16))
        self.Smoothness_line_2 = QLineEdit(self.widget_56)
        self.Smoothness_line_2.setObjectName(u"Smoothness_line_2")
        self.Smoothness_line_2.setGeometry(QRect(10, 190, 87, 16))
        self.Perimeter_line_2 = QLineEdit(self.widget_56)
        self.Perimeter_line_2.setObjectName(u"Perimeter_line_2")
        self.Perimeter_line_2.setGeometry(QRect(10, 140, 87, 16))

        self.horizontalLayout_18.addWidget(self.widget_56)

        self.widget_57 = QWidget(self.widget_53)
        self.widget_57.setObjectName(u"widget_57")
        self.widget_57.setGeometry(QRect(250, 0, 241, 251))
        self.horizontalLayout_19 = QHBoxLayout(self.widget_57)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.widget_58 = QWidget(self.widget_57)
        self.widget_58.setObjectName(u"widget_58")
        self.verticalLayout_9 = QVBoxLayout(self.widget_58)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_32 = QLabel(self.widget_58)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font2)

        self.verticalLayout_9.addWidget(self.label_32)

        self.label_33 = QLabel(self.widget_58)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font2)

        self.verticalLayout_9.addWidget(self.label_33)

        self.label_34 = QLabel(self.widget_58)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font2)

        self.verticalLayout_9.addWidget(self.label_34)


        self.horizontalLayout_19.addWidget(self.widget_58)

        self.widget_59 = QWidget(self.widget_57)
        self.widget_59.setObjectName(u"widget_59")
        self.sym_line_2 = QLineEdit(self.widget_59)
        self.sym_line_2.setObjectName(u"sym_line_2")
        self.sym_line_2.setGeometry(QRect(0, 110, 89, 16))
        self.fractal_line_2 = QLineEdit(self.widget_59)
        self.fractal_line_2.setObjectName(u"fractal_line_2")
        self.fractal_line_2.setGeometry(QRect(0, 180, 89, 16))
        self.Comp_line_2 = QLineEdit(self.widget_59)
        self.Comp_line_2.setObjectName(u"Comp_line_2")
        self.Comp_line_2.setGeometry(QRect(0, 40, 89, 16))

        self.horizontalLayout_19.addWidget(self.widget_59)

        self.widget_60 = QWidget(self.widget_52)
        self.widget_60.setObjectName(u"widget_60")
        self.widget_60.setGeometry(QRect(9, 251, 491, 91))
        self.gridLayout_16 = QGridLayout(self.widget_60)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.AreaButton_2 = QPushButton(self.widget_60)
        self.AreaButton_2.setObjectName(u"AreaButton_2")
        self.AreaButton_2.setFont(font2)
        self.AreaButton_2.setIcon(icon20)

        self.gridLayout_16.addWidget(self.AreaButton_2, 0, 0, 1, 1)

        self.AreaC = QLineEdit(self.widget_60)
        self.AreaC.setObjectName(u"AreaC")

        self.gridLayout_16.addWidget(self.AreaC, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.widget_61 = QWidget(self.page_9)
        self.widget_61.setObjectName(u"widget_61")
        self.widget_61.setGeometry(QRect(0, 0, 521, 351))
        self.widget_62 = QWidget(self.widget_61)
        self.widget_62.setObjectName(u"widget_62")
        self.widget_62.setGeometry(QRect(0, 0, 511, 351))
        self.widget_63 = QWidget(self.widget_62)
        self.widget_63.setObjectName(u"widget_63")
        self.widget_63.setGeometry(QRect(0, 0, 511, 351))
        self.widget_64 = QWidget(self.widget_63)
        self.widget_64.setObjectName(u"widget_64")
        self.widget_64.setGeometry(QRect(-1, 0, 511, 31))
        self.widget_64.setFont(font6)
        self.horizontalLayout_20 = QHBoxLayout(self.widget_64)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_35 = QLabel(self.widget_64)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font5)

        self.horizontalLayout_20.addWidget(self.label_35)

        self.predictora_2 = QLineEdit(self.widget_64)
        self.predictora_2.setObjectName(u"predictora_2")

        self.horizontalLayout_20.addWidget(self.predictora_2)

        self.label_37 = QLabel(self.widget_64)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font5)

        self.horizontalLayout_20.addWidget(self.label_37)

        self.numL_2 = QLineEdit(self.widget_64)
        self.numL_2.setObjectName(u"numL_2")

        self.horizontalLayout_20.addWidget(self.numL_2)

        self.widget_65 = QWidget(self.widget_63)
        self.widget_65.setObjectName(u"widget_65")
        self.widget_65.setGeometry(QRect(0, 50, 511, 51))
        self.gridLayout_17 = QGridLayout(self.widget_65)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.TreeB_2 = QPushButton(self.widget_65)
        self.TreeB_2.setObjectName(u"TreeB_2")
        self.TreeB_2.setFont(font4)
        self.TreeB_2.setIcon(icon21)

        self.gridLayout_17.addWidget(self.TreeB_2, 0, 0, 1, 1)

        self.widget_66 = QWidget(self.widget_63)
        self.widget_66.setObjectName(u"widget_66")
        self.widget_66.setGeometry(QRect(0, 88, 511, 261))
        self.ShowText_7 = QTextEdit(self.widget_66)
        self.ShowText_7.setObjectName(u"ShowText_7")
        self.ShowText_7.setGeometry(QRect(10, 0, 261, 111))
        self.ShowText_8 = QTextEdit(self.widget_66)
        self.ShowText_8.setObjectName(u"ShowText_8")
        self.ShowText_8.setGeometry(QRect(280, 0, 231, 251))
        self.tableWidget_7 = QTableWidget(self.widget_66)
        self.tableWidget_7.setObjectName(u"tableWidget_7")
        self.tableWidget_7.setGeometry(QRect(10, 120, 261, 131))
        self.widget_67 = QWidget(self.widget_63)
        self.widget_67.setObjectName(u"widget_67")
        self.widget_67.setGeometry(QRect(0, 30, 511, 31))
        self.horizontalLayout_21 = QHBoxLayout(self.widget_67)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_38 = QLabel(self.widget_67)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font5)

        self.horizontalLayout_21.addWidget(self.label_38)

        self.depth_2 = QLineEdit(self.widget_67)
        self.depth_2.setObjectName(u"depth_2")

        self.horizontalLayout_21.addWidget(self.depth_2)

        self.label_39 = QLabel(self.widget_67)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font5)

        self.horizontalLayout_21.addWidget(self.label_39)

        self.minSplit_2 = QLineEdit(self.widget_67)
        self.minSplit_2.setObjectName(u"minSplit_2")

        self.horizontalLayout_21.addWidget(self.minSplit_2)

        self.label_40 = QLabel(self.widget_67)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font5)

        self.horizontalLayout_21.addWidget(self.label_40)

        self.minleaf_2 = QLineEdit(self.widget_67)
        self.minleaf_2.setObjectName(u"minleaf_2")

        self.horizontalLayout_21.addWidget(self.minleaf_2)

        self.stackedWidget.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.widget_68 = QWidget(self.page_10)
        self.widget_68.setObjectName(u"widget_68")
        self.widget_68.setGeometry(QRect(0, 0, 511, 351))
        self.widget_69 = QWidget(self.widget_68)
        self.widget_69.setObjectName(u"widget_69")
        self.widget_69.setGeometry(QRect(10, 0, 511, 341))
        self.widget_78 = QWidget(self.widget_69)
        self.widget_78.setObjectName(u"widget_78")
        self.widget_78.setGeometry(QRect(9, 9, 493, 251))
        self.widget_79 = QWidget(self.widget_78)
        self.widget_79.setObjectName(u"widget_79")
        self.widget_79.setGeometry(QRect(9, -1, 241, 251))
        self.horizontalLayout_24 = QHBoxLayout(self.widget_79)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.widget_80 = QWidget(self.widget_79)
        self.widget_80.setObjectName(u"widget_80")
        self.verticalLayout_12 = QVBoxLayout(self.widget_80)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_47 = QLabel(self.widget_80)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font2)

        self.verticalLayout_12.addWidget(self.label_47)

        self.label_48 = QLabel(self.widget_80)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font2)

        self.verticalLayout_12.addWidget(self.label_48)

        self.label_49 = QLabel(self.widget_80)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font2)

        self.verticalLayout_12.addWidget(self.label_49)

        self.label_50 = QLabel(self.widget_80)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font2)

        self.verticalLayout_12.addWidget(self.label_50)


        self.horizontalLayout_24.addWidget(self.widget_80)

        self.widget_81 = QWidget(self.widget_79)
        self.widget_81.setObjectName(u"widget_81")
        self.ID_line_4 = QLineEdit(self.widget_81)
        self.ID_line_4.setObjectName(u"ID_line_4")
        self.ID_line_4.setGeometry(QRect(10, 30, 87, 16))
        self.textura_line_4 = QLineEdit(self.widget_81)
        self.textura_line_4.setObjectName(u"textura_line_4")
        self.textura_line_4.setGeometry(QRect(10, 80, 87, 16))
        self.Smoothness_line_4 = QLineEdit(self.widget_81)
        self.Smoothness_line_4.setObjectName(u"Smoothness_line_4")
        self.Smoothness_line_4.setGeometry(QRect(10, 190, 87, 16))
        self.area_line_2 = QLineEdit(self.widget_81)
        self.area_line_2.setObjectName(u"area_line_2")
        self.area_line_2.setGeometry(QRect(10, 140, 87, 16))

        self.horizontalLayout_24.addWidget(self.widget_81)

        self.widget_82 = QWidget(self.widget_78)
        self.widget_82.setObjectName(u"widget_82")
        self.widget_82.setGeometry(QRect(250, 0, 241, 251))
        self.horizontalLayout_25 = QHBoxLayout(self.widget_82)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.widget_83 = QWidget(self.widget_82)
        self.widget_83.setObjectName(u"widget_83")
        self.verticalLayout_13 = QVBoxLayout(self.widget_83)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_51 = QLabel(self.widget_83)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font2)

        self.verticalLayout_13.addWidget(self.label_51)

        self.label_52 = QLabel(self.widget_83)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font2)

        self.verticalLayout_13.addWidget(self.label_52)

        self.label_53 = QLabel(self.widget_83)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font2)

        self.verticalLayout_13.addWidget(self.label_53)


        self.horizontalLayout_25.addWidget(self.widget_83)

        self.widget_84 = QWidget(self.widget_82)
        self.widget_84.setObjectName(u"widget_84")
        self.sym_line_4 = QLineEdit(self.widget_84)
        self.sym_line_4.setObjectName(u"sym_line_4")
        self.sym_line_4.setGeometry(QRect(0, 110, 89, 16))
        self.fractal_line_4 = QLineEdit(self.widget_84)
        self.fractal_line_4.setObjectName(u"fractal_line_4")
        self.fractal_line_4.setGeometry(QRect(0, 180, 89, 16))
        self.Comp_line_4 = QLineEdit(self.widget_84)
        self.Comp_line_4.setObjectName(u"Comp_line_4")
        self.Comp_line_4.setGeometry(QRect(0, 40, 89, 16))

        self.horizontalLayout_25.addWidget(self.widget_84)

        self.widget_85 = QWidget(self.widget_69)
        self.widget_85.setObjectName(u"widget_85")
        self.widget_85.setGeometry(QRect(9, 251, 491, 81))
        self.gridLayout_19 = QGridLayout(self.widget_85)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.Diagnosis_button_2 = QPushButton(self.widget_85)
        self.Diagnosis_button_2.setObjectName(u"Diagnosis_button_2")
        self.Diagnosis_button_2.setFont(font2)
        self.Diagnosis_button_2.setIcon(icon20)

        self.gridLayout_19.addWidget(self.Diagnosis_button_2, 0, 0, 1, 1)

        self.DiagnosisLineEdit_2 = QLineEdit(self.widget_85)
        self.DiagnosisLineEdit_2.setObjectName(u"DiagnosisLineEdit_2")

        self.gridLayout_19.addWidget(self.DiagnosisLineEdit_2, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_10)

        self.horizontalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Button_1.setText(QCoreApplication.translate("MainWindow", u"Datos", None))
        self.Button_2.setText(QCoreApplication.translate("MainWindow", u"Asociaci\u00f3n", None))
        self.Button_5.setText(QCoreApplication.translate("MainWindow", u"Distancias", None))
        self.Button_3.setText(QCoreApplication.translate("MainWindow", u"Cl\u00faster jer\u00e1rquico", None))
        self.Button_4.setText(QCoreApplication.translate("MainWindow", u"Cl\u00faster particional", None))
        self.Button_6.setText(QCoreApplication.translate("MainWindow", u"R. Logistica", None))
        self.Button_7.setText(QCoreApplication.translate("MainWindow", u"R. Log. M\u00e9dico", None))
        self.Button_8.setText(QCoreApplication.translate("MainWindow", u"\u00c1rbol Pronos\u00f3stico", None))
        self.Button_9.setText(QCoreApplication.translate("MainWindow", u"\u00c1rbol P. M\u00e9dico", None))
        self.Button_10.setText(QCoreApplication.translate("MainWindow", u"\u00c1rbol Clasificaci\u00f3n", None))
        self.Button_11.setText(QCoreApplication.translate("MainWindow", u"\u00c1rbol Clas. M\u00e9dico", None))
        self.menuBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Men\u00fa", None))
        self.label.setText("")
        self.browse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.limpiar.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.Datos.setText(QCoreApplication.translate("MainWindow", u"Datos:", None))
        self.calcular.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.limpiar_2.setText(QCoreApplication.translate("MainWindow", u"Limpiar datos", None))
        self.guardar.setText(QCoreApplication.translate("MainWindow", u"Guardar datos", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Soporte", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Confianza", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Elevaci\u00f3n", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Variable Eval. Visual", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"No. Clusters", None))
        self.MCorr_Button.setText(QCoreApplication.translate("MainWindow", u"Matriz de correlaciones", None))
        self.EvalVis_Button.setText(QCoreApplication.translate("MainWindow", u"Gr\u00e1ficas", None))
        self.Tree_Button.setText(QCoreApplication.translate("MainWindow", u"\u00c1rbol", None))
        self.Centro_Button.setText(QCoreApplication.translate("MainWindow", u"Centroides", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Etiqueta X", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Etiqueta Y", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Variable Eval. Visual", None))
        self.MCorr_Button_2.setText(QCoreApplication.translate("MainWindow", u"Matriz de correlaciones", None))
        self.EvalVis_Button_2.setText(QCoreApplication.translate("MainWindow", u"Gr\u00e1ficas", None))
        self.Elbow_Button_2.setText(QCoreApplication.translate("MainWindow", u"Elbow", None))
        self.Centro_Button_2.setText(QCoreApplication.translate("MainWindow", u"Centroides", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Distancias", None))
        self.Euclideana.setText(QCoreApplication.translate("MainWindow", u"Euclideana", None))
        self.Chebyshev.setText(QCoreApplication.translate("MainWindow", u"Chebyshev", None))
        self.Manhattan.setText(QCoreApplication.translate("MainWindow", u"Manhattan", None))
        self.Minkowski.setText(QCoreApplication.translate("MainWindow", u"Minkowski", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Variable Eval. Visual", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Porcentaje datos prueba", None))
        self.EvalVis_Button_3.setText(QCoreApplication.translate("MainWindow", u"Gr\u00e1ficas", None))
        self.MCorr_Button_3.setText(QCoreApplication.translate("MainWindow", u"Matriz de correlaciones", None))
        self.RL_Button.setText(QCoreApplication.translate("MainWindow", u"Ecuaci\u00f3n", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Textura", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Area", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Smoothness", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Compactness", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Symmetry", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Fractal Dim.", None))
        self.Diagnosis_button.setText(QCoreApplication.translate("MainWindow", u"Diagnosis", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Variable Predictora", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Porcentaje datos prueba", None))
        self.TreeB.setText(QCoreApplication.translate("MainWindow", u"Obtener \u00c1rbol", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Profundidad", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Min_split", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Min_leaf", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Textura", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Perimeter", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Smoothness", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Compactness", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Symmetry", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Fractal Dim.", None))
        self.AreaButton_2.setText(QCoreApplication.translate("MainWindow", u"Area", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Variable Predictora", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Porcentaje datos prueba", None))
        self.TreeB_2.setText(QCoreApplication.translate("MainWindow", u"Obtener \u00c1rbol", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Profundidad", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Min_split", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Min_leaf", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Textura", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Area", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Smoothness", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Compactness", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Symmetry", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Fractal Dim.", None))
        self.Diagnosis_button_2.setText(QCoreApplication.translate("MainWindow", u"Diagnosis", None))
    # retranslateUi


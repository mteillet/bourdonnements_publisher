# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bourdonnementsProjectManager_qt_v002.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(892, 664)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainFrameLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainFrameLayout.setContentsMargins(10, 10, 10, 10)
        self.mainFrameLayout.setSpacing(0)
        self.mainFrameLayout.setObjectName("mainFrameLayout")
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        self.mainFrame.setStyleSheet("background-color: rgb(28, 33, 35);\n"
"\n"
"border-radius :10px;\n"
"")
        self.mainFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainFrame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_bar = QtWidgets.QFrame(self.mainFrame)
        self.title_bar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.title_bar.setStyleSheet("background-color : none;")
        self.title_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_bar.setObjectName("title_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.title_bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_title_boubou = QtWidgets.QFrame(self.title_bar)
        self.frame_title_boubou.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(14)
        self.frame_title_boubou.setFont(font)
        self.frame_title_boubou.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title_boubou.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title_boubou.setObjectName("frame_title_boubou")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_title_boubou)
        self.verticalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_title = QtWidgets.QLabel(self.frame_title_boubou)
        font = QtGui.QFont()
        font.setFamily("Fira Sans Condensed")
        font.setPointSize(20)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(225, 225, 225);")
        self.label_title.setObjectName("label_title")
        self.verticalLayout_2.addWidget(self.label_title)
        self.horizontalLayout.addWidget(self.frame_title_boubou)
        self.frame_btns = QtWidgets.QFrame(self.title_bar)
        self.frame_btns.setMaximumSize(QtCore.QSize(90, 16777215))
        self.frame_btns.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_btns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btns.setObjectName("frame_btns")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_btns)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_maximize = QtWidgets.QPushButton(self.frame_btns)
        self.btn_maximize.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_maximize.setMaximumSize(QtCore.QSize(16, 16))
        self.btn_maximize.setStyleSheet("QPushButton {\n"
"    border : none;\n"
"    border-radius : 8px;\n"
"    background-color: rgb(241,209,181);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:  rgba(241,209,181, 150);\n"
"}")
        self.btn_maximize.setText("")
        self.btn_maximize.setObjectName("btn_maximize")
        self.horizontalLayout_2.addWidget(self.btn_maximize)
        self.btn_minimize = QtWidgets.QPushButton(self.frame_btns)
        self.btn_minimize.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_minimize.setMaximumSize(QtCore.QSize(16, 16))
        self.btn_minimize.setStyleSheet("QPushButton {\n"
"    border : none;\n"
"    border-radius : 8px;\n"
"    background-color: rgb(240,183,164);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:  rgba(240,183,164,150);\n"
"}")
        self.btn_minimize.setText("")
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout_2.addWidget(self.btn_minimize)
        self.btn_close = QtWidgets.QPushButton(self.frame_btns)
        self.btn_close.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_close.setMaximumSize(QtCore.QSize(16, 16))
        self.btn_close.setStyleSheet("QPushButton {\n"
"    border : none;\n"
"    border-radius : 8px;\n"
"    background-color: rgb(241,140,142);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:  rgba(241,140,142, 150);\n"
"}")
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_2.addWidget(self.btn_close)
        self.horizontalLayout.addWidget(self.frame_btns)
        self.verticalLayout.addWidget(self.title_bar)
        self.contents_bar = QtWidgets.QFrame(self.mainFrame)
        self.contents_bar.setStyleSheet("background-color : none;")
        self.contents_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contents_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contents_bar.setObjectName("contents_bar")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.contents_bar)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabsHolder_frame = QtWidgets.QFrame(self.contents_bar)
        self.tabsHolder_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tabsHolder_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tabsHolder_frame.setObjectName("tabsHolder_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tabsHolder_frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tabsLeft_frame = QtWidgets.QFrame(self.tabsHolder_frame)
        self.tabsLeft_frame.setMaximumSize(QtCore.QSize(10, 16777215))
        self.tabsLeft_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tabsLeft_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tabsLeft_frame.setObjectName("tabsLeft_frame")
        self.horizontalLayout_4.addWidget(self.tabsLeft_frame)
        self.tabsMid_frame = QtWidgets.QFrame(self.tabsHolder_frame)
        self.tabsMid_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tabsMid_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tabsMid_frame.setObjectName("tabsMid_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabsMid_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tab_user_selection = QtWidgets.QFrame(self.tabsMid_frame)
        self.tab_user_selection.setMaximumSize(QtCore.QSize(16777215, 50))
        self.tab_user_selection.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tab_user_selection.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tab_user_selection.setObjectName("tab_user_selection")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_user_selection)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tabUserLabelContainer = QtWidgets.QFrame(self.tab_user_selection)
        self.tabUserLabelContainer.setMaximumSize(QtCore.QSize(125, 16777215))
        self.tabUserLabelContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tabUserLabelContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tabUserLabelContainer.setObjectName("tabUserLabelContainer")
        self.label_user = QtWidgets.QLabel(self.tabUserLabelContainer)
        self.label_user.setGeometry(QtCore.QRect(0, 3, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.label_user.setFont(font)
        self.label_user.setStyleSheet("color: rgb(86, 142, 166);")
        self.label_user.setObjectName("label_user")
        self.horizontalLayout_5.addWidget(self.tabUserLabelContainer)
        self.tabUser = QtWidgets.QFrame(self.tab_user_selection)
        self.tabUser.setMaximumSize(QtCore.QSize(240, 16777215))
        self.tabUser.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tabUser.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tabUser.setObjectName("tabUser")
        self.comboBox_User = QtWidgets.QComboBox(self.tabUser)
        self.comboBox_User.setGeometry(QtCore.QRect(10, 0, 211, 22))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_User.setFont(font)
        self.comboBox_User.setAutoFillBackground(False)
        self.comboBox_User.setStyleSheet("")
        self.comboBox_User.setObjectName("comboBox_User")
        self.comboBox_User.addItem("")
        self.comboBox_User.addItem("")
        self.comboBox_User.addItem("")
        self.comboBox_User.addItem("")
        self.comboBox_User.addItem("")
        self.comboBox_User.addItem("")
        self.comboBox_User.addItem("")
        self.horizontalLayout_5.addWidget(self.tabUser)
        self.tabUserBtn = QtWidgets.QFrame(self.tab_user_selection)
        self.tabUserBtn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Overpass Mono Light")
        self.tabUserBtn.setFont(font)
        self.tabUserBtn.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tabUserBtn.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tabUserBtn.setObjectName("tabUserBtn")
        self.btn_updateUser = QtWidgets.QPushButton(self.tabUserBtn)
        self.btn_updateUser.setGeometry(QtCore.QRect(0, 0, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Overpass Mono Light")
        self.btn_updateUser.setFont(font)
        self.btn_updateUser.setStyleSheet("QPushButton {\n"
"    border : none;\n"
"    border-radius : 8px;\n"
"    background-color: rgb(86,142,166);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:  rgba(86,142,166, 150);\n"
"}")
        self.btn_updateUser.setFlat(False)
        self.btn_updateUser.setObjectName("btn_updateUser")
        self.horizontalLayout_5.addWidget(self.tabUserBtn)
        self.verticalLayout_4.addWidget(self.tab_user_selection)
        self.tab_contents = QtWidgets.QFrame(self.tabsMid_frame)
        self.tab_contents.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tab_contents.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tab_contents.setObjectName("tab_contents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_contents)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.option_bar_top = QtWidgets.QFrame(self.tab_contents)
        self.option_bar_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.option_bar_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.option_bar_top.setObjectName("option_bar_top")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.option_bar_top)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.option_01_bar = QtWidgets.QFrame(self.option_bar_top)
        self.option_01_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.option_01_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.option_01_bar.setObjectName("option_01_bar")
        self.overview_btn = QtWidgets.QPushButton(self.option_01_bar)
        self.overview_btn.setGeometry(QtCore.QRect(0, 0, 250, 100))
        self.overview_btn.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.overview_btn.setFont(font)
        self.overview_btn.setStyleSheet("QPushButton {\n"
"    border : none;\n"
"    border-radius : 8px;\n"
"    background-color: rgb(86,142,166);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:  rgba(86,142,166, 150);\n"
"}")
        self.overview_btn.setObjectName("overview_btn")
        self.horizontalLayout_6.addWidget(self.option_01_bar)
        self.option_02_bar = QtWidgets.QFrame(self.option_bar_top)
        self.option_02_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.option_02_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.option_02_bar.setObjectName("option_02_bar")
        self.assets_btn = QtWidgets.QPushButton(self.option_02_bar)
        self.assets_btn.setGeometry(QtCore.QRect(0, 0, 250, 100))
        self.assets_btn.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.assets_btn.setFont(font)
        self.assets_btn.setStyleSheet("QPushButton {\n"
"    border : none;\n"
"    border-radius : 8px;\n"
"    background-color: rgb(86,142,166);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:  rgba(86,142,166, 150);\n"
"}")
        self.assets_btn.setObjectName("assets_btn")
        self.horizontalLayout_6.addWidget(self.option_02_bar)
        self.option_03_bar = QtWidgets.QFrame(self.option_bar_top)
        self.option_03_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.option_03_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.option_03_bar.setObjectName("option_03_bar")
        self.shots_btn = QtWidgets.QPushButton(self.option_03_bar)
        self.shots_btn.setGeometry(QtCore.QRect(0, 0, 250, 100))
        self.shots_btn.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.shots_btn.setFont(font)
        self.shots_btn.setStyleSheet("QPushButton {\n"
"    border : none;\n"
"    border-radius : 8px;\n"
"    background-color: rgb(86,142,166);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:  rgba(86,142,166, 150);\n"
"}")
        self.shots_btn.setObjectName("shots_btn")
        self.horizontalLayout_6.addWidget(self.option_03_bar)
        self.verticalLayout_5.addWidget(self.option_bar_top)
        self.opton_bar_mid = QtWidgets.QFrame(self.tab_contents)
        self.opton_bar_mid.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.opton_bar_mid.setFrameShadow(QtWidgets.QFrame.Raised)
        self.opton_bar_mid.setObjectName("opton_bar_mid")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.opton_bar_mid)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.option_04_bar = QtWidgets.QFrame(self.opton_bar_mid)
        self.option_04_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.option_04_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.option_04_bar.setObjectName("option_04_bar")
        self.compo_btn = QtWidgets.QPushButton(self.option_04_bar)
        self.compo_btn.setGeometry(QtCore.QRect(0, 0, 250, 100))
        self.compo_btn.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.compo_btn.setFont(font)
        self.compo_btn.setStyleSheet("QPushButton {\n"
"    border : none;\n"
"    border-radius : 8px;\n"
"    background-color: rgb(86,142,166);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:  rgba(86,142,166, 150);\n"
"}")
        self.compo_btn.setObjectName("compo_btn")
        self.horizontalLayout_7.addWidget(self.option_04_bar)
        self.option_05_bar = QtWidgets.QFrame(self.opton_bar_mid)
        self.option_05_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.option_05_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.option_05_bar.setObjectName("option_05_bar")
        self.editing_btn = QtWidgets.QPushButton(self.option_05_bar)
        self.editing_btn.setGeometry(QtCore.QRect(0, 0, 250, 100))
        self.editing_btn.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.editing_btn.setFont(font)
        self.editing_btn.setStyleSheet("QPushButton {\n"
"    border : none;\n"
"    border-radius : 8px;\n"
"    background-color: rgb(86,142,166);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:  rgba(86,142,166, 150);\n"
"}")
        self.editing_btn.setObjectName("editing_btn")
        self.horizontalLayout_7.addWidget(self.option_05_bar)
        self.option_06_bar = QtWidgets.QFrame(self.opton_bar_mid)
        self.option_06_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.option_06_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.option_06_bar.setObjectName("option_06_bar")
        self.ressources_btn = QtWidgets.QPushButton(self.option_06_bar)
        self.ressources_btn.setGeometry(QtCore.QRect(0, 0, 250, 100))
        self.ressources_btn.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.ressources_btn.setFont(font)
        self.ressources_btn.setStyleSheet("QPushButton {\n"
"    border : none;\n"
"    border-radius : 8px;\n"
"    background-color: rgb(86,142,166);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:  rgba(86,142,166, 150);\n"
"}")
        self.ressources_btn.setObjectName("ressources_btn")
        self.horizontalLayout_7.addWidget(self.option_06_bar)
        self.verticalLayout_5.addWidget(self.opton_bar_mid)
        self.option_bar_bot = QtWidgets.QFrame(self.tab_contents)
        self.option_bar_bot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.option_bar_bot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.option_bar_bot.setObjectName("option_bar_bot")
        self.verticalLayout_5.addWidget(self.option_bar_bot)
        self.verticalLayout_4.addWidget(self.tab_contents)
        self.tabBottom = QtWidgets.QFrame(self.tabsMid_frame)
        self.tabBottom.setMaximumSize(QtCore.QSize(16777215, 50))
        self.tabBottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tabBottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tabBottom.setObjectName("tabBottom")
        self.verticalLayout_4.addWidget(self.tabBottom)
        self.horizontalLayout_4.addWidget(self.tabsMid_frame)
        self.tabsRight_frame = QtWidgets.QFrame(self.tabsHolder_frame)
        self.tabsRight_frame.setMaximumSize(QtCore.QSize(10, 16777215))
        self.tabsRight_frame.setStyleSheet("")
        self.tabsRight_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tabsRight_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tabsRight_frame.setObjectName("tabsRight_frame")
        self.horizontalLayout_4.addWidget(self.tabsRight_frame)
        self.verticalLayout_3.addWidget(self.tabsHolder_frame)
        self.underTabs_frame = QtWidgets.QFrame(self.contents_bar)
        self.underTabs_frame.setMaximumSize(QtCore.QSize(16777215, 30))
        self.underTabs_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.underTabs_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.underTabs_frame.setObjectName("underTabs_frame")
        self.verticalLayout_3.addWidget(self.underTabs_frame)
        self.verticalLayout.addWidget(self.contents_bar)
        self.credits_bar = QtWidgets.QFrame(self.mainFrame)
        self.credits_bar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.credits_bar.setStyleSheet("background-color : none;")
        self.credits_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.credits_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.credits_bar.setObjectName("credits_bar")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.credits_bar)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.credits_version = QtWidgets.QFrame(self.credits_bar)
        self.credits_version.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.credits_version.setFrameShadow(QtWidgets.QFrame.Raised)
        self.credits_version.setObjectName("credits_version")
        self.label_alphaversion = QtWidgets.QLabel(self.credits_version)
        self.label_alphaversion.setGeometry(QtCore.QRect(10, 8, 371, 16))
        font = QtGui.QFont()
        font.setFamily("Overpass Mono Light")
        self.label_alphaversion.setFont(font)
        self.label_alphaversion.setStyleSheet("color: rgb(86, 142, 166);")
        self.label_alphaversion.setObjectName("label_alphaversion")
        self.horizontalLayout_3.addWidget(self.credits_version)
        self.credits_right = QtWidgets.QFrame(self.credits_bar)
        self.credits_right.setMaximumSize(QtCore.QSize(90, 16777215))
        self.credits_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.credits_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.credits_right.setObjectName("credits_right")
        self.horizontalLayout_3.addWidget(self.credits_right)
        self.verticalLayout.addWidget(self.credits_bar)
        self.mainFrameLayout.addWidget(self.mainFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "Bourdonnements Project Manager"))
        self.btn_maximize.setToolTip(_translate("MainWindow", "Minimize"))
        self.btn_minimize.setToolTip(_translate("MainWindow", "Maximize"))
        self.btn_close.setToolTip(_translate("MainWindow", "Close"))
        self.label_user.setText(_translate("MainWindow", "Current User:"))
        self.comboBox_User.setItemText(0, _translate("MainWindow", "Choose User"))
        self.comboBox_User.setItemText(1, _translate("MainWindow", "Aude"))
        self.comboBox_User.setItemText(2, _translate("MainWindow", "Lena"))
        self.comboBox_User.setItemText(3, _translate("MainWindow", "PierreLouis"))
        self.comboBox_User.setItemText(4, _translate("MainWindow", "Martin"))
        self.comboBox_User.setItemText(5, _translate("MainWindow", "Melanie"))
        self.comboBox_User.setItemText(6, _translate("MainWindow", "Zoe"))
        self.btn_updateUser.setText(_translate("MainWindow", "Update"))
        self.overview_btn.setText(_translate("MainWindow", "OVERVIEW"))
        self.assets_btn.setText(_translate("MainWindow", "ASSETS"))
        self.shots_btn.setText(_translate("MainWindow", "SHOTS"))
        self.compo_btn.setText(_translate("MainWindow", "COMPO"))
        self.editing_btn.setText(_translate("MainWindow", "EDITING"))
        self.ressources_btn.setText(_translate("MainWindow", "RESSOURCES"))
        self.label_alphaversion.setText(_translate("MainWindow", "by TEILLET Martin. PRE ALPHA - version 0.0.1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

## ==> GUI FILE
from main import *

## ==> GLOBALS

GLOBAL_STATE = 0

class UIFunctions(Ui_MainWindow):

    ## ==> MAXIMIZE RESTORE FUNCTION
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        # IF NOT MAXIMIZED
        if status == 0:
            self.showMaximized()

            # SET GLOBAL TO 1
            GLOBAL_STATE = 1

            #IF MAXIMIZED REMOVE MARGINS AND BORDER RADIUS
            self.ui.mainFrame.setContentsMargins(0, 0, 0, 0)
            self.ui.mainFrame.setStyleSheet("background-color: rgb(28, 33, 35);border-radius :0px;")
            self.ui.btn_maximize.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.mainFrame.setContentsMargins(10, 10, 10, 10)
            self.ui.mainFrame.setStyleSheet("background-color: rgb(28, 33, 35);border-radius :10px;")
            self.ui.btn_maximize.setToolTip("Maximize")
    
    ## ==> UI DEFINITIONS
    def uiDefinitions(self):


        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
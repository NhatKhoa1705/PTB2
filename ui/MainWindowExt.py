from ui.MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButtonSolve.clicked.connect(self.Solve)

    def showWindow(self):
            self.MainWindow.show()
    def Solve(self):
        pass





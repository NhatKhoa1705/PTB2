from Utils.Function import firstDegree, quadraticEquation
from ui.MainWindow import Ui_MainWindow
from Utils import Function

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
        a=float(self.lineEditA.text())
        b=float(self.lineEditB.text())
        c=float(self.lineEditC.text())
        result=quadraticEquation(a,b,c)
        self.lineEditResult.setText(result)









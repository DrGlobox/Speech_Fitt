from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from mainWindow import *

def main(args):

    app = QApplication(args)
    app.connect(app, SIGNAL("lastWindowClosed()"), app, SLOT("quit()"))

    mainWindow = MainWindow()
    mainWindow.show()

    app.exec_()



if __name__ == "__main__":
    main(sys.argv)

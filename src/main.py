from gui_interface import (Ui_MainWindow)
from nst import *

from PySide2 import *

def main():
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
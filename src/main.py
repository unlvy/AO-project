from gui_interface import (Ui_MainWindow)
from nst import *

from PyQt5 import *

def main():
	import sys
	app = QtWidgets.QApplication(sys.argv)
	ui = Ui_MainWindow()
	ui.setupUi()
	ui.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()

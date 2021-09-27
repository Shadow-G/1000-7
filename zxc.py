import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint
from gui import Ui_MainWindow

class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.status = 'cs16'

		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

		self.start = QPoint(0, 0)	# +
		self.pressing = False 		# +

		# нажатие на кнопки
		self.bt_exit.clicked.connect(self.myClose)
		self.bt_svernut.clicked.connect(self.myMinimize)


	def myClose(self):
		self.close()

	def myMinimize(self):
		self.showMinimized()

	def mousePressEvent(self, event):
		self.start = self.mapToGlobal(event.pos())
		self.pressing = True

	def mouseMoveEvent(self, event):
		if self.pressing:
			self.end = self.mapToGlobal(event.pos())
			self.movement = self.end-self.start
			self.setGeometry(self.mapToGlobal(self.movement).x(),
								self.mapToGlobal(self.movement).y(),
								self.width(),
								self.height())
			self.start = self.end

	def mouseReleaseEvent(self, QMouseEvent):
		self.pressing = False


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = ExampleApp()
	window.show()
	sys.exit(app.exec_())

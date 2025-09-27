from PySide6 import QtCore, QtGui, QtWidgets
from shiboken6 import wrapInstance
import maya.OpenMayaUI as omui
import os

ICON_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'icons'))

class PrimitiveCreatorDialog(QtWidgets.QDialog):
	def __init__(self, parent = None):
		super().__init__(parent)

		self.resize(300,300)
		self.setWindowTitle('Primitive Creator')

		self.main_Layout = QtWidgets.QVBoxLayout()
		self.setLayout(self.main_Layout)

		self.primitive_listWidget = QtWidgets.QListWidget()
		self.primitive_listWidget.setIconSize(QtCore.QSize(60,60))
		self.primitive_listWidget.setSpacing(8)
		self.primitive_listWidget.setViewMode(QtWidgets.QListView.IconMode)
		self.primitive_listWidget.setMovement(QtWidgets.QListView.Static)
		self.primitive_listWidget.setResizeMode(QtWidgets.QListView.Adjust)

		self.main_Layout.addWidget(self.primitive_listWidget)

		self.name_Layout = QtWidgets.QHBoxLayout()
		self.main_Layout.addLayout(self.name_Layout)

		self.name_Label = QtWidgets.QLabel('Name :')
		self.name_LineEdit = QtWidgets.QLineEdit()
		self.name_Layout.addWidget(self.name_Label)
		self.name_Layout.addWidget(self.name_LineEdit)

		self.button_Layout = QtWidgets.QHBoxLayout()
		self.main_Layout.addLayout(self.button_Layout)
		self.create_button = QtWidgets.QPushButton('Create')
		self.cancel_button = QtWidgets.QPushButton('Cancel')
		self.button_Layout.addStretch()
		self.button_Layout.addWidget(self.create_button)
		self.button_Layout.addWidget(self.cancel_button)

		self.initIconWidgets()

	def initIconWidgets(self):
		prims = ['cone', 'cube', 'sphere', 'torus']
		for prim in prims:
			item = QtWidgets.QListWidgetItem(prim)
			item.setIcon(QtGui.QIcon(os.path.join(ICON_PATH, f'{prim}.png')))
			self.primitive_listWidget.addItem(item)

def run():
	global ui

	try:
		ui.close()
	except:
		pass
	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
	ui = PrimitiveCreatorDialog(parent=ptr)
	ui.show()
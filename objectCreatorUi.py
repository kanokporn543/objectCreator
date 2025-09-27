try:
	from PySide6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapInstance
except:
	from PySide2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance

import maya.OpenMayaUI as omui
import os

ICON_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'icons'))

class objectCreatorDialog(QtWidgets.QDialog):
	def __init__(self, parent = None):
		super().__init__(parent)

		self.resize(300,350)
		self.setWindowTitle('Object Creator')

		self.main_Layout = QtWidgets.QVBoxLayout()
		self.setLayout(self.main_Layout)

		self.object_listWidget = QtWidgets.QListWidget()
		self.object_listWidget.setIconSize(QtCore.QSize(60,60))
		self.object_listWidget.setSpacing(8)
		self.object_listWidget.setViewMode(QtWidgets.QListView.IconMode)
		self.object_listWidget.setMovement(QtWidgets.QListView.Static)
		self.object_listWidget.setResizeMode(QtWidgets.QListView.Adjust)

		self.object_listWidget = QtWidgets.QListWidget()
		self.main_Layout.addWidget(self.object_listWidget)

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

def initIconWidgets(self):
		objs = ['cone', 'cube', 'sphere', 'torus']
		for obj in objs:
			item = QtWidgets.QListWidgetItem(prim)
			item.setIcon(QtGui.QIcon(os.path.join(ICON_PATH, f'{obj}.png')))
			self.object_listWidget.addItem(item)

def run():
	global ui

	try:
		ui.close()
	except:
		pass

	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
	ui = objectCreatorDialog(parent=ptr)
	ui.show()		


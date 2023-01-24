#This program gets two values from a DB into lineEdits.
import sys
import os
from pedes import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.pedesid)
     self.ui.pushButton_6.clicked.connect(self.pedescnt)
     self.ui.pushButton_3.clicked.connect(self.audiocre)
     self.ui.pushButton_4.clicked.connect(self.audiorun)
     self.ui.pushButton_5.clicked.connect(self.pedesan)
     self.ui.pushButton_7.clicked.connect(self.pedesans)
     

  def pedesid(self):
    os.system("python pedest1.py")

  def pedescnt(self):
    os.system("python pedest2.py")

  def audiocre(self):
    os.system("python pedest3.py")

  def audiorun(self):
    os.system("python pedest4.py")
	
  def pedesan(self):
    os.system("python pedest5.py")

  def pedesans(self):
    os.system("python pedest6.py")

	


          
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore
from name_ui import *
from name_190105 import *

class MyForm(QtGui.QMainWindow):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    self.ui = Ui_Form()
    self.ui.setupUi(self)

  def form_start(self):
    firstName = self.ui.lineEdit.text()
    
    try:
      firstName = int(firstName)
    except:
      QtGui.QMessageBox.question(
        self,
        u'확인',
        u"사용할 성의 한자 획수(숫자)를 입력해주세요",
        QtGui.QMessageBox.Ok
      )

    good_name_result = ""
    for i in suri_ohang(good_name(firstName)):
      # print("%02d + %02d + %02d = %02d" %(i[0],i[1],i[2],i[3]))
      good_name_result += "%02d + %02d + %02d = %02d\n" %(i[0],i[1],i[2],i[3])
 
    rich_name_result = ""
    for i in suri_ohang(rich_name(firstName)):
      # print("%02d + %02d + %02d = %02d" %(i[0],i[1],i[2],i[3]))
      rich_name_result += "%02d + %02d + %02d = %02d\n" %(i[0],i[1],i[2],i[3])
    
    self.ui.textEdit.setText(good_name_result)
    self.ui.textEdit_2.setText(rich_name_result)
      
    return

  def form_exit(self):
    QtCore.QCoreApplication.instance().quit()
    return

def main():
  app = QtGui.QApplication(sys.argv)
  myapp = MyForm()
  myapp.show()
  app.exec_()

if __name__=='__main__':
  main()

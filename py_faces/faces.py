import sys
from PyQt5 import QtGui, QtCore, QtWidgets
import cv2
from face_gui import Ui_MainWindow

class faces(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(faces, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    form = faces()
    form.show()
    sys.exit(app.exec_())

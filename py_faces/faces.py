import sys
from PyQt5 import QtCore, QtWidgets
from face_gui import Ui_MainWindow
from cv_camera import cv_camera


class faces(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(faces, self).__init__()
        self.setupUi(self)
        self.capture = None
        self.start_pushButton.clicked.connect(self.start)

    def start(self):
        if not self.capture:
            self.camera = cv_camera(0)
            self.stop_pushButton.clicked.connect(self.stop)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get_camera_frame)
        self.timer.start(1000./self.camera.fps)

    def stop(self):
        self.timer.stop()

    def get_camera_frame(self):
        pix = self.camera.get_frame()
        self.video_frame_label.setPixmap(pix)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = faces()
    form.show()
    sys.exit(app.exec_())

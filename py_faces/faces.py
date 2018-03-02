import sys
from PyQt5 import QtCore, QtWidgets
from face_gui import Ui_MainWindow
from cv_camera import cv_camera


class faces(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(faces, self).__init__()
        self.setupUi(self)
        self.camera = None
        self.start_pushButton.clicked.connect(self.start)
        self.info_label.setText('so fresh and so clean')

    def start(self):
        if not self.camera:
            self.camera = cv_camera(0)
            self.stop_pushButton.clicked.connect(self.stop)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get_camera_frame)
        self.timer.start(1000./self.camera.fps)
        self.info_label.setText('camera started')

    def stop(self):
        self.timer.stop()
        self.camera.release()
        self.camera = None
        self.info_label.setText('camera stopped')

    def get_camera_frame(self):
        pix = self.camera.get_frame()
        self.video_frame_label.setPixmap(pix)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = faces()
    form.show()
    sys.exit(app.exec_())

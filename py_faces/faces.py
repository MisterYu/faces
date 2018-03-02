import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from face_gui import Ui_MainWindow
from cv_camera import cv_camera
from face_detect import FaceDetect
import cv2


class faces(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(faces, self).__init__()
        self.setupUi(self)
        self.camera = None
        self.face_detector = FaceDetect()
        self.start_pushButton.clicked.connect(self.start)
        self.info_label.setText('so fresh and so clean')

        self.face_detect = False
        self.face_detect_checkBox.stateChanged.connect(self.update_face_detect)

    def start(self):
        if not self.camera:
            self.camera = cv_camera(0)
            self.stop_pushButton.clicked.connect(self.stop)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get_camera_frame)
        self.timer.start(1000./self.camera.fps)
        self.info_label.setText('camera started')

    def update_face_detect(self):
        self.face_detect = self.face_detect_checkBox.isChecked()

    def stop(self):
        self.timer.stop()
        self.info_label.setText('camera stopped')

    def get_camera_frame(self):
        frame = self.camera.get_frame()
        if self.face_detect:
            faces = self.face_detector.find_in_frame(frame)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        img = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(img)
        self.video_frame_label.setPixmap(pix)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = faces()
    form.show()
    sys.exit(app.exec_())

import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from face_gui import Ui_MainWindow
from cv_camera import cv_camera
from face_detect import FaceDetect
from face_recognition import FaceRecognition
import cv2


class faces(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(faces, self).__init__()
        self.setupUi(self)
        self.camera = None
        self.face_detector = FaceDetect()
        self.face_recognizer = FaceRecognition()
        self.face_recognizer.train('../face_data/')
        self.start_pushButton.clicked.connect(self.start)
        self.info_label.setText('so fresh and so clean')

        self.face_detect = False
        self.face_detect_checkBox.stateChanged.connect(self.update_face_detect)

        self.face_recognition = False
        self.face_recognition_checkBox.stateChanged.connect(self.update_face_recognition)

        self.b_threshold = self.confidence_spinBox.value()
        self.confidence_spinBox.valueChanged.connect(self.update_threshold)

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
        if not self.face_detect:
            self.face_detect_label.setText('face dectection off')

    def update_face_recognition(self):
        self.face_recognition = self.face_recognition_checkBox.isChecked()
        if not self.face_recognition:
            self.face_recognition_label.setText('Beyonce recognition off')

    def update_threshold(self):
        self.b_threshold = self.confidence_spinBox.value()

    def stop(self):
        self.timer.stop()
        self.info_label.setText('camera stopped')

    def get_camera_frame(self):
        frame = self.camera.get_frame()
        if self.face_detect:
            bboxes, faces = self.face_detector.in_frame(frame)
            self.face_detect_label.setText('{0} faces found'.format(len(faces)))
            if self.face_recognition:
                for bbox, face in zip(bboxes, faces):
                    label, confidence = self.face_recognizer.predict_face(face)
                    str_recog = 'Beyonce not recognized'
                    box_color = (204, 255, 0)
                    if confidence > self.b_threshold:
                        str_recog = 'Beyonce recognized @{0:5.4f} confidence'.format(confidence)
                        box_color = (209, 159, 232)
                    self.face_recognition_label.setText(str_recog)
                    x, y, w, h = bbox
                    cv2.rectangle(frame, (x, y), (x+w, y+h), box_color, 2)

        img = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(img)
        self.video_frame_label.setPixmap(pix)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = faces()
    form.show()
    sys.exit(app.exec_())

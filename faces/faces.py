import sys
import numpy as np
from PyQt5 import QtCore, QtWidgets, QtGui
from face_gui import Ui_MainWindow
from cv_camera import cv_camera
from face_detect import FaceDetect
from face_recognition import FaceRecognition
import cv2
import hulk
from morse_code import MorseCodeDecoder


class faces(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(faces, self).__init__()
        self.setupUi(self)

        # init objects that process faces
        self.face_detector = FaceDetect()
        self.eye_detector = FaceDetect('eye')
        self.morse_code_decoder = MorseCodeDecoder()
        self.face_recognizer = FaceRecognition()    # this one is SLOOOOwwww
        self.face_recognizer.train('../face_data/')

        # init cameras
        self.camera = cv_camera()

        # init and connect controls
        self.start_pushButton.clicked.connect(self.start)
        self.camera_spinBox.setMaximum(self.camera.n_cameras-1)
        self.camera_spinBox.valueChanged.connect(self.change_camera)
        self.info_label.setText('ready to go!')

        self.eye_detect = False
        self.eyes_checkBox.stateChanged.connect(self.update_eye_detect)

        self.hulk_out = False
        self.hulk_checkBox.stateChanged.connect(self.update_hulk_out)

        self.face_detect = False
        self.face_detect_checkBox.stateChanged.connect(self.update_face_detect)

        self.face_recognition = False
        self.face_recognition_checkBox.stateChanged.connect(self.update_face_recognition)

        self.b_threshold = self.confidence_spinBox.value()
        self.confidence_spinBox.valueChanged.connect(self.update_threshold)

    def start(self):
        self.stop_pushButton.clicked.connect(self.stop)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.process_display_frame)
        self.timer.start(1000./self.camera.fps)
        self.info_label.setText('camera started')

    def update_eye_detect(self):
        self.eye_detect = self.eyes_checkBox.isChecked()

    def update_hulk_out(self):
        self.hulk_out = self.hulk_checkBox.isChecked()

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

    def change_camera(self):
        i_new_cam = self.camera_spinBox.value()
        self.camera.i_current_camera = i_new_cam

    def stop(self):
        self.timer.stop()
        self.info_label.setText('camera stopped')

    def process_display_frame(self):
        # pull a frame from chosen camera
        frame = self.camera.get_frame()

        if self.face_detect:
            # do face detection
            bboxes, faces = self.face_detector.in_frame(frame)

            # non-Beyonce color
            box_color = (204, 255, 0)

            # update face status
            self.face_detect_label.setText('{0} faces found'.format(len(faces)))

            # loop thru faces and draw boxes in frame
            for bbox, face in zip(bboxes, faces):
                # do Beyonce reconition
                if self.face_recognition:
                    label, confidence = self.face_recognizer.predict_face(face)
                    # default to no Beyonce; it's not common after all...
                    str_recog = 'Beyonce not recognized'

                    # if confidence of detection > threshold change text and box color
                    if confidence > self.b_threshold:
                        str_recog = 'Beyonce recognized @{0:5.4f} confidence'.format(confidence)
                        box_color = (209, 159, 232)
                    self.face_recognition_label.setText(str_recog)
                # draw bounding boxes
                x, y, w, h = bbox

                if self.eye_detect:
                    eye_bboxes, eyes = self.eye_detector.in_frame(face)
                    self.morse_code_decoder.update_state(len(eyes))
                    str_morse_code = 'Eye say: ' + self.morse_code_decoder.get_char_buffer()
                    self.morse_code_label.setText(str_morse_code)

                if self.hulk_out:
                    # make face green
                    hulk_face = hulk.angry(face)
                    # swap out face
                    frame[y:y+h, x:x+w, :] = hulk_face
                cv2.rectangle(frame, (x, y), (x+w, y+h), box_color, 2)

        # do Qt things to frame so it can be set in a QLabel
        img = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(img)
        self.video_frame_label.setPixmap(pix)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = faces()
    form.show()
    sys.exit(app.exec_())

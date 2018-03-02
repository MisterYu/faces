from PyQt5 import QtGui
import cv2


class cv_camera():
    def __init__(self, *args):
        self.fps = 24
        self.cap = cv2.VideoCapture(*args)
        self.isCapturing = False
        self.ith_frame = 1

    def setFPS(self, fps):
        self.fps = fps

    def get_frame(self):
        ret, frame = self.cap.read()

        # Save images if isCapturing
        if self.isCapturing:
            cv2.imwrite('img_%05d.jpg'%self.ith_frame, frame)
            self.ith_frame += 1

        # My webcam yields frames in BGR format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame

    def capture(self):
        if not self.isCapturing:
            self.isCapturing = True
        else:
            self.isCapturing = False
    # ------ Modification ------ #

    def release(self):
        self.cap.release()

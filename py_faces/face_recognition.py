import os
import cv2
import numpy as np
from face_detect import FaceDetect


class face_recognition():
    def __init__(self):
        self.face_detector = FaceDetect()
        self.face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        # TODO choose a recognizer
        # or use EigenFaceRecognizer by replacing above line with
        # face_recognizer = cv2.face.EigenFaceRecognizer_create()
        # or use FisherFaceRecognizer by replacing above line with
        # face_recognizer = cv2.face.FisherFaceRecognizer_create()
        self.faces = []
        self.labels = []
        self.label_dict = {}

    def load_training_data(self, path):
        if os.path.isdir(path):
            n_trainees = 1
            for training_dir in os.listdir(path):
                label = os.path.basename(training_dir)
                self.label_dict[n_trainees] = label
                # TODO parallize this for speed up later
                for f in os.listdir(path+'/'+training_dir):
                    # build correct path
                    img_path = '/'.join([path,training_dir,f])
                    # detect face; assume only 1 face and it the 1st one
                    bbox, face = self.face_detector.in_file(img_path)
                    # append respective list
                    self.faces.append(face[0])
                    self.labels.append(n_trainees)
                n_trainees += 1

    def train(self, path):
        # load training data if none
        if not self.faces and not self.labels:
            self.load_training_data(path)

        # train
        if self.faces and self.labels and len(self.faces) == len(self.labels):
            self.face_recognizer.train(self.faces, np.array(self.labels))

    def predict_img(self, img):
        bbox, faces = self.face_detector.in_frame(img)
        label, confidence = self.face_recognizer.predict(faces[0])
        return label, confidence

    def predict_file(self, fname):
        img = cv2.imread(fname)
        label, confidence = self.predict_img(img)
        return label, confidence

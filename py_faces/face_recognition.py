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
        self.avg_face_dim = ()

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

    def uniform_faces(self):
        # collect dimensions of all faces
        face_dims = [f.shape for f in self.faces]
        # get average value
        self.avg_face_dim = tuple(np.mean(face_dims, axis=0).astype(int))
        # resize all to be the same size
        self.faces = [cv2.resize(face, self.avg_face_dim) for face in self.faces]

    def train(self, path):
        # load training data if none
        if not self.faces and not self.labels:
            self.load_training_data(path)
            self.uniform_faces()

        # train
        if self.faces and self.labels and len(self.faces) == len(self.labels):
            self.face_recognizer.train(self.faces, np.array(self.labels))

    def predict_img(self, img):
        # find face(s)
        bbox, faces = self.face_detector.in_frame(img)
        # make face same size as training data
        if self.avg_face_dim:
            faces[0] = cv2.resize(faces[0], self.avg_face_dim)
        # predict
        label, confidence = self.face_recognizer.predict(faces[0])
        return label, confidence

    def predict_file(self, fname):
        img = cv2.imread(fname)
        label, confidence = self.predict_img(img)
        return label, confidence

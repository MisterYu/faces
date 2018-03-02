import os
import cv2
from face_detect import FaceDetect


class face_recognition():
    def __init__(self):
        self.face_detector = FaceDetect()

    def train(self, path):
        if os.path.isdir(path):
            faces = []
            labels = []
            for training_dir in os.listdir(path):
                label = os.path.basename(training_dir)
                print(label)
                for f in os.listdir(path+'/'+training_dir):
                    print('\t',f)
                    img_path = '/'.join([path,training_dir,f])
                    bbox, face = self.face_detector.in_file(img_path)
                    # assume only 1 face and it the 1st one
                    faces.append(face[0])
                    labels.append(label)
        else:
            return

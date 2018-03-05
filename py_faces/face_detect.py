import cv2


class FaceDetect():
    feature_file = {
        'eye':'opencv_files/haarcascade_eye.xml',
        'face0':'opencv_files/haarcascade_frontalface_24x24.xml',
        'face1':'opencv_files/haarcascade_frontalface_20x20.xml',
        'face2':'opencv_files/lbpcascade_frontalface.xml'
    }

    def __init__(self, feature=''):
        # TODO enable hot swapping different CascadeClassifiers or parameters
        if feature in self.feature_file.keys():
            cascPath = self.feature_file[feature]
        else:
            # default to face 24x24
            cascPath = 'opencv_files/haarcascade_frontalface_24x24.xml'
        self.faceCascade = cv2.CascadeClassifier(cascPath)

    def in_frame(self, frame):
        # suck the color out image
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # get bounding box(es) for face from cascade classifier
        bbox = self.faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
        )
        # crop face(s)
        faces = [gray[y:y+w, x:x+h] for x,y,w,h in bbox]

        return bbox, faces

    def in_file(self, fname):
        # get pixels from file
        frame = cv2.imread(fname)
        # get bounding box(es) and face(s)
        bbox, faces = self.in_frame(frame)
        return bbox, faces

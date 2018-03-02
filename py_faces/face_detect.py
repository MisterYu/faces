import cv2


class FaceDetect():
    def __init__(self):
        # TODO enable hot swapping different CascadeClassifiers or parameters
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

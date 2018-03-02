import cv2


class FaceDetect():
    def __init__(self):
        # TODO enable swapping different CascadeClassifiers or parameters
        cascPath = 'opencv_files/haarcascade_frontalface_24x24.xml'
        self.faceCascade = cv2.CascadeClassifier(cascPath)

    def in_frame(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        bbox = self.faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
        )

        faces = [gray[y:y+w, x:x+h] for x,y,w,h in bbox]

        return bbox, faces

    def in_file(self, fname):
        frame = cv2.imread(fname)
        bbox, faces = self.in_frame(frame)
        return bbox, faces

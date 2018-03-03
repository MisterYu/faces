import cv2


class cv_camera():
    def __init__(self, *args):
        self.fps = 24
        self.isCapturing = False
        self.ith_frame = 1
        max_cameras = 10
        self.cameras = [cv2.VideoCapture(i)
                        for i in range(max_cameras)
                        if cv2.VideoCapture(i).isOpened()]
        self.n_cameras = len(self.cameras)
        self.i_current_camera = 0

    def setFPS(self, fps):
        self.fps = fps

    def get_frame(self):
        ret, frame = self.cameras[self.i_current_camera].read()

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

    def release(self):
        for camera in self.cameras:
            camera.release()
